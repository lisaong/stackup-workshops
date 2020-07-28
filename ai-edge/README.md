## AI on the Edge

### Slides
Browse the slides [here](ai-on-the-edge.ipynb)

### Demos
|Demo|Hardware|Software / Docker images|
|--|--|--|
|CoreML|OSX machine|XCode 9.3.1|
|Embedded Learning Library (Python 3)|Raspberry Pi 3 Model B|Docker image: lisaong/pi3-miniconda3-ell:2.3.3, default jupyter port: 28888|
|Keras with TensorFlow backend (Python 3)|Raspberry Pi 3 Model B|Docker image: lisaong/rpi-keras:1.0, default jupyter port: 38888|
|Movidius (Python 3)|Raspberry Pi 3 Model B, Movidius Neural Compute Stick|Docker image: lisaong/rpi-movidius:2.04, default jupyter port: 8888|
|TensorFlow (Python 2)|Raspberry Pi 3 Model B|Docker image: lisaong/rpi-docker-tensorflow:tf1.8.0, default jupyter port: 18888|
|TensorFlow 2.0, Pytorch 1.3 (Python 3.7)|Raspberry Pi 3 Model B|Docker image: lisaong/rpi-jupyter-tf2-torch-py37:1.0, default jupyter port: 48888, default tensorboard port: 46006|

#### Raspberry Pi 3 Setup

1. [Download and flash](https://www.raspberrypi.org/downloads/raspbian) a recent Raspbian Lite image onto a 16GB or larger micro SD card (last verified on Stretch). You may also wish to try a [DietPi](https://dietpi.com/) image (last verified on Buster).
2. Boot up the Raspberry Pi 3
3. Git clone this repository
4. Bootstrap git-lfs
```
cd stackup-workshops/ai-edge/bootstrap
sh ./install_git_lfs_rpi.sh
git lfs pull
```
5. Install docker
```
curl -sSL get.docker.com | sh
sudo usermod -aG docker pi

# IMPORTANT: log out, then log back in again for changes to take effect, then run the next line

sudo systemctl start docker
```
6. Launch a demo by navigating to its folder and starting the docker container
```
cd stackup-workshops/ai-edge/docker/tensorflow
./launch_docker.sh
```
If all goes well, you should see a Jupyter uri and token. Copy and paste that uri (with token) to your browser on the desktop, and replace `localhost` with the ip address of the Raspberry Pi 3.

Note that each demo is configured to run in its docker container, which has the necessary environment and tools setup. Mixing and matching containers and demos won't work.

### Rendering Presentations

For a better viewing experience, you can render the Jupyter notebook in slide presentation view (reveal.js slideshows):

1. Install [Miniconda](https://conda.io/miniconda.html)
2. Install [RISE](https://github.com/damianavila/RISE)

```
conda install -c damianavila82 rise
```

From the Jupyter notebook:

* Alt-r, "Enter/Exit Live Reveal Slideshow
* Shift-i, Toggle slide
* Shift-u, Toggle subslide
* Shift-f, Toggle fragment

[Usage](https://github.com/damianavila/RISE/blob/master/doc/usage.md)
