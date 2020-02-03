# https://registry.hub.docker.com/r/balenalib/raspberrypi3-alpine-python
# https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
FROM balenalib/raspberrypi3-alpine-python:3-latest-run as base
FROM base as builder

RUN mkdir /install
WORKDIR /install

# alpine package manager
RUN apk add --no-cache gcc musl-dev

RUN curl -L -O https://github.com/al45tair/netifaces/archive/release_0_10_9.tar.gz \
    && tar zxvf release_0_10_9.tar.gz \
    && rm release_0_10_9.tar.gz \
    && cd netifaces-release_0_10_9 \
    && python setup.py install

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir --install-option="--prefix=/install" \
    -r /tmp/requirements.txt

# multi-stage build
FROM base

COPY --from=builder /install /usr/local
COPY . /app

WORKDIR /app

CMD ["python", "publish.py", "wlan0", "iot.eclipse.org"]
