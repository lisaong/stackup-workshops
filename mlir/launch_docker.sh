#!/usr/bin/env bash
docker run -it \
  -m=6g \
  -v $PWD:/build \
  lisaong/onnx-mlir:1.0 \
  bash

