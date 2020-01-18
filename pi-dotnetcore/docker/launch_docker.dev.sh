#!/usr/bin/env bash
# Launch dotnet core environment for development purposes
# To launch an existing service, use `docker-compose up` intead
#
# Note: use -it for interactive
#       use -d for daemon

mkdir -p ../projects

docker run -u $(id -u):$(id -g) -it \
   -v ~/stackup-workshops/pi-dotnetcore/projects:/code \
   -p=18080:8080 \
   -p=18081:8081 \
   lisaong/rpi-dotnetcore-3:1.1 \
   /bin/bash