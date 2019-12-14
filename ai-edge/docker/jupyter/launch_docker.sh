#!/usr/bin/env bash
# Note: use -it for interactive
#       use -d for daemon
docker run -d \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  -p=48888:8888 \
  -e PASSWORD='a1-edge' \
  lisaong/rpi-jupyter-tf2-torch-py37:1.0
