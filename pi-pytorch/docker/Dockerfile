FROM resin/rpi-raspbian:stretch

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python3-pip python3-setuptools \
        python3-numpy python3-sklearn python3-pandas \
        libopenblas-dev

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install \
    torch-raspi

WORKDIR "/code"

# Test
RUN python3 -c "import torch; print('torch', torch.__version__); \
        import sklearn; print('sklearn', sklearn.__version__)"