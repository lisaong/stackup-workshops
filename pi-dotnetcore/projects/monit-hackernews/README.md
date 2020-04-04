## Hackernews Monitoring Service

Scenario:
- Deploying an ASP.NET Core service + SignalR hub on Raspberry Pi to monitor Hackernews
- When latest news is updated, the Raspberry Pi will update connected clients using SignalR

Requirements: dotnet core 3.1 (https://dotnet.microsoft.com/download/dotnet-core/3.1)

### Server
#### On Development Machine (PC)

**Development**

Install SQLLite3: https://www.sqlite.org/download.html (Windows: 64-bit DLL (x64) for SQLite version 3.31.1.)

Setup Entity Framework:
```
cd monit-hackernews
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet tool install --global dotnet-ef
dotnet add package Microsoft.EntityFrameworkCore.Design
dotnet ef migrations add InitialCreate
dotnet ef database update
```

Build and run server locally from a command prompt:
```
cd monit-hackernews
dotnet add package Microsoft.AspNetCore.SignalR.Client
dotnet watch run
```

Navigate to https://localhost:5001/fetchdata to test.

**Packaging**

On the PC, package into a self-contained deployment for Raspberry Pi (https://docs.microsoft.com/en-us/dotnet/core/deploying/deploy-with-cli)
```
dotnet publish --runtime linux-arm --self-contained true --configuration Release
dotnet publish --runtime linux-arm --self-contained true --configuration Debug
```

Check the binaries into the git repository.

#### On Raspberry Pi

1. Update this repository to get the ARM deployment binaries

2. Kestrel (the cross-platform ASP.NET core web server) requires an SSL certificate. Generate the certificate:
```
cd docker

openssl req \
 -newkey rsa:2048 \
 -nodes \
 -keyout pi.key \
 -out pi.csr

openssl x509 \
 -signkey pi.key \
 -in pi.csr \
 -req \
 -days 3650 \
 -out pi.crt

openssl pkcs12 \
 -inkey pi.key \
 -in pi.crt \
 -export \
 -out pi.pfx
```

2. Update `docker/.env` to set SSL_PASS to the password you used for generating the cert.

3a. Run docker compose, which will launch the server with the SSL cert path and password specified in the .env.
```
docker-compose up
```
3b. Alternatively, to run as a daemon:
```
docker-compose up -d
```
Once started, logs can be monitored:
```
docker-compose logs -f
```

The output should look like
```
root@DietPi:~/stackup-workshops/pi-dotnetcore/docker# docker-compose logs -f
Attaching to docker_dotnetcore-rt_1
dotnetcore-rt_1  | warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[35]
dotnetcore-rt_1  |       No XML encryptor configured. Key {fa593ccd-6197-4406-a214-ed5befa7b989} may be persisted to storage in unencrypted form.
dotnetcore-rt_1  | info: monit_hackernews.Data.MonitorNewsHostedService[0]
dotnetcore-rt_1  |       Throttle interval 15 minute(s)
dotnetcore-rt_1  | info: System.Net.Http.HttpClient.Default.LogicalHandler[100]
dotnetcore-rt_1  |       Start processing HTTP request GET https://hacker-news.firebaseio.com/v0/topstories.json
dotnetcore-rt_1  | info: System.Net.Http.HttpClient.Default.ClientHandler[100]
dotnetcore-rt_1  |       Sending HTTP request GET https://hacker-news.firebaseio.com/v0/topstories.json
dotnetcore-rt_1  | info: Microsoft.Hosting.Lifetime[0]
dotnetcore-rt_1  |       Now listening on: https://[::]:8081
dotnetcore-rt_1  | info: Microsoft.Hosting.Lifetime[0]
dotnetcore-rt_1  |       Now listening on: http://[::]:8080
dotnetcore-rt_1  | info: Microsoft.Hosting.Lifetime[0]
dotnetcore-rt_1  |       Application started. Press Ctrl+C to shut down.
dotnetcore-rt_1  | info: Microsoft.Hosting.Lifetime[0]
dotnetcore-rt_1  |       Hosting environment: Production
dotnetcore-rt_1  | info: Microsoft.Hosting.Lifetime[0]
dotnetcore-rt_1  |       Content root path: /app
dotnetcore-rt_1  | info: System.Net.Http.HttpClient.Default.ClientHandler[101]
dotnetcore-rt_1  |       Received HTTP response after 1526.7894ms - OK
dotnetcore-rt_1  | info: System.Net.Http.HttpClient.Default.LogicalHandler[101]
dotnetcore-rt_1  |       End processing HTTP request after 1557.3044ms - OK
dotnetcore-rt_1  | info: System.Net.Http.HttpClient.Default.LogicalHandler[100]
dotnetcore-rt_1  |       Start processing HTTP request GET https://hacker-news.firebaseio.com/v0/item/22742349.json
dotnetcore-rt_1  | info: System.Net.Http.HttpClient.Default.ClientHandler[100]
dotnetcore-rt_1  |       Sending HTTP request GET https://hacker-news.firebaseio.com/v0/item/22742349.json
```

4. Navigate to https://ipaddress_of_pi:18081/fetchdata

![example](example.png)

### Client

The console client can be used to subscribe to the SignalR feed, and display the latest headlines, with the top comment and a QR code for the URL.

From a command prompt:

```
cd monit-hackernews/client
dotnet add package Microsoft.Extensions.Logging.Console
dotnet add package QRCoder --source ../third_party/QRCoder/Release
dotnet run [ip_address_of_server(default: localhost)] [port(default: 5001)]
```

![client](client.png)

### References
- https://codedbeard.com/iot-with-blazor-on-raspberry-pi-part-3/
- https://github.com/HackerNews/API
- https://docs.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-3.1
- https://mohitgoyal.co/2018/09/25/use-ssl-certificates-for-dotnet-core-application-in-docker-containers/
- https://medium.com/@sketchmycloud/how-to-deploy-asp-net-core-2-1-applications-on-ubuntu-474062f8db73

