import sys
from PIL import Image
import torch
import open_clip

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

image_path = sys.argv[1]
image = preprocess(Image.open(image_path)).unsqueeze(0)
with torch.no_grad():
    image_features = model.encode_image(image)
print(image_features.squeeze().tolist())
