import torch
from torch.autograd import Variable

# import our network
from rnn import SimpleRNN

# import our data generator
from data import sample

def load_model():
    model = SimpleRNN(hidden_size=50)
    checkpoint = torch.load('checkpoint.pt')
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    print(model)
    return model

def generate_data():
    sequence_len = 50
    samples = sample(sequence_len) # generate new data
    inputs = Variable(torch.from_numpy(samples[:-1]).float()) # 0 .. n-1
    return inputs

if __name__ == '__main__':
    model = load_model()
    inputs = generate_data()

    outputs, hidden = model(inputs)
    print('generated output', outputs.data.view(-1))
