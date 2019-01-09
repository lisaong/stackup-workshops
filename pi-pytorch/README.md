## PyTorch on RaspberryPi

The following examples demonstrate to train Deep Learning models using PyTorch and then deploy on a Raspberry Pi 3 to get predictions.

The PyTorch installation on Raspberry Pi 3 uses this docker image: [lisaong/armv71-torch-py3.6](https://hub.docker.com/r/lisaong/armv71-torch-py3.6/)

### Slides
http://bit.ly/pi-pytorch-bmt

### Workflow

1. Train model on desktop system
2. Transfer to RaspberryPi to evaluate

![img](https://github.com/lisaong/stackup-workshops/raw/master/pi-pytorch/assets/PyTorch%20with%20Raspberry%20Pi.png)

### Examples
- [Basic PyTorch training and deployment](tutorials/train/README.md)
- [RNN to generate multi-sine wave](tutorials/rnn/README.md)
- [RNN on sensor data to predict equipment failure](tutorials/sensor/README.md)

## Setup Instructions
### Desktop Setup

Reference: https://pytorch.org/get-started

#### GPU (Ubuntu or Windows)

Install Cuda 9.2:
https://developer.nvidia.com/cuda-92-download-archive

(both the Base installer and Patch 1)

```
conda create -n torch python=3.6
conda activate torch
conda install pytorch cuda92 -c pytorch
pip install torchvision

# test gpu install
python -c "import torch; print(torch.rand(5, 3).cuda())"
```

#### CPU (MacOS, Ubuntu, Windows)

```
conda create -n torch python=3.6
conda activate torch
conda install pytorch torchvision -c pytorch
```

### Raspberry Pi Setup

These steps have been tested on a Model 3B.

1. [Download and flash](https://www.raspberrypi.org/downloads/raspbian) a recent Raspbian Stretch Lite image onto a 8GB or larger micro SD card.
2. Boot up the Raspberry Pi
3. Git clone this repository
4. Bootstrap git-lfs
```
cd stackup-workshops/ai-edge/bootstrap
sh ./install_git_lfs_rpi.sh
git lfs pull
```
5. Reboot Raspberry Pi
6. Install docker
```
curl -sSL get.docker.com | sh
sudo usermod -aG docker pi

# IMPORTANT: log out, then log back in again for changes to take effect, then run the next line

sudo systemctl start docker
```
7. Launch the PyTorch docker image (lisaong/armv71-torch-py3.6)
```
cd stackup-workshops/pi-pytorch/docker
sh launch_docker.sh
```
8. From the docker image, run the following test script to load and evalute a neural network. You should see output like below (actual values will differ because of random seed).
```
root@xxxxx:/code# cd tutorials/train
root@xxxxx:/code/tutorials/train# python3 nn_eval.py

result tensor([[-1.3430,  0.3558, -1.3451,  0.6432, -0.6340, -0.1667, -0.5551,
          0.3526, -0.1512, -0.1724]])
```
