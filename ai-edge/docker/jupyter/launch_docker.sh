#!/usr/bin/env bash
docker run -it \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  -p=46006:6006 \
  -p=48888:8888 \
  lisaong/rpi-jupyter:1.0
