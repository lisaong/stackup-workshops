using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using System.Text.Json;

namespace monit_hackernews.Data
{
    public class NewsHeadlineFetcher
    {
        private readonly string _newsServiceUrl;

        private readonly HttpClient _httpClient;

        public NewsHeadlineFetcher(IHttpClientFactory httpClient, IServiceConfiguration configuration)
        {
            // https://www.telerik.com/blogs/.net-core-background-services
            _httpClient = httpClient.CreateClient();
            _newsServiceUrl = configuration.NewsServiceUri;
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

        private Task<string> GetItemAsync(int id)
        {
            var query = String.Format("{0}item/{1}.json", _newsServiceUrl, id);
            return _httpClient.GetStringAsync(query);
        }
        private async Task<Comment> GetCommentAsync(int id)
        {
            var responseString = await GetItemAsync(id);
            return JsonSerializer.Deserialize<Comment>(responseString);
        }

        private async Task<NewsHeadline> GetHeadlineAsync(int id)
        {
            var responseString = await GetItemAsync(id);
            var headline = JsonSerializer.Deserialize<NewsHeadline>(responseString);

            if (headline.kids.Count > 0)
            {
                responseString = await GetItemAsync(headline.kids[0]);
                headline.topComment = JsonSerializer.Deserialize<Comment>(responseString);
            }
            
            return headline;
        }
    }
}