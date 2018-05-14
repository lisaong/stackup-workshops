#!/usr/bin/env bash

# Chalta
mkdir -p /models/object-classifier
pushd /models/object-classifier
curl --location -o categories.txt https://github.com/Microsoft/ELL-models/raw/master/models/ILSVRC2012/categories.txt
curl --location -o model.ell.zip https://github.com/Microsoft/ELL-models/raw/master/models/ILSVRC2012/Chalta/Chalta.ell.zip
unzip model.ell.zip
mv Chalta.ell model.ell
python /ELL/tools/wrap/wrap.py model.ell --language python --target pi3
popd