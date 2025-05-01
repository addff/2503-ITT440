### NAME : NUR FARISHA ADRIANA BINTI ROSLI 
### CLASS : M3CS2554B
### STUDENT ID : 2023837406
### ITT440 - 10% Individual Assignment

# Image Processing with Kornia

#### INTRODUCTION 

Image processing enhances images or extracts information using various techniques and algorithms. It improves quality, detects patterns, separates objects, and converts formats for both photos and videos. The process involves capturing an image, applying algorithms, and generating analyzable results. In this part, we will be focusing on the library used in Kornia to develop digital image processing.

![image](https://github.com/user-attachments/assets/23b65d39-55cb-41e8-a976-6e4e34a9eab2)


#### WHY KORNIA FOR IMAGE PROCESSING?

- Kornia is a unique library that makes it possible to combine traditional computer vision techniques with deep learning models. It includes various routines and modules that can handle common computer vision tasks. The library is built on PyTorch, which helps it run efficiently and allows for easy calculation of gradients for complicated functions using reverse-mode auto-differentiation.

- The library includes a collection of packages with tools that can be added to neural networks for training models to do things like change images, understand epipolar geometry, estimate depth, and handle basic image processing tasks like filtering and detecting edges, all of which work directly with tensors.

#### HIGHLIGHTED FEATURES OF KORNIA

At Kornia, we improve computer vision with a powerful and efficient toolkit based on PyTorch. We are excited to unveil a new feature that simplifies the incorporation of lightweight AI models into Kornia, helping developers and researchers tackle complex vision problems and accelerate innovation. Our collection includes models like YuNet, Loftr, and SAM, all optimized for performance without requiring costly GPUs. We encourage developers and researchers passionate about advancing computer vision to contribute their fast models!

At a granular level, Kornia is a library that consists of the following components:

- kornia : A Differentiable Computer Vision library like OpenCV, with strong GPU support
- kornia.augmentation : a module to perform data augmentation in the GPU
- kornia.color : a set of routines to perform color space conversions
- kornia.contrib : a compilation of user contrib and experimental operators
- kornia.feature : a module to perform feature detection
- kornia.filters : a module to perform image filtering and edge detection
- kornia.geometry : a geometric computer vision library to perform image transformations, 3D linear algebra and conversions using different camera models
- kornia.losses : a stack of loss functions to solve different vision tasks
- kornia.morphology : a module to perform morphological operations
- kornia.utils : image to tensor utilities and metrics for vision problems

# Example of Image Processing using Kornia

### STEP-BY-STEP OF IMPLEMENTATION

#### Step 1 : Download the python and setup the python

You can [download the python](https://www.python.org/downloads/) here and [setup the python](https://youtu.be/C3bOxcILGu4?feature=shared) by referring the video.

#### Step 2 : Install the libraries (you need to run this command in your terminal or command prompt):

1. Install Kornia, OpenCV and Matplotlib by using this command:
```
pip install kornia opencv-python matplotlib 
```

2. (Optional but Recommended) Install Torch (PyTorch)
   
   - Kornia depends on PyTorch. You can install PyTorch CPU version easily:
     
     ```
     pip install torch torchvision torchaudio
     ```
   - Or if you have an NVIDIA GPU and want CUDA (GPU speed), install like:
     
     ```
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```

#### Step 3 : Save the image that you want to modify into the file same as Python

You can save any image that you want to modify in the same folder as your Python script. This makes it easier to load the image using just its filename (e.g., 'my_image.jpg') without needing to specify a full path. 

#### Step 4 : Write and run the source code in the Python terminal.

The following code applies a series of image transformations using Kornia, converts the results to NumPy format, and displays them using Matplotlib for visual comparison:

```
import torch
import kornia
import matplotlib.pyplot as plt
import cv2

# Load and convert image to RGB
image = cv2.imread('kornia1.jpg')  # Make sure the file exists
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to normalized tensor
image_tensor = torch.tensor(image_rgb).float() / 255.0
image_tensor = image_tensor.permute(2, 0, 1).unsqueeze(0)  # (1, 3, H, W)

# Transformations
rotated_image = kornia.geometry.transform.rotate(image_tensor, torch.tensor(90.0))
blurred_image = kornia.filters.gaussian_blur2d(image_tensor, (25, 25), (10.0, 10.0))
flipped_ud_image = kornia.geometry.transform.vflip(image_tensor)
color_jitter = kornia.augmentation.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5)
jittered_image = color_jitter(image_tensor)
grayscale_image = kornia.color.rgb_to_grayscale(image_tensor)
edges_image = kornia.filters.sobel(image_tensor)
brightness_image = kornia.enhance.adjust_brightness(image_tensor, 1.5)
contrast_image = kornia.enhance.adjust_contrast(image_tensor, 1.5)

# Helper function to convert tensor to numpy image
def to_numpy(tensor):
    return tensor.squeeze(0).permute(1, 2, 0).cpu().numpy()

# Convert all results to numpy
original_np = image_rgb
rotated_np = to_numpy(rotated_image)
blurred_np = to_numpy(blurred_image)
flipped_ud_np = to_numpy(flipped_ud_image)
jittered_np = to_numpy(jittered_image)
grayscale_np = grayscale_image.squeeze().cpu().numpy()
edges_np = to_numpy(edges_image)
brightness_np = to_numpy(brightness_image)
contrast_np = to_numpy(contrast_image)

# Display all images
images = [
    (original_np, "Original"),
    (rotated_np, "Rotated 90°"),
    (blurred_np, "Max Blur"),
    (flipped_ud_np, "Flip Up-Down"),
    (jittered_np, "Color Jitter"),
    (grayscale_np, "Grayscale"),
    (edges_np, "Edge Detection"),
    (brightness_np, "Brighter"),
    (contrast_np, "More Contrast"),
]

plt.figure(figsize=(16, 10))
for i, (img, title) in enumerate(images):
    plt.subplot(3, 3, i + 1)
    if img.ndim == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.show()
```

#### THE RESULT

This script loads an image and applies a variety of computer vision transformations—such as rotation, blurring, flipping, color jitter, grayscale conversion, edge detection, brightness and contrast adjustments—then displays all results using Matplotlib.

![image](https://github.com/addff/2503-ITT440/blob/main/10%25%20Individual%20Assignment/M3CS2554B/NUR%20FARISHA%20ADRIANA%20BINTI%20ROSLI/Image%20Processing%20of%20%20Kornia.png)


Simple Demonstration Using Kornia for Image Processing on Youtube

[Let's Learn How to Use Kornia](https://youtu.be/ECqhoSgNZNI)




