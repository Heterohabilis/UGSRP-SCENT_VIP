import cv2
import numpy as np
import torch
import torchvision
import traitlets
import ipywidgets.widgets as widgets
from IPython.display import display
from jetbot import Camera, bgr8_to_jpeg
import torch.nn as nn

class DevicePredictor():
    model = None
    device = None
    class_names = ['device 1', 'device 2', 'device 3', 'device 4']

    def __init__(self):
        # device initialize
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        # model import
        self.model = torchvision.models.resnet50(pretrained=True)
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 4)
        self.model.load_state_dict(torch.load("device_identifier.pth", map_location=torch.device('cpu')))
        self.model.eval()
        self.model.to(self.device)

    def preprocess(self, img):
        mean = 255.0 * np.array([0.485, 0.456, 0.406])
        stdev = 255.0 * np.array([0.229, 0.224, 0.225])
        normalize = torchvision.transforms.Normalize(mean, stdev)
        x = img
        x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
        x = x.transpose((2, 0, 1))
        x = torch.from_numpy(x).float()
        x = normalize(x)
        x = x.to(self.device)
        x = x[None, ...]
        return x

    def predict(self, img)->str:
        img = self.preprocess(img)
        y = self.model(img)
        _, preds = torch.max(y, 1)
        return self.class_names[preds[0]]





