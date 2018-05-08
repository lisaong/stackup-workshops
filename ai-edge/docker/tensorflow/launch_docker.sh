#!/usr/bin/env bash
docker run -it -p 18888:8888 -v ~/stackup-workshops/ai-edge:/notebooks/myNotebooks lisaong/rpi-docker-tensorflow:tf1.8.0 bash /run_jupyter.sh --allow-root