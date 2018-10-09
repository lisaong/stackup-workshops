# Simple Recurrent Neural Network

This is a 2-layer LSTM that generates the output of a noisy multi-sine wave (e.g. two sine waves superimposed).
It uses [teacher-forcing](https://machinelearningmastery.com/teacher-forcing-for-recurrent-neural-networks/) to speed up convergence. 

Based on https://gist.github.com/spro/ef26915065225df65c1187562eca7ec4

## Train on Desktop

From our Anaconda environment:

```
(pytorch) python train.py
```

This will train for 100 epochs and save a `checkpoint.pt` file on the smallest mean epoch loss.

### TensorBoard
You can view training progress via TensorBoard:

```
(pytorch) cd tutorials/rnn
(pytorch) tensorboard --logdir=logs --host=0.0.0.0
```

![tensorboard](tensorboard.png)

## Evaluate on Raspberry Pi

1. [Optional] Copy the `checkpoint.pt` file to the tutorials/rnn folder on the Raspberry Pi if you have re-trained it.
2. Launch the Raspberry Pi PyTorch docker image and evaluate the RNN by running `eval.py` from the `/code/tutorials/rnn` folder.

```
cd ~/stackup-workshops/pi-pytorch/docker
sh launch_docker.sh

root@xxxxxx:/code# cd tutorials/rnn
root@xxxxxx:/code/tutorials/rnn# python3 eval.py
SimpleRNN(
  (input): Linear(in_features=1, out_features=50, bias=True)
  (rnn): LSTM(50, 50, num_layers=2, dropout=0.05)
  (output): Linear(in_features=50, out_features=1, bias=True)
)
generated output tensor([-0.3185, -0.5966, -0.7345, -0.7951, -0.7835, -0.7544, -0.6609,
        -0.5441, -0.4247, -0.2759, -0.0955,  0.0688,  0.2215,  0.3388,
         0.4313,  0.5148,  0.5906,  0.6461,  0.6726,  0.6893,  0.7050,
         0.7137,  0.6957,  0.6666,  0.6322,  0.5683,  0.4736,  0.3679,
         0.2587,  0.1614,  0.0381, -0.0512, -0.1216, -0.1707, -0.1941,
        -0.1872, -0.1695, -0.1538, -0.1564, -0.1149, -0.0568,  0.0024,
         0.0581,  0.0836,  0.1293,  0.1356,  0.1342,  0.1474,  0.1452])

```