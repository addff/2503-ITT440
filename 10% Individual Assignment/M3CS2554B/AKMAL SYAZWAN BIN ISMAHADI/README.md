# AKMAL SYAZWAN BIN ISMAHADI
# 2023277674

---

### **Introduction to Image Processing with PyTorch**
Image processing involves manipulating and analyzing images to extract useful information or enhance visual quality. PyTorch is a powerful deep learning framework, widely used for computer vision tasks, including image processing. It provides dynamic computation graphs and flexibility, making it suitable for experimenting with models and algorithms.

---

### **Core Concepts in Image Processing**
1. **Pixels and Representations**: Images are composed of pixels, each containing intensity values (e.g., RGB channels for color images).
2. **Transformations**: Operations such as resizing, cropping, rotating, and normalizing are essential for preprocessing images.
3. **Feature Extraction**: Techniques such as edge detection, segmentation, and filters to analyze images.
4. **Convolutional Neural Networks (CNNs)**: A specialized architecture used in image classification and recognition tasks. PyTorch supports building and training CNNs efficiently.
5. **Tensor Representation**: In PyTorch, images are represented as tensors—a multi-dimensional array enabling mathematical operations.

---

### **Tools for Image Processing in PyTorch**
1. **Torchvision Library**:
   - Contains datasets, models, and image transformations.
   - Common transformations: `transforms.Compose()`, `transforms.ToTensor()`, and `transforms.Normalize()`.
   
2. **Dataloader**:
   - Simplifies loading and batching of image datasets.
   - Example: `torch.utils.data.DataLoader()`.
   
3. **Autograd**:
   - Enables automatic differentiation for backpropagation.
   
4. **Pre-trained Models**:
   - Models like ResNet, VGG, and EfficientNet, available in `torchvision.models` for transfer learning or feature extraction.

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
