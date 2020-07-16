# Mask or No-mask?

[![Mask or Not CI](https://github.com/lisaong/stackup-workshops/workflows/Mask%20or%20Not%20CI/badge.svg)](https://github.com/lisaong/stackup-workshops/actions?query=workflow%3A%22Mask+or+Not+CI%22)

## Introduction
TBA

## Instructions
1. Go to `Documents\Arduino\libraries`
  a. Create the subfolder `mask_or_not`, copy `mlp_*.h` to it
  b. git clone https://github.com/eloquentarduino/EloquentTinyML
2. Start Arduino IDE
3. Open the sketch file: `run_model.ino`
  a. Update the `NUMBER_OF_INPUTS` to match the model size. For example `mlp_10.h` will use 10 inputs, `mlp_5.h` will use 5 inputs.
  b. You may need to also tweak `TENSOR_ARENA_SIZE` if `AllocateTensors` fail. 
4. Connect an ESP32 to USB, select the COM port to connect to it
5. Upload the sketch to the ESP32
6. Once upload is complete, open Serial Monitor to monitor serial output
  a. If you observe `nan`, reset the ESP32 to see if `AllocateTensors` has failed.

View the [Colab Notebook](mask_or_not.ipynb).