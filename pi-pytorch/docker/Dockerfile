FROM resin/rpi-raspbian:stretch

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python-pip python3-pip python3-setuptools python3-markdown python3-pillow python3-yaml python3-pygraphviz python3-h5py python3-nose python3-lxml python3-matplotlib python3-numpy python3-protobuf python3-dateutil python3-skimage python3-scipy python3-six python3-networkx python3-tk

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*
