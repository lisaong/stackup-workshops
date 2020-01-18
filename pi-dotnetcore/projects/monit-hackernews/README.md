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

Package into a self-contained deployment (https://docs.microsoft.com/en-us/dotnet/core/deploying/deploy-with-cli)
```
dotnet publish --runtime linux-arm --self-contained true
```

#### On Raspberry Pi

### Generating SSL certificates

1. Kestrel (the cross-platform ASP.NET core web server) requires an SSL certificate. Generate the certificate:
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

2. Update docker/.env to set SSL_PASS to the password you used for generating the cert.

3. Run docker compose, which will launch the server with the SSL cert.
```
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

### References
- https://codedbeard.com/iot-with-blazor-on-raspberry-pi-part-3/
- https://github.com/HackerNews/API
- https://docs.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-3.1
- https://mohitgoyal.co/2018/09/25/use-ssl-certificates-for-dotnet-core-application-in-docker-containers/
