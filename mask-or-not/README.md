# Mask or No-mask?

[![Mask or Not CI](https://github.com/lisaong/stackup-workshops/workflows/Mask%20or%20Not%20CI/badge.svg)](https://github.com/lisaong/stackup-workshops/actions?query=workflow%3A%22Mask+or+Not+CI%22)

![title](assets/mask_no_mask.jpg)

## Introduction
This workshop demonstrates how to train an image classifier using Tensorflow-Keras, convert it to Tensorflow Lite, and how to port it using EloquentTinyML to run on an ESP32 platform.

ESP32 is a popular platform for IoT projects because it supports Bluetooth Classic, Bluetooth LE, WiFi, and can be programmed using the Arduino IDE. ESP32 comes in many variants. I used DevKitC V4, which includes 4MB flash.

## Colab Notebook
View the [Colab Notebook](mask_or_not.ipynb).

## Model Architecture

This uses a [Depthwise Separable Convolutional](https://towardsdatascience.com/a-basic-introduction-to-separable-convolutions-b99ec3102728) Neural Network classifier to output a binary "mask" or "no mask" prediction. Images are downsampled to 10x10 pixels.

A Depthwise Separable Convolutional Layer cuts down the amount of Multiply-Add operations, compared to a Convolutional Layer, at the expense of lower complexity.

|Counts|Standard Convolution|Depthwise Separable Convolution|
|--|--|--|
|# Multiply-Adds|kernel_size x output_size x depth x channels + depth|(kernel_size x output_size + depth) x channels + depth + channels|
|# Weights|(kernel_size x depth x channels) + depth|(kernel_size + depth + 1) x channels + depth|
|Summary|More accurate, higher memory and execution overhead|Less accurate, but lower memory and execution overhead|

![arch](assets/separable_cnn.png)

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

### Comparison to MLP
Even though the Depthwise CNN is underfitting, it is better in terms of accuracy and F1-score than an MLP. An MLP requires dimensionality reduction to 7 dimensions (using PCA) before it can reliably run on the ESP32 (See [run_model_pca_mlp.ino](run_model_pca_mlp.ino)).

We are faced with 2 constraints on the ESP32 when applying an MLP:
- Data size of PCA coefficients: 400 x 7
- Constructing an MLP of sufficient complexity

Metrics on Train and Test Data (MLP):
```
              precision    recall  f1-score   support

           0       0.70      0.70      0.70        10
           1       0.70      0.70      0.70        10

    accuracy                           0.70        20
   macro avg       0.70      0.70      0.70        20
weighted avg       0.70      0.70      0.70        20
```

Metrics on Test Data (MLP):
```
              precision    recall  f1-score   support

           0       0.50      0.67      0.57         3
           1       0.00      0.00      0.00         2

    accuracy                           0.40         5
   macro avg       0.25      0.33      0.29         5
weighted avg       0.30      0.40      0.34         5
```
The training and quantization process is covered in this [Colab notebook](mask_or_not.ipynb).

## Instructions (MacOS or Linux)

Note: At this time, Windows 10 does not support connecting to the Bluetooth Serial Virtual COM port. These instructions have been verified on MacOS, and should also work for Linux.

1. Install the latest Ardiuno IDE. You will also need an ESP32 board, and [configure Arduino IDE to program an ESP32](https://embedgyan.wordpress.com/2020/06/22/installing-the-esp32-board-in-arduino-ide-windows-mac-os-x-linux/).
2. Go to `Documents\Arduino\libraries`.

   a. Create a subfolder `mask_or_not`, copy [models/10/cnn_10.h](models/10/cnn_10.h) to it. Just copy the file, don't copy the models folder or subfolders (else Arduino IDE cannot find the file during compilation).

   b. Git clone https://github.com/eloquentarduino/EloquentTinyML into the `Documents/Arduino/libraries` folder. This should create a subfolder called `Documents/Arduino/libraries/EloquentTinyML`.

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
   
   d. [Optional] Connect a TM1637 4-digit display, such as one from [Seed Studio](https://wiki.seeedstudio.com/Grove-4-Digit_Display/) or [SgBotic](https://www.sgbotic.com/index.php?dispatch=products.view&product_id=2488), and install the corresponding Arduino library.

   Example pinout:
   |TM1637|ESP32|
   |--|--|
   |5V or 3.3V|5V or 3.3V|
   |GND|GND|
   |DIO|GPIO 23|
   |CLK|GPIO 22|

   ![wiring1](assets/wiring1.png)
   ![wiring2](assets/wiring2.png)

3. Start Arduino IDE. Go to Boards Manager, select `ESP32 Arduino (in sketchbook)`. This will reference the updated libraries.
4. Open the sketch file: [run_model_cnn.ino](run_model_cnn.ino).
5. Connect an ESP32 to USB, select the COM port to connect to it.
6. Upload the sketch to the ESP32.
7. Once upload is complete, open Serial Monitor to monitor serial output.
  
   a. If you observe `nan`, reset the ESP32 to see if `AllocateTensors` has failed. If so, you may need to increase `TENSOR_ARENA_SIZE`.

   b. If the ESP32 goes into a reboot loop, the input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).
  
   c. If you get a linker error (dangerous relocation), the input dimensions are too big. Try a smaller image dimension (`OUTPUT_SIZE` in the Colab Notebook).
8. Pair with the ESP32 device over Bluetooth.
9. Check the serial port connection using `ls /dev/cu*`. Update `send_image.py` to use the connection string (set in `PORT`) if different.
10. Run the python script to send a test image to the device, after installing dependencies.
    ```
    pip install -r requirements.txt
    python send_image.py
    ```

Sample output from Serial Monitor (using a 10x10 test image sent over Bluetooth SPP):
```
[V][BluetoothSerial.cpp:275] esp_spp_cb(): ESP_SPP_DATA_IND_EVT len=100 handle=385
onDataCallback(0x3ffe3900, 100)53,60,168,182,180,161,60,30,197,211,12,119,178,204,192,187,173,131,203,211,74,175,165,200,193,187,172,177,204,211,147,174,111,52,116,180,97,141,213,211,141,178,89,157,175,184,157,175,210,211,139,176,187,173,176,185,160,192,214,211,126,167,170,186,144,167,176,177,195,212,113,162,161,182,169,175,160,165,219,212,154,146,163,159,157,165,149,160,213,213,219,114,150,168,186,180,184,153,219,215,
predicting...
prediction: 0.61
[I][BluetoothSerial.cpp:247] esp_spp_cb(): ESP_SPP_CLOSE_EVT
[I][BluetoothSerial.cpp:235] esp_spp_cb(): ESP_SPP_SRV_OPEN_EVT
Client Connected
[V][BluetoothSerial.cpp:275] esp_spp_cb(): ESP_SPP_DATA_IND_EVT len=100 handle=129
onDataCallback(0x3ffe3a0c, 100)53,60,168,182,180,161,60,30,197,211,12,119,178,204,192,187,173,131,203,211,74,175,165,200,193,187,172,177,204,211,147,174,111,52,116,180,97,141,213,211,141,178,89,157,175,184,157,175,210,211,139,176,187,173,176,185,160,192,214,211,126,167,170,186,144,167,176,177,195,212,113,162,161,182,169,175,160,165,219,212,154,146,163,159,157,165,149,160,213,213,219,114,150,168,186,180,184,153,219,215,
predicting...
prediction: 0.61
```

## Continuous Integration
This project also features continuous integration of the Jupyter notebook:
1. The Jupyter notebook is setup to serialise the model specs in ci_artifacts.pkl. Model specs include inputs, target, pre-processors, and pointers to the saved weights.
2. During continuous integration, this [Github workflow](../.github/workflows/maskornot.yml) will execute the Jupyter notebook in a Docker container. This trains the models and saves their weights, preprocessors, and data.
3. The workflow will run this [integration test](ci_test.py) to load the model weights, preprocessors, and data to get predictions and metrics.

Example schema used to organise the model artifacts:
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
