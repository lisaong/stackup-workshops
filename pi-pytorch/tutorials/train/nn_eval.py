import torch
import torch.nn as nn
import torch.nn.functional as F

# LeNet
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5) # stride = 1
        self.conv2 = nn.Conv2d(6, 16, 5)

        # y = Wx + b
        self.fc1 = nn.Linear(in_features=16*5*5, out_features=120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # conv(1, 6, 5), relu, maxpool
        x = F.max_pool2d(F.relu(self.conv1(x)), kernel_size=2)
        # conv(6, 16, 5), relu, maxpool
        x = F.max_pool2d(F.relu(self.conv2(x)), kernel_size=2)
        # flatten
        x = x.view(-1, self.num_flat_features(x))
        # classifier
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

# load model parameters
net = Net()
checkpoint = torch.load('nn_checkpoint.pt')
net.load_state_dict(checkpoint['model_state_dict'])
net.eval() # just evaluation

input = torch.randn(1, 1, 32, 32)
print('result', net(input))