using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace monit_hackernews.Data
{
    public class MonitorNewsService
    {
        private const string _newsServiceUrl = "https://hacker-news.firebaseio.com/v0/";

        private readonly HttpClient _httpClient;

        // https://docs.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/use-httpclientfactory-to-implement-resilient-http-requests#multiple-ways-to-use-httpclientfactory
        public MonitorNewsService(HttpClient httpClient)
        {
            _httpClient = httpClient;
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
                headlines.Add(await GetHeadlineAsync(item));
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
