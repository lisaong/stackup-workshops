using System;
using System.Net.Http;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR.Client;

namespace client
{
    class Program
    {
        static bool ValidateSslCertificate(
            object sender,
            X509Certificate cert,
            X509Chain certChain,
            SslPolicyErrors policyErrors)
        {
            // Validate the cert here and return true if it's correct.
            // If this is a development app, you could just return true always
            // In production you should ALWAYS either use a trusted cert or check the thumbprint of the cert matches one you expect.
            return true;
        }

        // https://dotnettutorials.net/lesson/async-main-csharp/
        static async Task Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var connection = new HubConnectionBuilder()
                .WithUrl("https://localhost:5001/newshub", options => {

                    // Create a handler that accepts custom (untrusted) certificates
                    var handler = new HttpClientHandler
                    {
                        ClientCertificateOptions = ClientCertificateOption.Manual,
                        ServerCertificateCustomValidationCallback = (sender, cert, chain, sslPolicyErrors) => 
                        { 
                            return ValidateSslCertificate(sender, cert, chain, sslPolicyErrors); 
                        }
                    };

                    // Register the custom handler above and also configure WebSockets
                    options.HttpMessageHandlerFactory = _ => handler;
                    options.WebSocketConfiguration = sockets =>
                    {
                        sockets.RemoteCertificateValidationCallback = 
                            new RemoteCertificateValidationCallback(ValidateSslCertificate);
                    };
                })
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
