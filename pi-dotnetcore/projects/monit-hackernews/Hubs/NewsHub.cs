using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;
using monit_hackernews.Data;

namespace monit_hackernews.Hubs
{
    // https://docs.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-3.1#strongly-typed-hubs
    public interface INewsHub
    {
        Task ReceiveHeadline(NewsHeadline headline);
    }

    public class NewsHub : Hub<INewsHub>
    {
        // BUGBUG: where is SendTimeToClients used? Blazor?
        public async Task SendHeadline(NewsHeadline headline)
        {
            await Clients.All.ReceiveHeadline(headline);
        }
    }
}