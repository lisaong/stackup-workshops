#!/usr/bin/env bash
docker run -it \
  -v $PWD:/build \
  lisaong/onnx-mlir:1.0 \
  bash

