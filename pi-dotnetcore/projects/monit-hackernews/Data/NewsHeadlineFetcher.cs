using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using System.Text.Json;
using Microsoft.AspNetCore.SignalR;
using Microsoft.Extensions.Hosting;
using monit_hackernews.Hubs;

namespace monit_hackernews.Data
{
    public class NewsHeadlineFetcher
    {
        private const string _newsServiceUrl = "https://hacker-news.firebaseio.com/v0/";

        private readonly HttpClient _httpClient;

        public NewsHeadlineFetcher(IHttpClientFactory httpClient)
        {
            // https://www.telerik.com/blogs/.net-core-background-services
            _httpClient = httpClient.CreateClient();
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
            }
            return headlines;
        }

        private async Task<NewsHeadline> GetHeadlineAsync(int id)
        {
            var query = String.Format("{0}item/{1}.json", _newsServiceUrl, id);
            var responseString = await _httpClient.GetStringAsync(query);
            return JsonSerializer.Deserialize<NewsHeadline>(responseString);
        }
    }
}