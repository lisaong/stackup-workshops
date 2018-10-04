## Pytorch on RaspberryPi

Workflow

1. Train model on desktop system
2. Transfer to RaspberryPi to evaluate

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

