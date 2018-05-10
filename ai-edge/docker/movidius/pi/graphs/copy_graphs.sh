#!/usr/bin/env bash
mkdir -p caffe
sudo docker cp $1:/home/movidius/ncappzoo/caffe/SSD_MobileNet caffe/SSD_MobileNet
sudo docker cp $1:/home/movidius/ncappzoo/caffe/SqueezeNet caffe/SqueezeNet

mkdir -p tensorflow
sudo docker cp $1:/home/movidius/ncappzoo/tensorflow/mobilenets/model tensorflow/mobilenets
