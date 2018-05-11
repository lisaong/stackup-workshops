#!/usr/bin/env bash
sudo docker run -it \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  -p 18888:8888 \
  lisaong/debian-miniconda3-ell:2.3.3 bash
