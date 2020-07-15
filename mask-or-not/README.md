# Mask or No-mask?

[![Mask or Not CI](https://github.com/lisaong/stackup-workshops/workflows/Mask%20or%20Not%20CI/badge.svg)](https://github.com/lisaong/stackup-workshops/actions?query=workflow%3A%22Mask+or+Not+CI%22)

## Introduction
TBA

## Instructions
1. Create this folder `Documents\Arduino\libraries\mask_or_not`, copy `mlp_full.h` to it
2. Start Arduino IDE
3. From Library Manager, add the "Eloquent TinyML" library. Refer to this [link](https://eloquentarduino.github.io/2020/01/easy-tinyml-on-esp32-and-arduino/) for details.
4. Open the sketch file: `run_model.ino`
5. Connect an ESP32 to USB, select the COM port to connect to it
6. Upload the sketch to the ESP32
7. Once upload is complete, open Serial Monitor to monitor serial output

View the [Colab Notebook](mask_or_not.ipynb).