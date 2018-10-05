FROM resin/rpi-raspbian:stretch

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python-pip python3-pip python3-setuptools

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*
