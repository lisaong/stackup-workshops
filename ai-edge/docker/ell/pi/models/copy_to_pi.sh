#!/usr/bin/env bash
pushd ..
scp -r models pi@$1:/home/pi/stackup-workshops/ai-edge/docker/ell/pi
popd
