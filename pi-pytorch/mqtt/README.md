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

3. Start the subscriber listening for topics associated with the MAC addresses in macs.txt. If not specified, will listen for the wlan0 interface.
```
cd subscribe
python client.py macs.txt [--interface eth0]
```

## Publisher (Raspberry Pi)
1. Install docker
2. Place these 2 files in a folder on the Pi, e.g.
```
pi@raspberrypi:~ $ ls publish_ip/ -a
.  ..  docker-compose.yml  .env
```
3. Edit `.env` accordingly to select the interface (e.g. wlan0 or eth0)
4. Start the container. This should be done at least once to pull the container down before configuring to run on reboot.
```
cd publish_ip
docker-compose up
```
5. Configure to run on reboot by adding the following example command to crontab
```
crontab -e
```

Command to add to the end of crontab:
```
@reboot /usr/bin/docker ps && cd $HOME/publish_ip && $HOME/.local/bin/docker-compose up
```
