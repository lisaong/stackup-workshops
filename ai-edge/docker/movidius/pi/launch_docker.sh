#!/usr/bin/env bash
docker run -it \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  --privileged --net=host \
  -v /dev:/dev:shared -v /media/data2/NCS/:/media/data2/NCS/ \
  lisaong/rpi-movidius:2.04
