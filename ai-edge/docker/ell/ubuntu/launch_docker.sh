#!/usr/bin/env bash
docker run -it \
  -v `pwd`/scripts:/scripts \
  -v `pwd`/models:/tmp/models \
  lisaong/debian-miniconda3-ell:2.3.3 bash
