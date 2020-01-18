using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace monit_hackernews.Hubs
{
    public class NewsHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }
    }
}