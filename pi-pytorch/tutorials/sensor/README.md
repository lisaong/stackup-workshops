# Predicting Failures from IoT Sensor Data

This uses data from(https://developer.ibm.com/patterns/predict-equipment-failure-using-iot-sensor-data/) to predict failures using a Recurrent Neural Network.

## Train on Desktop

From our Anaconda environment:

1. Install pre-requisites
```
(torch) conda install pandas scikit-learn
```

2. Train the RNN
```
(torch) python train.py
```

This will save a `checkpoint.pt` file containing the lowest loss after 100 epochs.

### TensorBoard
You can view training progress via TensorBoard:

```
(torch) cd tutorials/sensor
(torch) tensorboard --logdir=logs --host=0.0.0.0
```
![tensorboard](tensorboard.png)

## Evaluate on Raspberry Pi

1. [Optional] Copy the `checkpoint.pt` file to the tutorials/sensor folder on the Raspberry Pi if you have re-trained it.
2. Launch the Raspberry Pi PyTorch docker image.
```
cd ~/stackup-workshops/pi-pytorch/docker
sh launch_docker.sh
```

3. From the docker image, evaluate the RNN on test data. You should see output like below (actual values will differ because of random seed).
```
root@xxxxx:/code# cd /tutorials/sensor
root@xxxxx:/code/tutorials/sensor# python3 eval.py
```
