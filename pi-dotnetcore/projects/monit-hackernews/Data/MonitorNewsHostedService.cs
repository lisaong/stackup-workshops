using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using monit_hackernews.Hubs;

// https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/background-tasks-with-ihostedservice
namespace monit_hackernews.Data
{
    public class MonitorNewsHostedService : BackgroundService
    {
        private const int _topN = 5;

        private readonly IHubContext<NewsHub, INewsHub> _hubContext;
        private readonly NewsHeadlineFetcher _newsFetcher;
        private readonly IServiceScopeFactory _scopeFactory;
        private readonly IServiceConfiguration _configuration;

        private readonly ILogger _logger;

        public MonitorNewsHostedService(NewsHeadlineFetcher newsFetcher,
            IHubContext<NewsHub, INewsHub> hubContext,
            IServiceScopeFactory scopeFactory,
            IServiceConfiguration configuration,
            ILogger<MonitorNewsHostedService> logger)
        {
            _hubContext = hubContext;
            _newsFetcher = newsFetcher;
            _scopeFactory = scopeFactory;
            _configuration = configuration;
            _logger = logger;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            double interval = 15;
            if (double.TryParse(
                _configuration.ThrottleIntervalMinutes, 
                out interval))
            {
                _logger.LogInformation("Throttle interval {0} minute(s)", interval);
            }
            else
            {
                _logger.LogError("Invalid ThrottleIntervalMinutes, check appsettings*.json. Default to {0} minute(s)", 
                    interval);
            }

            while (!stoppingToken.IsCancellationRequested)
            {
                // Do background work
                var headlines = await _newsFetcher.GetHeadlinesAsync();
                _logger.LogInformation("Fetched {0} headlines", headlines.Count);

                // Publish
                await PublishUpdatesAsync(headlines);

                // Store
                var storeResult = await StoreAsync(headlines);
                _logger.LogInformation("Store result: {0}", storeResult);

                // Throttle
                await Task.Delay((int)(interval * 60 * 1000));
            }
        }

        private async Task PublishUpdatesAsync(List<NewsHeadline> headlines)
        {
            // TODO: https://markheath.net/post/async-antipatterns
            foreach(var headline in headlines)
            {
                await _hubContext.Clients.All.ReceiveHeadline(headline);
            }
            _logger.LogInformation("Published {0} headlines", headlines.Count);
        }

        private Task<int> StoreAsync(List<NewsHeadline> headlines)
        {
            // https://docs.microsoft.com/en-us/ef/core/miscellaneous/configuring-dbcontext#implicitly-sharing-dbcontext-instances-across-multiple-threads-via-dependency-injection
            using (var scope = _scopeFactory.CreateScope())
            {
                using (var dbContext = scope.ServiceProvider.GetRequiredService<NewsHeadlineContext>())
                {
                    foreach (var headline in headlines)
                    {
                        var comment = headline.topComment != null ? headline.topComment.text : "";

                        // https://docs.microsoft.com/en-us/ef/core/get-started/?tabs=netcore-cli
                        var entry = dbContext.Headlines
                            .OrderBy(h => h.Id)
                            .First();
                        if (entry == null)
                        {
                            // Create
                            dbContext.Headlines.Add(new NewsHeadlineModel {
                                Id = headline.id.ToString(),
                                Title = headline.title,
                                Comment = comment
                            });
                        }
                        else
                        {
                            // Update
                            entry.Comment = comment;
                        }
                    }

                    return dbContext.SaveChangesAsync();
                }
            }
        }
    }
}