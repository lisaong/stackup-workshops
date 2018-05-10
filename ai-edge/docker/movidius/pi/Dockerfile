# Jupyter: https://github.com/romilly/rpi-docker-tensorflow
# Movidius: https://movidius.github.io/blog/ncs-apps-on-rpi/

FROM resin/rpi-raspbian:stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libusb-1.0-0-dev libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler libatlas-base-dev git automake byacc lsb-release cmake libgflags-dev libgoogle-glog-dev liblmdb-dev swig3.0 graphviz libxslt-dev libxml2-dev gfortran udev

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev python-pip python3-pip python3-setuptools python3-markdown python3-pillow python3-yaml python3-pygraphviz python3-h5py python3-nose python3-lxml python3-matplotlib python3-numpy python3-protobuf python3-dateutil python3-skimage python3-scipy python3-six python3-networkx python3-tk

RUN  apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install \
        ipykernel \
        jupyter && \
    python3 -m ipykernel.kernelspec

RUN git clone https://github.com/movidius/ncsdk
WORKDIR /ncsdk/api/src
RUN make && \
    make basicinstall pythoninstall && \
    ldconfig

WORKDIR /
RUN git clone https://github.com/movidius/ncappzoo

# Pre-converted Movidius graphs
COPY graphs/caffe/SSD_MobileNet/ /ncappzoo/caffe/SSD_MobileNet/
COPY test_movidius.py /root/

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
