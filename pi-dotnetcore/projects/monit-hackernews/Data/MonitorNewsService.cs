using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR;
using monit_hackernews.Hubs;

namespace monit_hackernews.Data
{
    public class MonitorNewsService
    {
        private const string _newsServiceUrl = "https://hacker-news.firebaseio.com/v0/";

        private readonly HttpClient _httpClient;
        private readonly NewsHub _hub;

        // Dependency-injection
        // https://docs.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/use-httpclientfactory-to-implement-resilient-http-requests#multiple-ways-to-use-httpclientfactory
        public MonitorNewsService(HttpClient httpClient, NewsHub hub)
        {
            _httpClient = httpClient;
            _hub = hub;
        }

        public async Task<List<NewsHeadline>> GetHeadlinesAsync()
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
            return _hub.SendMessage(headline.title, headline.url);
        }

        private async Task<NewsHeadline> GetHeadlineAsync(int id)
        {
            var query = String.Format("{0}item/{1}.json", _newsServiceUrl, id);
            var responseString = await _httpClient.GetStringAsync(query);
            return JsonSerializer.Deserialize<NewsHeadline>(responseString);
        }
    }
}
