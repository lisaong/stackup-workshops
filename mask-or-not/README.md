# Mask or No-mask?

[![Mask or Not CI](https://github.com/lisaong/stackup-workshops/workflows/Mask%20or%20Not%20CI/badge.svg)](https://github.com/lisaong/stackup-workshops/actions?query=workflow%3A%22Mask+or+Not+CI%22)

## Introduction
TBA

## Instructions
1. Go to `Documents\Arduino\libraries`

   a. Create the subfolder `mask_or_not`, copy `*.h` to it

   b. git clone https://github.com/eloquentarduino/EloquentTinyML
  
2. Start Arduino IDE
3. Open the sketch file: `run_model.ino`
4. Connect an ESP32 to USB, select the COM port to connect to it
5. Upload the sketch to the ESP32
6. Once upload is complete, open Serial Monitor to monitor serial output
  
   a. If you observe `nan`, reset the ESP32 to see if `AllocateTensors` has failed. If so, you may need to increase `TENSOR_ARENA_SIZE`.

   b. If the ESP32 goes into a reboot loop, the PCA input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).
  
   c. If you get a linker error (dangerous relocation), the PCA input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).

View the [Colab Notebook](mask_or_not.ipynb).
