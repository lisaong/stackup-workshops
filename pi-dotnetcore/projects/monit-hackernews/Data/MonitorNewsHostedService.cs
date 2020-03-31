using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using System.Text.Json;
using Microsoft.AspNetCore.SignalR;
using Microsoft.Extensions.Hosting;
using monit_hackernews.Hubs;

// https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/background-tasks-with-ihostedservice
namespace monit_hackernews.Data
{
    public class MonitorNewsHostedService : BackgroundService
    {
        private const double _intervalMinutes = 15;
        private const int _topN = 5;

        private readonly IHubContext<NewsHub, INewsHub> _hubContext;
        private readonly NewsHeadlineFetcher _newsFetcher;

        public MonitorNewsHostedService(NewsHeadlineFetcher newsFetcher, IHubContext<NewsHub, INewsHub> hubContext)
        {
            _hubContext = hubContext;
            _newsFetcher = newsFetcher;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                // Do background work
                var headlines = await _newsFetcher.GetHeadlinesAsync();

                // TODO: check if actually a new headline

                // Publish
                await PublishUpdates(headlines);

                // Throttle
                await Task.Delay((int)(_intervalMinutes * 60 * 1000));
            }
        }

        private async Task PublishUpdates(List<NewsHeadline> headlines)
        {
            // TODO: https://markheath.net/post/async-antipatterns
            foreach(var headline in headlines)
            {
                await _hubContext.Clients.All.ReceiveMessage(headline);
            }
        }
    }
}