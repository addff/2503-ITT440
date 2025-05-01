# NAME : NUR FARISHA ADRIANA BINTI ROSLI
# STUDENT ID : 2023837406

# Image Processing with Kornia

**INTRODUCTION**

Image processing enhances images or extracts information using various techniques and algorithms. It improves quality, detects patterns, separates objects, and converts formats for both photos and videos. The process involves capturing an image, applying algorithms, and generating analyzable results. In this part, we will be focusing on the library used in Kornia to develop digital image processing.

![image](https://github.com/user-attachments/assets/23b65d39-55cb-41e8-a976-6e4e34a9eab2)


**WHY KORNIA FOR IMAGE PROCESSING?**

- Kornia is a unique library that makes it possible to combine traditional computer vision techniques with deep learning models. It includes various routines and modules that can handle common computer vision tasks. The library is built on PyTorch, which helps it run efficiently and allows for easy calculation of gradients for complicated functions using reverse-mode auto-differentiation.

- The library includes a collection of packages with tools that can be added to neural networks for training models to do things like change images, understand epipolar geometry, estimate depth, and handle basic image processing tasks like filtering and detecting edges, all of which work directly with tensors.

**HIGHLIGHTED TOOLS OF KORNIA**

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

# Example

import torch
import kornia
import matplotlib.pyplot as plt
import cv2

Load and convert image to RGB
image = cv2.imread('kornia1.jpg')  # Make sure the file exists
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

Convert to normalized tensor
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





