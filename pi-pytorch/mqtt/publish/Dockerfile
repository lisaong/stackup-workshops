# https://registry.hub.docker.com/r/balenalib/raspberrypi3-alpine-python
FROM balenalib/raspberrypi3-alpine-python:3-latest-run

WORKDIR /app

COPY . .

RUN pip3 --no-cache-dir install \
    paho-mqtt

CMD ["python", "publish.py", "iot.eclipse.org"]
