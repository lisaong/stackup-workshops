#!/usr/bin/env bash

sudo docker run -it \
   -v ~/stackup-workshops/pi-mediapipe/cross_compile/libs:/dest \
   -w /dest \
   sgtwilko/rpi-raspbian-opencv:stretch-balena-3 \
   /bin/bash
