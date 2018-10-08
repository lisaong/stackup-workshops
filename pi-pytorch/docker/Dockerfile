FROM resin/rpi-raspbian:stretch

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python3-pip python3-setuptools python3-numpy \
        libopenblas-dev

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install \
    torch-raspi

# Test
RUN python3 -c "import torch; print(torch.__version__)"