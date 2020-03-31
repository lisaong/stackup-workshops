using System;
using System.Net.Http;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR.Client;
using monit_hackernews.Data;

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

            // quick and dirty
            string ipAddress = "localhost";
            string port = "5001";
            if (args.Length > 0)
            {
                ipAddress = args[0];
                if (args.Length > 1){
                    port = args[1];
                }
            }

            Uri url = new Uri(String.Format("https://{0}:{1}/newshub", ipAddress, port));
            Console.WriteLine(String.Format("Connecting to {0}", url));

            var connection = new HubConnectionBuilder()
                .WithUrl(url, options => {

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

            connection.On<NewsHeadline>("ReceiveHeadline", (headline) =>
            {
                Console.WriteLine(headline.ToString());
            });

            await connection.StartAsync();
            Console.WriteLine("Press any key to exit.");
            Console.Read();
        }
    }
}
