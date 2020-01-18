using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace monit_hackernews.Hubs
{
    public class NewsHub : Hub
    {
        public async Task SendMessage(string title, string url)
        {
            await Clients.All.SendAsync("ReceiveMessage", title, url);
        }
    }
}