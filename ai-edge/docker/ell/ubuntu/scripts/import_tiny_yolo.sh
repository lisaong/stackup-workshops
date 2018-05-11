#!/usr/bin/env bash

# Script to run in debian docker instance to import tiny-yolo
# Ref: https://microsoft.github.io/ELL/tutorials/Getting-started-with-object-detection-using-region-of-interest-networks/
#
# docker image to use: lisaong/debian-miniconda3-ell:2.3.3

mkdir -p /tiny-yolo
pushd /tiny-yolo
curl --location -o model.cfg https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov2-tiny-voc.cfg
curl --location -o model.weights https://pjreddie.com/media/files/yolov2-tiny-voc.weights
curl --location -o categories.txt https://raw.githubusercontent.com/pjreddie/darknet/master/data/voc.names
python /ELL/tools/importers/darknet/darknet_import.py model.cfg model.weights
python /ELL/tools/wrap/wrap.py model.ell --lang python --target pi3
popd
