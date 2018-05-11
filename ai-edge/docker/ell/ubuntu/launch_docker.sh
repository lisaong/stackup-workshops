#!/usr/bin/env bash
docker run -it \
  -v `pwd`/scripts:/scripts \
  lisaong/debian-miniconda3-ell:2.3.3 bash
