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
        private readonly MonitorNewsHostedService _bgService;

        // Dependency-injection
        // https://docs.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/use-httpclientfactory-to-implement-resilient-http-requests#multiple-ways-to-use-httpclientfactory
        public MonitorNewsService(MonitorNewsHostedService service)
        {
            _bgService = service;
        }

        public async Task<List<NewsHeadline>> GetHeadlinesAsync()
        {
            // TODO: get from event bus
            return await _bgService.GetHeadlinesAsync();
        }
    }
}
