# Mask or No-mask?

[![Mask or Not CI](https://github.com/lisaong/stackup-workshops/workflows/Mask%20or%20Not%20CI/badge.svg)](https://github.com/lisaong/stackup-workshops/actions?query=workflow%3A%22Mask+or+Not+CI%22)

![title](mask_no_mask.jpg)

## Introduction
This workshop demonstrates how to train an image classifier using Tensorflow-Keras, convert it to Tensorflow Lite, and how to port it using EloquentTinyML to run on an ESP32 platform.

ESP32 is a popular platform for IoT projects, and comes in many variants. I used DevKitC V4, which includes 4MB flash.

## Model Architecture

This uses a Depthwise Separable Convolutional Neural Network classifier to output a binary "mask" or "no mask" prediction. Images are downsampled to 10x10 pixels.

A Depthwise Separable Convolutional Layer cuts down the amount of Multiply-Add operations, compared to a Convolutional Layer, at the expense of fewer weights (lower model complexity, more tendency to underfit).

![arch](separable_cnn.png)

Metrics on Train and Test Data:
```
Testing TFLite Model
              precision    recall  f1-score   support

           0       0.90      0.90      0.90        10
           1       0.90      0.90      0.90        10

    accuracy                           0.90        20
   macro avg       0.90      0.90      0.90        20
weighted avg       0.90      0.90      0.90        20
```

Metrics on Test Data alone shows that this model will need to be further tuned:
```
              precision    recall  f1-score   support

           0       0.67      0.67      0.67         3
           1       0.50      0.50      0.50         2

    accuracy                           0.60         5
   macro avg       0.58      0.58      0.58         5
weighted avg       0.60      0.60      0.60         5
```

The code to run this model on the ESP32 is [run_model_cnn.ino](run_model_cnn.ino).

However, it is much better than an MLP, which requires dimensionality reduction to 7 dimensions (using PCA) before it can reliably run on the ESP32 (See [run_model_pca_mlp.ino](run_model_pca_mlp.ino)):
```
              precision    recall  f1-score   support

           0       0.50      0.67      0.57         3
           1       0.00      0.00      0.00         2

    accuracy                           0.40         5
   macro avg       0.25      0.33      0.29         5
weighted avg       0.30      0.40      0.34         5
```
The training and conversion process is covered in the Colab notebook linked below.

## Instructions
1. Install the latest Ardiuno IDE. You will also need an ESP32 board, and [configure Arduino IDE to program an ESP32](https://embedgyan.wordpress.com/2020/06/22/installing-the-esp32-board-in-arduino-ide-windows-mac-os-x-linux/).
2. Go to `Documents\Arduino\libraries`

   a. Create a subfolder `mask_or_not`, copy [models/10/cnn_10.h](models/10/cnn_10.h) to it. Just copy the file, don't copy the models folder or subfolders (else Arduino IDE cannot find the file during compilation).

   b. Git clone https://github.com/eloquentarduino/EloquentTinyML into the `Documents/Arduino/libraries` folder. This should create a subfolder called `Documents/Arduino/libraries/EloquentTinyML`

   c. Clone the latest Arduino-ESP32 library from Espressif master, to enable the BluetoothSerial data callback. Instructions are [here](https://github.com/espressif/arduino-esp32).
   ```
    mkdir -p ~/Documents/Arduino/hardware/espressif && \
    cd ~/Documents/Arduino/hardware/espressif && \
    git clone https://github.com/espressif/arduino-esp32.git esp32 && \
    cd esp32 && \
    git submodule update --init --recursive && \
    cd tools && \
    python get.py 
   ```
  
3. Start Arduino IDE. Go to Boards Manager, select `ESP32 Arduino (in sketchbook)`. This will reference the updated libraries.
4. Open the sketch file: [run_model_cnn.ino](run_model_cnn.ino).
5. Connect an ESP32 to USB, select the COM port to connect to it
6. Upload the sketch to the ESP32
7. Once upload is complete, open Serial Monitor to monitor serial output
  
   a. If you observe `nan`, reset the ESP32 to see if `AllocateTensors` has failed. If so, you may need to increase `TENSOR_ARENA_SIZE`.

   b. If the ESP32 goes into a reboot loop, the input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).
  
   c. If you get a linker error (dangerous relocation), the input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).

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

## Colab Notebook
View the [Colab Notebook](mask_or_not.ipynb).

## Continuous Integration
This project also features continuous integration of the Jupyter notebook:
1. The Jupyter notebook is setup to serialise the model specs in ci_artifacts.pkl. Model specs include inputs, target, pre-processors, and pointers to the saved weights.
2. During continuous integration, this [Github workflow](../.github/workflows/maskornot.yml) will execute the Jupyter notebook in a Docker container. This trains the models and saves their weights, preprocessors, and data.
3. The workflow will run this [integration test](ci_test.py) to load the model weights, preprocessors, and data to get predictions and metrics.

Example the schema used to organise the artifacts:
```
ci_artifacts = {
    'inputs' : {
        'X' : X,
        'X_cnn' : X_scaled_reshape
    },

    'target' : {
        'y' : y,
        'encoder' : le
    },

    'preprocessors' : {
      'scaler' : scaler,
      'pca' : pca
    },

    'baseline' : {
        'input' : 'X',
        'model' : lr,
        'preprocessors' : [
          'scaler',
          'pca'
        ],
    },

    # model1 spec
    'mlp' : {
        'input' : 'X',
        'scaler' : scaler,
        'preprocessors' : [
          'scaler',
          'pca'                 
        ],
        'h5' : 'mlp.h5'
    },

    # model2 spec
    'cnn' : {
        'input' : 'X_cnn',
        'preprocessors' : [
        ],
        'h5' : 'cnn.h5',
        'tflite' : 'cnn.tflite',
        'h' : 'cnn.h' 
    }
}
```
