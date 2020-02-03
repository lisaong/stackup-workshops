#!/usr/bin/env bash
sudo docker run -it \
  lisaong/armv71-mqttmyip:1.0 \
  python publish.py eth0 iot.eclipse.org
