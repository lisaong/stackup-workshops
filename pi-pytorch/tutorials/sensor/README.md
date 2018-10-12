# Predicting Failures from IoT Sensor Data

This uses data from https://developer.ibm.com/patterns/predict-equipment-failure-using-iot-sensor-data/ to predict failures using a Recurrent Neural Network.

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

This will save a `checkpoint.pt` file containing the lowest loss after training.

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

RNN(
  (rnn): LSTM(9, 10, num_layers=2, batch_first=True)
  (fc): Linear(in_features=10, out_features=1, bias=True)
)
model training loss 0.23991495370864868
model training epoch 803
prediction time: 0.068s
[[ 92  15]
 [  8 112]]
             precision    recall  f1-score   support

          0       0.92      0.86      0.89       107
          1       0.88      0.93      0.91       120

avg / total       0.90      0.90      0.90       227

```
