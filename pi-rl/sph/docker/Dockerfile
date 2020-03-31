# === Build Stage ===
FROM balenalib/raspberrypi3:buster as builder

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     build-essential \
     git

RUN apt-get install -y --no-install-recommends \
  python3-dev python3-pip python3-setuptools \
  cmake \
  swig3.0

RUN  apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# OgmaNeo2
WORKDIR /tmp
RUN git clone https://github.com/ogmacorp/OgmaNeo2.git \
  && cd OgmaNeo2 \
  && mkdir build \
  && cd build \
  && cmake .. -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=On \
  && cmake --build . \
  && cmake --build . --target install

# PyOgmaNeo2
# https://github.com/ogmacorp/PyOgmaNeo2
# (PyOgmaNeo does not support install prefixes yet)
WORKDIR /app
RUN pip3 install --no-cache-dir \
      virtualenv

RUN virtualenv . \
  && . bin/activate \
  && git clone https://github.com/ogmacorp/PyOgmaNeo2.git \
  && cd PyOgmaNeo2 \
  && python3 setup.py install

RUN . bin/activate \
  && pip3 install --no-cache-dir \
    gym

# === Production Stage ===
FROM balenalib/raspberrypi3:buster

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  git \
  python3-dev \
  python3-pip \
  python3-setuptools \
  libgomp1 \
  libatlas-base-dev \
  libfreetype6

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app /app
COPY --from=builder /usr/local/include /usr/local/include
COPY --from=builder /usr/local/lib/libOgmaNeo.so /usr/local/lib

# Install custom environments
# Use the forked version of gym-inventory with deprecation fixes
WORKDIR /tmp
RUN . /app/bin/activate \
  && pip3 --no-cache-dir install -e \
  "git+https://github.com/ivallesp/gym-inventory#egg=gym_inventory"

RUN . /app/bin/activate \
  && pip3 --no-cache-dir install \
   matplotlib \
   pandas

# Test
WORKDIR /app

RUN . bin/activate \
  && python3 -c "import pyogmaneo as test; print(test); \
  import gym_inventory; print(gym_inventory);"

WORKDIR /code
