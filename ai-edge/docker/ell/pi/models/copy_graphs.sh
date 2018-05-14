#!/usr/bin/env bash
pushd ..
docker cp $1:/models .
chown -R $USER:$USER models
popd
