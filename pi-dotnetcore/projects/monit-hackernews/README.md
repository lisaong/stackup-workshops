### Hackernews Monitoring Service

#### On Development Machine
From a command prompt:

```
cd monit-hackernews
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

#### References
- https://codedbeard.com/iot-with-blazor-on-raspberry-pi-part-3/
- https://github.com/HackerNews/API