#!/usr/bin/env bash
docker run -it \
  -v `pwd`/scripts:/scripts \
  -v `pwd`/models:/tmp/models \
  lisaong/debian-miniconda3-ell:2.3.3 bash

# To compile Open MPI (needed for CNTK):
# root# cd /openmpi-1.10.3 && make -j all && make install