import torch
import math
import torch.nn as nn
import numpy as np
import torch.nn.functional as F

def xavier_init(param):
    # NOTE: Not for Vanilla Classifier
    # TODO: Complete this to initialize the weights
    for p in param:
        classname = p.__class__.__name__
        
        if isinstance(p, nn.Linear):
            # stdv = 1. / math.sqrt(p.weight.size(1))
            torch.nn.init.xavier_normal_(p.weight)
            # p.bias.data.uniform_(-stdv, stdv)

def zero_init(param):
    # NOTE: Not for Vanilla Classifier
    # TODO: Complete this to initialize the weights
    for p in param:
        classname = p.__class__.__name__
        
        if isinstance(p, nn.Linear):
            torch.nn.init.zeros_(p.weight)
            torch.nn.init.zeros_(p.bias)
            
def ones_init(param):
    for p in param:
        if isinstance(p, nn.Linear):
            torch.nn.init.ones_(p.weight)
            torch.nn.init.ones_(p.bias)

class Network(nn.Module):
    def __init__(self,init_method=None):
        super(Network, self).__init__()
        # TODO: Define the model architecture here
        # raise NotImplementedError
        #28*28
        # 28
        # self.conv1 = nn.Conv2d(1, 10, 5, stride=1)
        # #24*24*10
        # self.hiddenc1= nn.Linear(1440,100)
        self.hidden = nn.Linear(784, 100)

        # Output layer, 10 units - one for each digit
        self.output = nn.Linear(100, 10)
        
        # Define relu activation and softmax output 
        self.relu = nn.ReLU()
        # self.drop = nn.Dropout(p=0.44)
        self.init_weights(init_method)
        # NOTE: Not for Vanilla Classsifier
        # TODO: Initalize weights by calling the
        # init_weights method
        # self.init_weights()

    def init_weights(self,init_method):
        # NOTE: Not for Vanilla Classsifier
        # TODO: Initalize weights by calling by using the
        # appropriate initialization function
        if init_method is 'xavier':
            xavier_init(self.modules())
        elif init_method is 'zero':
            zero_init(self.modules())
        elif init_method is 'one':
            ones_init(self.modules())
        else:
            None

        # raise NotImplementedError

    def forward(self, x):
        # TODO: Define the forward function of your model
        # x=self.drop(x)
        
        # x = self.relu(self.conv1(x))
        # #24*24*10
        # x = F.max_pool2d(x, 2, 2)
        # x=x.reshape(x.size(0), -1)
        # #12*12*10
        # x=self.hiddenc1(x)



        x = self.hidden(x)
        # x=self.drop(x)
        x = self.relu(x)
        x = self.output(x)
        # x = self.softmax(x)
        return x
    
    def save(self, ckpt_path):
        # TODO: Save the checkpoint of the model
        torch.save(Network.state_dict(), ckpt_path)
        

    def load(self, ckpt_path):
        # TODO: Load the checkpoint of the model
        model.load_state_dict(torch.load(ckpt_path))