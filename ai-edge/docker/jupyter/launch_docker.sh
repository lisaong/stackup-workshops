#!/usr/bin/env bash
docker run -it \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  -p=48888:8888 \
  -e PASSWORD='a1-edge' \
  lisaong/rpi-jupyter-tf2-torch-py37:1.0
