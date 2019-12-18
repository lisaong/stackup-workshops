#!/usr/bin/env bash
# Note: use -it for interactive
#       use -d for daemon
mkdir -p ~/notebooks

# Jupyter
docker run -d \
  -v ~/notebooks:/notebooks \
  -p=48888:8888 \
  -e PASSWORD='a1-edge' \
  lisaong/rpi-jupyter-tf2-torch-py37:1.1

# Tensorboard
docker run -d \
  -v ~/notebooks:/notebooks \
  -p=46006:6006 \
  lisaong/rpi-jupyter-tf2-torch-py37:1.1 \
  tensorboard --logdir /notebooks/logs --bind_all