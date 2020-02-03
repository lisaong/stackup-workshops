#!/usr/bin/env bash
# https://community.wia.io/d/15-accessing-the-host-from-inside-a-docker-container
# --network="host" attaches the docker container to the local network
# and allows querying of the ipaddresses of the host's network interfaces
sudo docker run -it \
  --volume $(pwd):/code \
  --network="host" \
  lisaong/armv71-mqttmyip:1.0 \
  python /code/publish.py eth0 mqtt.eclipse.org 1883
