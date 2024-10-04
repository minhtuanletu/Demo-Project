import torch

class CNNBlock(torch.nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, pool=False):
        super(CNNBlock, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.pool = pool
        self.module = torch.nn.Sequential(
            torch.nn.Conv2d(self.in_channels, self.out_channels, self.kernel_size, self.stride, self.padding),
            torch.nn.BatchNorm2d(self.out_channels),
            torch.nn.ReLU()
        )
        if self.pool:
            self.module.append(torch.nn.MaxPool2d(2))

    def forward(self, x):
        return self.module(x)

class MyModel(torch.nn.Module):
    def __init__(self, input_chanel, num_classes, image_size, dropout):
        super(MyModel, self).__init__()
        self.input_chanel = input_chanel
        self.num_classes = num_classes
        self.image_size = image_size
        self.dropout = dropout
        self.feature_extraction = torch.nn.Sequential(
            CNNBlock(in_channels=self.input_chanel, out_channels=8, kernel_size=3, stride=1, padding=1, pool=True),
            torch.nn.Dropout(self.dropout),
            CNNBlock(in_channels=8, out_channels=32, kernel_size=3, stride=1, padding=1, pool=True),
            torch.nn.Dropout(self.dropout),
            CNNBlock(in_channels=32, out_channels=32, kernel_size=3, stride=1, padding=1, pool=True),
            torch.nn.Dropout(self.dropout),
            CNNBlock(in_channels=32, out_channels=32, kernel_size=3, stride=1, padding=1, pool=True),
            torch.nn.Dropout(self.dropout),
            CNNBlock(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1, pool=True),
            torch.nn.Dropout(self.dropout),
            torch.nn.Flatten()
        )
        output_shape = self.compute_output_dim()
        self.MLP = torch.nn.Sequential(
            torch.nn.Linear(output_shape, 128),
            torch.nn.Linear(128, 32),
            torch.nn.Linear(32, self.num_classes),
            torch.nn.Sigmoid()
        )
    
    def compute_output_dim(self):
        x = torch.randn((1, self.input_chanel, self.image_size[0], self.image_size[1]))
        output_shape = self.feature_extraction(x).shape
        return output_shape[-1]
        
    def forward(self, x):
        feature = self.feature_extraction(x)
        output = self.MLP(feature)
        return output
    
def build_model(checkpoint_path, device):
    checkpoints = torch.load(checkpoint_path, map_location=device, weights_only=False)
    input_chanel = 1
    num_classes = 2
    dropout = 0.2
    image_size = (224, 224)
    model = MyModel(input_chanel, num_classes, image_size, dropout).to(device)
    model.load_state_dict(checkpoints['model_state_dict'])
    return model