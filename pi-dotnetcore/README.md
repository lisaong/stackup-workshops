## .NET Core RaspberryPi

1. Install Docker and Docker Compose on Raspberry Pi
```
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi

```
2. Logout and login for usermod to take effect
3. Install Docker Compose
```
sudo apt-get install python3-pip
sudo pip3 install docker-compose
```
4. Add docker-compose to `$PATH`
```
export PATH=$PATH:$HOME/.local/bin
```

### Launch container

```
cd docker
sh ./launch_docker.sh
```

The `projects` folder is mapped as `/code` in the Docker container
