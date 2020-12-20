import torch
import sys
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import numpy as np


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        in_size = 1
        transform = transforms.ToTensor()
        x = transform(x)
        x = x[None, :, :, :] # for BCHW
        x = F.relu(self.mp(self.conv1(x)))
        x = F.relu(self.mp(self.conv2(x)))
        x = x.view(in_size, -1)  # flatten the tensor
        x = self.fc(x)
        return torch.argmax(F.softmax(x, dim=1)).item(), F.softmax(x, dim=1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("main.py <img path>")
        exit(0)
    model = Net()
    model.load_state_dict(torch.load('PATH.pth'))
    model.eval()

    path = sys.argv[1]
    img = Image.open(path)
    img = img.resize((28,28)) # MNIST size
    output, sm = model(img)
    print(sm)
    print("this number is " + str(output))


    #python main.py C:\Users\teang\PycharmProjects\C084/1.jpg
