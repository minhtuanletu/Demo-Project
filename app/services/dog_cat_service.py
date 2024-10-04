import torch
from torchvision.transforms import v2

def predict(image, model, device):
    labels = {0: 'cats', 1: 'dogs'}
    image_size = (224, 224)
    transform = v2.Compose([
        v2.Resize(image_size, antialias=True),
        v2.PILToTensor(),
        v2.ToDtype(torch.float),
    ])
    transformed_input = transform(image)
    transformed_input = torch.unsqueeze(transformed_input, dim=0).to(device)
    output = model(transformed_input)
    result = torch.argmax(output.cpu(), dim=-1).numpy()
    label_name = labels[result[0]]
    conf = torch.max(torch.nn.functional.softmax(output, dim=-1).cpu(), dim=-1).values.detach().numpy()[0]
    return {
        'label_name': label_name,
        'conf': conf,
        'status': 'successful'
    }