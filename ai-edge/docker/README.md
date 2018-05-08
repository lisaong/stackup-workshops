## Docker install on Raspberry Pi3

Reference: https://github.com/romilly/rpi-docker-tensorflow

```
curl -sSL get.docker.com | sh
sudo usermod -aG docker pi
```

log out, then log back in again for the change to take effect

```
sudo systemctl start docker
```

Build the image
```
docker build -t='lisaong/rpi-docker-tensorflow:tf1.8.0' .
```
