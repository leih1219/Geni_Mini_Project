import torch
from PIL import Image
from torchvision import transforms


class Img_reco():
    def __init__(self):
        self.model = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
        self.model.eval()
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        with open("Server/imagenet_classes.txt", "r") as f:
            categories = [s.strip() for s in f.readlines()]
        self.categories = categories

    # import urllib
    # url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
    # try: urllib.URLopener().retrieve(url, filename)
    # except: urllib.request.urlretrieve(url, filename)

    def predict(self, filename):
        input_image = Image.open(filename)
        input_tensor = self.preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

        # move the input and model to GPU for speed if available
        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            self.model.to('cuda')

        with torch.no_grad():
            output = self.model(input_batch)

        # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
        probabilities = torch.nn.functional.softmax(output[0], dim=0)

        top5_prob, top5_catid = torch.topk(probabilities, 5)
        prediction = []
        for i in range(top5_prob.size(0)):
            print(self.categories[top5_catid[i]], top5_prob[i].item())
            prediction.append([self.categories[top5_catid[i]], top5_prob[i].item()])
        return prediction


if __name__ == '__main__':
    Img_reco = Img_reco()
    filename = "1.jpg"
    # input_image = Image.open(filename)
    result = Img_reco.predict(filename)
    print(result)
