import torch
from torch.autograd import Variable
from sklearn.metrics import confusion_matrix

# import our model and data
from rnn import RNN
from data import get_data

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

hidden_size = 10
learning_rate = 0.01
num_layers = 2
num_epochs = 1000
sequence_length = 10
batch_size = 32

def load_model(input_size):
    model = RNN(input_size, hidden_size, num_layers).to(device)
    checkpoint = torch.load('checkpoint.pt')
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

    inputs = Variable(X_test.float()).to(device)
    outputs = model(inputs)

    print(confusion_matrix(y_test.values, outputs.data.view(-1)))