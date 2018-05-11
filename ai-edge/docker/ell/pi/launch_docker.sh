#!/usr/bin/env bash
docker run -it \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  -v /opt/vc:/opt/vc \
  -p:28888:8888 \
  lisaong/pi3-miniconda3-ell:2.3.3
