## Hackernews Monitoring Service

Requirements: Dotnet core 3.1 (https://dotnet.microsoft.com/download/dotnet-core/3.1)

### Server
#### On Development Machine
From a command prompt:

```
cd monit-hackernews
dotnet add package Microsoft.AspNetCore.SignalR.Client
dotnet watch run
```

Navigate to https://localhost:5001

#### On Raspberry Pi

Run docker compose, which will call dotnet run
```
cd docker
docker compose up
```

Navigate to https://ipaddress_of_pi:18081

![example](example.png)

### Client

From a command prompt:

```
cd monit-hackernews/client
dotnet run ip_address_of_server
```
![client](client.png)

#### References
- https://codedbeard.com/iot-with-blazor-on-raspberry-pi-part-3/
- https://github.com/HackerNews/API
- https://docs.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-3.1
