# https://hub.docker.com/r/bitnami/python/
# https://github.com/bitnami/bitnami-docker-python/tree/3.8.1-ol-7-r48-prod/example

# Build stage
from bitnami/python:3 as builder

COPY . /app
WORKDIR /app

RUN virtualenv . && \
    . bin/activate && \
    pip3 install --no-cache-dir -r requirements.txt

# Production stage
FROM bitnami/python:3-prod
COPY --from=builder /app /app
WORKDIR /app
CMD bash -c "source bin/activate && python monitor.py"


     
