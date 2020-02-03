# IP discovery for Headless Raspberry Pis

## Subscriber (Desktop)
0. Find the MAC address of your Raspberry Pi for the wlan0 interface.
1. Create a text file containing all the known mac addresses of your Raspberry Pis, containing 1 address per line:

Example: subscribe/macs.txt
```
AA:BB:CC:DD:EE
AA:BB:CC:DD:EF
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Start the subscriber for the given interface (defaults to wlan0)
```
cd subscribe
python client.py macs.txt --interface eth0
```

## Publisher (Raspberry Pi)
1. Install docker
2. Option 1: Run the docker container to publish the ip address via MQTT
```
cd publish
sh launch_docker.sh
```

Option 2: If using docker compose, edit .env file accordingly to select the interface
```
cd publish
docker-compose run publish_ip
```

Option 3: If running automatically on reboot, add the following example command to crontab -e
```
@reboot /usr/bin/docker ps && /home/pi/.local/bin/docker-compose run -f /home/pi/publish_ip/ docker-compose.yml publish_ip
```
