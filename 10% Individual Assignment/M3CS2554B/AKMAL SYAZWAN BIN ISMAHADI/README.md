# AKMAL SYAZWAN BIN ISMAHADI
# 2023277674

---

### **Introduction to Image Processing with PyTorch**
![image alt](https://github.com/akmalsyzwn/picture/blob/main/Pytorch_logo.png?raw=true)

Image processing is all about tweaking and analyzing pictures to pull out useful details or make them look better. PyTorch, a powerful deep learning framework, is widely used in computer vision for these tasks. Thanks to its flexible structure and dynamic computational graphs, it’s a go-to choice for building and experimenting with models.

---

### **Core Concepts in Image Processing**
1. **Pixels and Representations**: Every image is just a collection of pixels, each storing intensity values like RGB for colors.
2. **Transformations**: Before using images in models, they often need resizing, cropping, rotating, or normalizing.
3. **Feature Extraction**: This involves techniques like edge detection, segmentation, and filtering to break down image data
4. **Convolutional Neural Networks (CNNs)**: These are specially designed networks for recognizing patterns in images. PyTorch makes building and training them efficient
5. **Tensor Representation**: PyTorch represents images as tensors, which are basically multi-dimensional arrays that allow quick calculations.

---

### **Tools for Image Processing in PyTorch**
1. **Torchvision Library**:
   - A collection of datasets, pre-trained models, and tools for image transformations. 
   - Common transformations: `transforms.Compose()`, `transforms.ToTensor()`, and `transforms.Normalize()`.
   
2. **Dataloader**:
   - This helps load images in batches, making it easier to work with large datasets.
   - Example: `torch.utils.data.DataLoader()`.
   
3. **Autograd**:
   - PyTorch’s automatic differentiation tool, crucial for model training.
   
4. **Pre-trained Models**:
   - Instead of training from scratch, you can use well-known models like ResNet, VGG, or EfficientNet from `torchvision.models` for tasks like transfer learning or feature extraction.

---

### **Example in PyTorch**
Here’s a simple example to preprocess an image, load it into PyTorch, and apply transformations:

```python
from torchvision import transforms
from PIL import Image
import torch

# Load the image
image = Image.open("example.jpg")

# Define transformations
transform = transforms.Compose([
    transforms.Resize((128, 128)),     # Resize to 128x128
    transforms.ToTensor(),             # Convert to PyTorch Tensor
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalize
])

# Apply transformations
image_tensor = transform(image)

print(image_tensor.shape)  # Output the tensor shape
```
### **Full Guide to do Image Processing in Pytorch**
https://www.youtube.com/watch?v=5TMRnwmwGTI


---

### **Real-World Applications**
1. **Medical Imaging**:
   - Detecting anomalies in X-rays, MRI scans, and CT images.
   - PyTorch is used to train models for diagnosing diseases.

2. **Autonomous Vehicles**:
   - Image recognition for detecting obstacles, lanes, and traffic signs.
   - PyTorch powers vision systems in self-driving cars.

3. **Retail and E-commerce**:
   - Product search using image recognition.
   - Detecting objects on shelves or customer behavior analysis.

4. **Security Systems**:
   - Facial recognition and intrusion detection.
   - PyTorch excels in building real-time monitoring systems.

5. **Art Restoration**:
   - Enhancing and restoring old or damaged images.

---
