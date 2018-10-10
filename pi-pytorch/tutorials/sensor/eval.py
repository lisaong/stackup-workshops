import torch
from torch.autograd import Variable
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import time

# import our model and data
from rnn import RNN
from data import get_data

hidden_size = 10
learning_rate = 0.01
num_layers = 2
num_epochs = 1000
sequence_length = 10
batch_size = 32

def load_model(input_size):

    model = RNN(input_size, hidden_size, num_layers)

    # load on CPU only
    checkpoint = torch.load('checkpoint.pt', map_location='cpu')
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()

    print(model)
    print('model training loss', checkpoint['loss'])
    print('model training epoch', checkpoint['epoch'])

    return model

if __name__ == '__main__':

    X_train, X_test, y_train, y_test = get_data(sequence_length)
    input_size = X_train.shape[2] # batch, seq_len, input_size

    model = load_model(input_size)
    inputs = Variable(X_test.float())

    tick = time.time()
    outputs = model(inputs)
    tock = time.time()

    # convert probabilities => 0 or 1
    y_pred = (outputs.detach().numpy() > 0.5).astype(np.int)

    print('prediction time: %.3fs' % (tock - tick))

    print(confusion_matrix(y_test.values, y_pred))
    print(classification_report(y_test.values, y_pred))
