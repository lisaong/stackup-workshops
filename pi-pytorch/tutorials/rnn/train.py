# https://pytorch.org/tutorials/beginner/ptcheat.html
import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.autograd import Variable
from torch import optim
import random

# import our network
from rnn import SimpleRNN

# import our sample data
from data import sample

# command: tensorboard --logdir=logs --host=0.0.0.0
from tensorboardX import SummaryWriter

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
        tensorboard_writer.add_scalar('loss', epoch_loss, epoch)
        print(epoch_loss)

if __name__ == '__main__':
    print(torch.cuda.device(0))

    model = SimpleRNN(hidden_size=50)
    train(model, n_epochs=100, n_samples=50, sequence_len=50)
