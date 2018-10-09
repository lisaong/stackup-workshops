import torch
import torch.nn as nn

class RNN(nn.Module):

    def __init__(self, input_size, hidden_size, num_layers):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size
        self.num_layers = num_layers

        # batch_first=True means we expect input to be batch, seq_len, input_size
        self.rnn = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, input):

        # input: batch, seq_len, input_size
        # output: batch, seq_len, hidden_size
        output, _ = self.rnn(input)

        # Decode the hidden state of the last time step
        output = torch.sigmoid(self.fc(output[:, -1, :]))
        return output