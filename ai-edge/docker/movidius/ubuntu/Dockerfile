# Credits: https://github.com/ichbinblau/ncsdk_container

FROM ubuntu:16.04
ARG http_proxy

ARG https_proxy

ENV http_proxy ${http_proxy}

ENV https_proxy ${https_proxy}

RUN echo $https_proxy

RUN echo $http_proxy

ARG USERNAME=movidius
ARG WORKSPACE=/home/$USERNAME

# Uncomment the two lines below if you wish to use an Ubuntu mirror repository
# that is closer to you (and hence faster). The 'sources.list' file inside the
# 'tools/docker/' folder is set to use one of Ubuntu's official mirror in Taiwan.
# You should update this file based on your own location. For a list of official
# Ubuntu mirror repositories, check out: https://launchpad.net/ubuntu/+archivemirrors
#COPY sources.list /etc/apt
#RUN rm /var/lib/apt/lists/* -vf

RUN apt-get update \
    && apt-get upgrade \
    && apt-get install -y \
      build-essential \
      git \
      sudo \
      udev \
      usbutils \
      wget \
    && apt-get clean all

RUN apt-get update \
    && apt-get install -y \
      lsb-release \
    && apt-get clean all

RUN useradd -c "Movidius User" -m $USERNAME
COPY 10-installer /etc/sudoers.d/
RUN mkdir -p /etc/udev/rules.d/
USER $USERNAME

# NC SDK
WORKDIR $WORKSPACE
RUN git clone https://github.com/movidius/ncsdk.git
WORKDIR $WORKSPACE/ncsdk
RUN make install
RUN make examples

# NC App Zoo
WORKDIR $WORKSPACE
RUN git clone https://github.com/movidius/ncappzoo.git

# Download, export, freeze and profile model
# https://github.com/movidius/ncappzoo/blob/master/tensorflow/mobilenets/README.md
WORKDIR $WORKSPACE
RUN git clone https://github.com/tensorflow/tensorflow.git
RUN git clone https://github.com/tensorflow/models.git

WORKDIR $WORKSPACE/ncappzoo/tensorflow/mobilenets/
ENV TF_SRC_PATH $WORKSPACE/tensorflow
ENV TF_MODELS_PATH $WORKSPACE/models
RUN make

WORKDIR $WORKSPACE/ncappzoo/apps/ssd-object-detector/
RUN make
