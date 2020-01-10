using System;
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

        public async Task<int[]> GetHeadlinesAsync()
        {
            var responseString = await _httpClient.GetStringAsync(_newsServiceUrl);
            var items = JsonSerializer.Deserialize<int[]>(responseString);
            return items;
        }
    }
}
