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
  && mkdir build /app \
  && cd build \
  && cmake .. -DCMAKE_INSTALL_PREFIX=/app -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=On \
  && cmake --build . \
  && cmake --build . --target install

# PyOgmaNeo2
# https://github.com/ogmacorp/PyOgmaNeo2
WORKDIR /app
RUN pip3 install --no-cache-dir \
      virtualenv

RUN virtualenv . \
  && . bin/activate \
  && git clone https://github.com/ogmacorp/PyOgmaNeo2.git \
  && cd PyOgmaNeo2 \
  && CMAKE_PREFIX_PATH=/app python3 setup.py install --user

# === Production Stage ===
FROM balenalib/raspberrypi3:buster
COPY --from=builder /app /app

# Test
RUN . bin activate \
  && python3 -c "import pyogmaneo as test; print(test.__version__);"

WORKDIR "/code"
