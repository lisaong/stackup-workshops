using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR;
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

        private readonly NewsHeadlineContext _dbContext;

        private readonly IServiceConfiguration _configuration;

        private readonly ILogger _logger;

        public MonitorNewsHostedService(NewsHeadlineFetcher newsFetcher,
            IHubContext<NewsHub, INewsHub> hubContext,
            NewsHeadlineContext dbContext,
            IServiceConfiguration configuration,
            ILogger<MonitorNewsHostedService> logger)
        {
            _hubContext = hubContext;
            _newsFetcher = newsFetcher;
            _dbContext = dbContext;
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

                // Store
                Store(headlines);

                // Publish
                await PublishUpdates(headlines);

                // Throttle
                await Task.Delay((int)(interval * 60 * 1000));
            }
        }

        private async Task PublishUpdates(List<NewsHeadline> headlines)
        {
            // TODO: https://markheath.net/post/async-antipatterns
            foreach(var headline in headlines)
            {
                await _hubContext.Clients.All.ReceiveHeadline(headline);
            }
            _logger.LogInformation("Published {0} headlines", headlines.Count);
        }

        private void Store(List<NewsHeadline> headlines)
        {
            

            _logger.LogInformation("Stored {0} headlines", headlines.Count);
        }
    }
}