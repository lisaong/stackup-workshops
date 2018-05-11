#!/usr/bin/env bash
docker run -it \
  -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks \
  -p:28888:8888 \
  lisaong/pi3-miniconda3-ell:2.3.3 bash
