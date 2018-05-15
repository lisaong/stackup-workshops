#!/usr/bin/env bash

# Script to run in debian docker instance to import speech commands models
# Ref: https://microsoft.github.io/ELL/tutorials/Getting-started-with-audio-keyword-classification-on-the-Raspberry-Pi/
#
# docker image to use: lisaong/debian-miniconda3-ell:2.3.3

# Featurizer and Classifier models
mkdir -p /models/speech-cmds
pushd /models/speech-cmds
curl --location -o featurizer_16k.ell.zip https://github.com/Microsoft/ELL-models/raw/master/models/speech_commands_v0.01/Cinnamon/f_16000_512_160_mel_40_40_log.zip
curl --location -o classifier_16k.ell.zip https://github.com/Microsoft/ELL-models/raw/master/models/speech_commands_v0.01/Cinnamon/gru_f_16000_512_160_mel_40_40_log.zip
curl --location -o categories.txt https://github.com/Microsoft/ELL-models/raw/master/models/speech_commands_v0.01/categories.txt

unzip featurizer_16k.ell.zip
unzip classifier_16k.ell.zip
mv f_16000_512_160_mel_40_40_log.ell featurizer_16k.ell
mv gru_f_16000_512_160_mel_40_40_log.ell classifier_16k.ell

# TEMP: replace with local versions of the model until ELL-models is updated
cp /tmp/models/speech-cmds/f_16000_512_160_mel_40_40_log.ell featurizer_16k.ell
cp /tmp/models/speech-cmds/gru_f_16000_512_160_mel_40_40_log.ell classifier_16k.ell

python /ELL/tools/wrap/wrap.py featurizer_16k.ell --target pi3 --outdir featurizer_16k --module_name mfcc
python /ELL/tools/wrap/wrap.py classifier_16k.ell --target pi3 --outdir classifier_16k --module_name model
popd
