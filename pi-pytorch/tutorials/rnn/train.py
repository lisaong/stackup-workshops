# https://pytorch.org/tutorials/beginner/ptcheat.html
# or try https://github.com/pytorch/ignite

import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.autograd import Variable
from torch import optim
import numpy as np
import random

# import our network
from rnn import SimpleRNN

# import our data generator
from data import sample

# command: tensorboard --logdir=logs --host=0.0.0.0
from tensorboardX import SummaryWriter

def checkpoint(model, optimizer, epoch, loss, prev_loss):
    if (loss < prev_loss):
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss
        }, 'checkpoint.pt')

def train(model, n_epochs, n_samples, sequence_len):
    """Trains the recurrent neural network
    Arguments:
        model: the RNN
        n_epochs: number of epochs
        n_samples: number of input sequences to sample per epoch
        sequence_len: length of each input sequence
    """
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    tensorboard_writer = SummaryWriter('logs/simple_rnn')

    # training loop
    prev_loss = np.inf
    for epoch in range(n_epochs):
        epoch_loss = 0

        for i in range(n_samples):
            samples = sample(sequence_len) # generate new data

            inputs = Variable(torch.from_numpy(samples[:-1]).float()) # 0 .. n-1
            targets = Variable(torch.from_numpy(samples[1:]).float()) # 1 .. n

            # apply teacher forcing 50% of the time
            force = random.random() < 0.5

            # forward propagation for len(inputs) steps
            outputs, hidden = model(inputs, hidden=None, force=force)

            optimizer.zero_grad()
            loss = criterion(torch.squeeze(outputs), targets)
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        epoch_loss /= n_samples
        print(epoch_loss)
        tensorboard_writer.add_scalar('loss', epoch_loss, epoch)
        checkpoint(model, optimizer, epoch, epoch_loss, prev_loss)
        prev_loss = epoch_loss

if __name__ == '__main__':
    model = SimpleRNN(hidden_size=50)
    print(model)
    train(model, n_epochs=100, n_samples=50, sequence_len=50)
