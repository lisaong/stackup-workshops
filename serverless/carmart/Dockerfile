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

ENV SLACK_WEBHOOK_URL ''
ENV CARMART_QUERIES mx-5;brz;suzuki+swift
ENV S3_BUCKET_NAME carmart

# Allow specification of access keys from Lambda (consumed by boto3).
# TODO: Unlike EC2, Lambdas don't seem to support instance metadata retrieval for credentials...
ENV AWS_ACCESS_KEY_ID ''
ENV AWS_SECRET_ACCESS_KEY ''

WORKDIR /app
CMD bash -c "source bin/activate && python monitor.py"
