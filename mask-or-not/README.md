# Mask or No-mask?

[![Mask or Not CI](https://github.com/lisaong/stackup-workshops/workflows/Mask%20or%20Not%20CI/badge.svg)](https://github.com/lisaong/stackup-workshops/actions?query=workflow%3A%22Mask+or+Not+CI%22)

## Introduction
This workshop demonstrates how to train an image classifier using Tensorflow-Keras, convert it to Tensorflow Lite, and how to port it using EloquentTinyML to run on an ESP32 platform.

ESP32 is a popular platform for IoT projects, and comes in many variants. I used DevKitC V4, which includes 4MB flash.

## Instructions
1. Go to `Documents\Arduino\libraries`

   a. Create the subfolder `mask_or_not`, copy the contents of the `model` directory to it. Just copy the *.h, don't copy the models directory.

   b. git clone https://github.com/eloquentarduino/EloquentTinyML
  
2. Start Arduino IDE
3. Open the sketch file: `run_model.ino`
4. Connect an ESP32 to USB, select the COM port to connect to it
5. Upload the sketch to the ESP32
6. Once upload is complete, open Serial Monitor to monitor serial output
  
   a. If you observe `nan`, reset the ESP32 to see if `AllocateTensors` has failed. If so, you may need to increase `TENSOR_ARENA_SIZE`.

   b. If the ESP32 goes into a reboot loop, the PCA input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).
  
   c. If you get a linker error (dangerous relocation), the PCA input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).

Sample output from Serial Monitor (using random data):
```
predicted: 0.46
-0.39,-0.06,0.61,-0.76,0.13,0.08,0.02,-0.26,-0.09,0.13,-0.74,-0.50,-0.98,0.60,-0.19,0.13,0.94,-0.75,-0.74,-0.22,-0.95,-0.17,0.83,-0.54,-0.44,-0.64,0.54,0.05,0.57,0.47,-0.95,0.48,0.42,0.69,-0.43,0.61,-0.09,0.18,0.54,-0.91,0.14,0.91,-0.89,0.76,-0.49,-0.16,-0.02,-0.65,0.37,-0.86,-0.75,0.80,-0.44,-0.32,-0.04,0.57,-0.91,0.98,0.02,-0.87,-0.39,0.92,-0.71,0.39,0.84,-0.43,-0.43,0.24,0.44,0.06,0.12,0.79,-0.68,-0.61,0.83,0.05,-0.67,0.06,-0.90,-0.35,-0.64,-0.28,-0.72,-0.08,0.82,0.52,0.83,0.28,-0.87,0.65,-0.39,0.11,-0.69,0.08,-0.60,0.80,0.83,0.61,0.22,0.52,
predicting...
predicted: 0.47
0.72,0.34,0.18,0.00,-0.31,0.84,0.75,0.31,-0.47,-0.82,0.08,0.21,0.94,0.17,-0.36,0.98,-0.08,-0.33,0.19,0.07,0.72,-0.91,-0.06,0.27,-0.61,-0.86,0.72,-0.64,0.41,-0.49,0.07,-0.65,-0.26,-0.91,0.08,0.31,0.10,0.94,0.23,0.46,0.72,0.70,-0.83,0.17,0.65,-0.06,0.66,-0.43,0.45,-0.21,0.39,-0.69,-0.98,0.43,-0.39,0.80,0.31,-0.62,-0.80,-0.69,0.43,0.06,-0.28,0.40,-0.16,0.55,0.71,0.08,-0.82,-0.17,0.39,0.65,0.03,0.24,-0.28,-0.89,-0.83,0.07,-0.81,-0.56,0.45,-0.51,0.28,-0.06,-0.21,0.94,-0.04,0.23,-0.37,0.93,-1.00,-0.20,0.43,-0.65,0.87,0.96,0.81,-0.02,0.79,0.38,
predicting...
predicted: 0.48
```

View the [Colab Notebook](mask_or_not.ipynb).
