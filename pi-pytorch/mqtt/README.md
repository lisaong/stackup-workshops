## Subscriber (Desktop)
1. Create a text file containing all the known mac addresses of your Raspberry Pis, containing 1 address per line:

subscribe/macs.txt
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
2. Run the docker container
```
cd publish
sh launch_docker.sh
```
