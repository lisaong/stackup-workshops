using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR.Client;

namespace client
{
    class Program
    {
        // https://dotnettutorials.net/lesson/async-main-csharp/
        static async Task Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var connection = new HubConnectionBuilder()
                .WithUrl("http://localhost:53353/newshub")
                .WithAutomaticReconnect()
                .Build();

            connection.Closed += async (error) =>
            {
                await Task.Delay(new Random().Next(0,5) * 1000);
                await connection.StartAsync();
            };

            await connection.StartAsync();
            Console.WriteLine("Press any key to exist.");
            Console.ReadKey();
        }
    }
}
