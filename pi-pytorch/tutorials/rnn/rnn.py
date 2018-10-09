# https://gist.github.com/spro/ef26915065225df65c1187562eca7ec4

import torch
import torch.nn as nn
from torch.autograd import Variable

class SimpleRNN(nn.Module):

    def __init__(self, hidden_size):
        super(SimpleRNN, self).__init__()

        self.hidden_size = hidden_size

        self.input = nn.Linear(1, hidden_size)

        # stacked LSTM with Dropout in between
        self.rnn = nn.LSTM(input_size=hidden_size, hidden_size=hidden_size,
            num_layers=2, dropout=0.05)

        self.output = nn.Linear(hidden_size, 1)

    def _step(self, input, hidden=None):
        'Called by forward() to advance the RNN by 1 step'
        # 1. Flatten the input
        # 2. Insert an extra timestep dimension after the batch dimension
        #     batch_dim, data_dim => batch_dim, 1 (timestep), data_dim
        input = self.input(input.view(1, -1)).unsqueeze(1)

        # step through stacked LSTM
        output, hidden = self.rnn(input, hidden)

        # unsqueeze = removes all dimensions of size 1
        output = self.output(output.squeeze(1))
        return output, hidden

    def forward(self, inputs, hidden=None, force=True, steps=0):
        """Perform forward propagation in the network
        Arguments:
            inputs: input sequence
            hidden: previous hidden state
            force: apply teacher forcing (use output from the previous
                   forward propagation instead of the previous step as input)
            steps: number of forward steps
        Returns:
            the outputs and the updated hidden state

        Teacher forcing:
            https://machinelearningmastery.com/teacher-forcing-for-recurrent-neural-networks/
        """

        # when teacher forcing is used, always step through the
        # entire input sequence (output from previous forward propagation)
        if force or steps == 0:
            steps = len(inputs)

        outputs = Variable(torch.zeros(steps, 1, 1))
        for i in range(steps):
            if force or i == 0:
                # use output from the previous forward() call
                input = inputs[i]
            else:
                # use output from the previous step
                input = output

            # advance the RNN layers by 1 timestep
            output, hidden = self._step(input, hidden)
            outputs[i] = output

        return outputs, hidden
