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
        private const string _newsServiceUrl = "https://hacker-news.firebaseio.com/v0/";

        private readonly HttpClient _httpClient;
        private readonly IHubContext<NewsHub> _hubContext;

        public MonitorNewsHostedService(IHttpClientFactory httpClient, IHubContext<NewsHub> hubContext)
        {
            // https://www.telerik.com/blogs/.net-core-background-services
            _httpClient = httpClient.CreateClient();
            _hubContext = hubContext;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                // Do background work
                await GetHeadlinesAsync();
            }
        }

        private async Task<List<NewsHeadline>> GetHeadlinesAsync()
        {
            Index topN = 5;
            var responseString = await _httpClient.GetStringAsync(_newsServiceUrl + "topstories.json");
            var items = JsonSerializer.Deserialize<int[]>(responseString);

            List<NewsHeadline> headlines = new List<NewsHeadline>();

            // TODO: https://markheath.net/post/async-antipatterns
            foreach(var item in items[0..topN])
            {
                var headline = await GetHeadlineAsync(item);
                headlines.Add(headline);

                // TODO: check if actually a new headline
                await PublishUpdate(headline);
            }
            return headlines;
        }

        private Task PublishUpdate(NewsHeadline headline)
        {
            return _hubContext.Clients.All.SendAsync("ReceiveMessage", headline);
        }

        private async Task<NewsHeadline> GetHeadlineAsync(int id)
        {
            var query = String.Format("{0}item/{1}.json", _newsServiceUrl, id);
            var responseString = await _httpClient.GetStringAsync(query);
            return JsonSerializer.Deserialize<NewsHeadline>(responseString);
        }

    }
}