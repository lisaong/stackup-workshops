import torch
import torch.nn as nn
from torch import optim
from torch.autograd import Variable
import numpy as np

# import our model and data
from rnn import RNN
from data import get_data

# command: tensorboard --logdir=logs --host=0.0.0.0
from tensorboardX import SummaryWriter

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

hidden_size = 10
learning_rate = 0.01
num_layers = 2
num_epochs = 1000
sequence_length = 10
batch_size = 32

def checkpoint(model, optimizer, epoch, loss, prev_loss):
    if (loss < prev_loss):
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss
        }, 'checkpoint.pt')

def train(model, X_train, y_train, X_val, y_val):
    # loss function: Binary Cross Entropy
    criterion = nn.BCELoss()

    # optimizer: Stochastic Gradient Descent
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    # mini-batch splitting
    # split into chunks (last chunk can be smaller than batch_size)
    num_batches = X_train.shape[0] // batch_size + 1
    X_batches = torch.chunk(X_train, num_batches, 0)
    y_batches = torch.chunk(torch.tensor(y_train.values), num_batches, 0)

    # validation set
    val_inputs = Variable(X_val.float()).to(device)
    val_targets = Variable(torch.tensor(y_val.values).float()).to(device)

    tensorboard_writer = SummaryWriter('logs/sensor')

    # training loop
    prev_val_loss = np.inf

    for epoch in range(num_epochs):
        epoch_loss = 0
        val_loss = 0

        for X_batch, y_batch in zip(X_batches, y_batches):

            # LSTM expects FloatTensors
            inputs = Variable(X_batch.float()).to(device)
            targets = Variable(y_batch.float()).to(device)

            # input: batch_size, seq_len, input_size
            outputs = model(inputs)
            optimizer.zero_grad()

            # squeeze: output dimension from (batch_size, 1) => (batch_size)
            loss = criterion(torch.squeeze(outputs), targets)
            loss.backward(retain_graph=True)
            optimizer.step()

            epoch_loss += loss.item()

        epoch_loss /= num_batches
        print('loss', epoch_loss)
        tensorboard_writer.add_scalar('loss', epoch_loss, epoch)

        val_outputs = model(val_inputs)
        val_loss = criterion(torch.squeeze(val_outputs), val_targets).item()
        print('val_loss', val_loss)

        tensorboard_writer.add_scalar('val_loss', val_loss, epoch)
        checkpoint(model, optimizer, epoch, val_loss, prev_val_loss)
        prev_val_loss = val_loss

if __name__ == '__main__':

    X_train, X_test, y_train, y_test = get_data(sequence_length)
    input_size = X_train.shape[2] # batch, seq_len, input_size

    model = RNN(input_size, hidden_size, num_layers).to(device)
    print(model)

    train(model, X_train, y_train, X_test, y_test)

