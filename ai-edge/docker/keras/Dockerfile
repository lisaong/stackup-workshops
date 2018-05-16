# Jupyter: https://github.com/romilly/rpi-docker-tensorflow
# Keras: http://www.instructables.com/id/Installing-Keras-on-Raspberry-Pi-3/

FROM resin/rpi-raspbian:stretch

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        libjpeg8-dev \
        libzmq3-dev \
        pkg-config

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python-pip python3-pip python3-setuptools python3-markdown python3-pillow python3-yaml python3-pygraphviz python3-h5py python3-nose python3-lxml python3-matplotlib python3-numpy python3-protobuf python3-dateutil python3-skimage python3-scipy python3-six python3-networkx python3-tk

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install \
        ipykernel \
        jupyter \
    && python3 -m ipykernel.kernelspec

# TensorFlow
RUN curl -L -O https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.8.0/tensorflow-1.8.0-cp35-none-linux_armv7l.whl \
    && pip3 --no-cache-dir install \
            tensorflow-1.8.0-cp35-none-linux_armv7l.whl

# Keras
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libatlas-base-dev
RUN pip3 --no-cache-dir install \
    keras

# Jupyter
COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /
RUN chmod 777 /run_jupyter.sh

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

WORKDIR "/notebooks"

CMD ["/run_jupyter.sh", "--allow-root"]
