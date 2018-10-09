# PyTorch Deployment on Raspberry Pi 

This adapts the [60 Minute Blitz PyTorch tutorial](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html) with deployment to Raspberry Pi.

## Train on Desktop

From our Anaconda environment:

```
(pytorch) python nn_tutorial.py
```

This will save a `nn_checkpoint.pt` file containing the example LeNet Neural Network.

### TensorBoard
You can view training progress via TensorBoard:

```
(pytorch) cd tutorials/nn_tutorial
(pytorch) tensorboard --logdir=logs --host=0.0.0.0
```

![tensorboard](tensorboard.png)

### Profiling
For more detailed timings (CPU and GPU profiling), this example also demonstrates how to save a `nn.trace` Chrome trace file that can be viewed from the Google Chrome Browser using the URI: `chrome://tracing`.

![chrome_trace](chrome_trace.png)

More details on Chrome Tracing: https://aras-p.info/blog/2017/01/23/Chrome-Tracing-as-Profiler-Frontend/

## Evaluate on Raspberry Pi

1. [Optional] Copy the `nn_checkpoint.pt` file to the tutorials/train folder on the Raspberry Pi if you have re-trained it.
2. Launch the Raspberry Pi PyTorch docker image.
```
cd ~/stackup-workshops/pi-pytorch/docker
sh launch_docker.sh
```

3. From the docker image, run the following test script to load and evalute a neural network. You should see output like below (actual values will differ because of random seed).
```
root@xxxxx:/code# cd /tutorials/train
root@xxxxx:/code/tutorials/train# python3 nn_eval.py

result tensor([[-1.3430,  0.3558, -1.3451,  0.6432, -0.6340, -0.1667, -0.5551,
          0.3526, -0.1512, -0.1724]])
```