#!/usr/bin/env bash
# Note: use -it for interactive
#       use -d for daemon

docker run -d \
  -v .:/code \
  lisaong/rpi-dotnetcore-3:1.0
