# Jupyter: https://github.com/romilly/rpi-docker-tensorflow
# Ref: https://hub.docker.com/r/paledger/rpi-tensorflow/
# Ref: https://hub.docker.com/r/continuumio/miniconda3/~/dockerfile/

FROM resin/rpi-raspbian:stretch

ENV PATH /opt/conda/bin:$PATH

RUN apt-get update \
    && apt-get install -y \
      build-essential \
      cmake \
      curl \
      gcc \
      git \
      wget \
      bzip2 \
      ca-certificates \
      libopenblas-dev

# OpenCV
RUN apt-get update \
    && apt-get install -y \
      libavcodec-dev \
      libavformat-dev \
      libdc1394-22 \
      libfreetype6-dev \
      libgtk-3-0 \
      libharfbuzz-dev \
      libjasper-dev \
      libswscale-dev

RUN apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

# Miniconda
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh -O ~/miniconda.sh \
    && bash ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh

# OpenCV
RUN conda install -c microsoft-ell/label/stretch opencv
RUN echo /opt/vc/lib > /etc/ld.so.conf.d/pi_vc_core.conf \
    && ldconfig

# Jupyter
RUN /bin/bash -c "source activate root" \
    && pip install --upgrade pip \
    && pip install --no-cache-dir --ignore-installed \
          ipykernel \
          jupyter \
    && python -m ipykernel.kernelspec

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

# tini
ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-armhf /usr/bin/tini
RUN chmod +x /usr/bin/tini

# ELL models
ADD https://raw.githubusercontent.com/Microsoft/ELL/master/docs/tutorials/shared/tutorial_helpers.py /

# Tiny Yolo (too memory intensive on a Pi3)
# COPY models/tiny-yolo/ /tiny-yolo
# WORKDIR /tiny-yolo/pi3
# RUN mkdir -p build \
#    && cd build \
#    && cmake -DCMAKE_BUILD_TYPE=Release .. \
#    && make

# Speech Commands
COPY models/speech_cmds/ /speech_cmds
WORKDIR /speech_cmds/pi3
RUN mkdir -p build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. \
    && make

WORKDIR "/notebooks"
ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD ["/run_jupyter.sh", "--allow-root"]
