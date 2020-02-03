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

3. Start the subscriber
```
cd subscribe
python client.py macs.txt
```

## Publisher (Raspberry Pi)
1. Install docker
2. Run the docker container to publish the ip address via MQTT
```
cd publish
sh launch_docker.sh
```
