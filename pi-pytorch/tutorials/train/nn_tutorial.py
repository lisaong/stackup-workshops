# https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# torch.backends.cudnn.deterministic = True
# torch.manual_seed(999)

# https://github.com/lanpa/tensorboardX
# conda install tensorflow-gpu
# pip install tensorboardX
# tensorboard --logdir=logs --host=0.0.0.0
from tensorboardX import SummaryWriter
writer = SummaryWriter('logs/nn_tutorial')

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

# architecture
net = Net()
print(net)

# weights
params = list(net.parameters())
for p in params:
    print(p.size())
    print(p)

# prediction
input = torch.randn(1, 1, 32, 32)
output = net(input)
print(output)

# loss function
target = torch.randn(10) # normal distribution
target = target.view(1, -1) # reshape to same shape as output
criterion = nn.MSELoss()
loss = criterion(output, target)
print(loss)

# navigate loss function graph
grad_fn = loss.grad_fn
print(grad_fn)
while (len(grad_fn.next_functions)):
    grad_fn = grad_fn.next_functions[0][0]
    print(grad_fn)

# backprop
net.zero_grad() # clear gradient buffers (otherwise will accumulate)
print('before backward', net.conv1.bias.grad)
loss.backward()
print('after backward', net.conv1.bias.grad)

# weight update
# weight = weight - learning_rate * gradient
optimizer = optim.SGD(net.parameters(), lr=1e-2)

# training loop
# https://pytorch.org/docs/stable/optim.html#optimizer-step
n_iters = 100

# https://pytorch.org/docs/stable/autograd.html#profiler
# with torch.autograd.profiler.profile(use_cuda=True) as prof:
for i in range(n_iters):
    optimizer.zero_grad() # not accumulating in a batch
    output = net(input)
    loss = criterion(output, target)
    loss.backward()
    print(loss.item())
    writer.add_scalar('loss', loss.item(), i) # update tensorboard
    optimizer.step() # update
# print(prof.table())
# prof.export_chrome_trace('nn.trace')

# https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-a-general-checkpoint-for-inference-and-or-resuming-training

# save model parameters only (recommended for portability)
torch.save({
    'epoch': n_iters,
    'model_state_dict': net.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss
}, 'nn_checkpoint.pt')

# load model parameters
net2 = Net()
checkpoint = torch.load('nn_checkpoint.pt')
net2.load_state_dict(checkpoint['model_state_dict'])
net2.eval() # just evaluation

input = torch.randn(1, 1, 32, 32)
print('serialized model', net2(input))
print('original', net(input))
