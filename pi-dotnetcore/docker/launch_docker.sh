#!/usr/bin/env bash
# Note: use run for interactive
#       use up -d for daemon

mkdir -p ../projects

# pulls containers
docker-compose up

# run as interactive mode
docker-compose run dotnetcore
