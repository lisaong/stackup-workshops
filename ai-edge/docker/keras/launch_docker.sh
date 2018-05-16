#!/usr/bin/env bash
docker run -it \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  -p=38888:8888 \
  lisaong/rpi-keras:1.0
