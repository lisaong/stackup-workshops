#!/usr/bin/env bash
# Note: use -it for interactive
#       use -d for daemon

docker run -it \
  -v ~/stackup-workshops/pi-dotnetcore/projects:/code \
  lisaong/rpi-dotnetcore-3:1.0
