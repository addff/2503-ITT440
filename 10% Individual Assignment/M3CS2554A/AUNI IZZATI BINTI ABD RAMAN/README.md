NAME: AUNI IZZATI BINTI ABD RAMAN

GROUP:CDCS2554A

STUDENT ID: 2023260244

# *TITLE: INTRODUCTION TO IMAGE PROCESSING USING KORNIA IN PYTHON.*

### INTRODUCTION

Image processing is a method of performing operations on an Image to enhance it or to extract useful information. It is a key area in computer vision, machine learning and artificial intelligence. Some common tasks in image processing include adjusting color, blurring, rotating, sharpening, and transforming images for further analysis or display.


![image](https://github.com/user-attachments/assets/9c45e3cc-e8d0-4833-8b91-2720dac2a119)

🔥**What is Kornia?** 

Kornia is an open-source computer vison library built on top of PyTorch. It provides a wide range of mage processing functions using tensor operations, allowing images to be manipulated just like numerical data. This makes Kornia powerful for building flexible and efficient computer vision applications, especially when combined with deep learning.

🔥**Why Choose Kornia?**

Kornia was chosen because it integrates smoothly with PyTorch, which is a widely used deep learning framework. Kornia allows for simple, readable code while still providing fast, GPU-accelerated operations. Instead of switching between different libraries for different tasks, Kornia brings computer vison capabilities directly into the PyTorch ecosystem.

🔥**Advantages of using Kornia?**

-	GPU Acceleration: Operations can run on GPU for faster computation.
  
-	Integration with PyTorch: Easy to combine image transformations with deep learning models.
  
-	Simple Syntax: Clear and concise code, easy to learn for beginners.
  
-	Open Source: Free to use, with a strong community and regular updates.
  
-	Wide Range of Functions: Includes geometry transformations, color adjustments, filters, feature detection and more.


In this project, Kornia was used to apply various basic image transformations. The transformations included:

•	Rotation - Rotating the image by a specified angle.

•	Gaussian Blur - Applying a blur effect to smooth the image.

•	Grayscale Conversion - Changing the image to black and white.

•	Hue Adjustment - Shifting the hue to change the image color tone.

•	Contrast Adjustment - Increasing or decreasing the contrast to make images clearer or softer.

All transformations were implemented using Kornia’s functions, demonstrating its capability for simple yet powerful image manipulation.

***
This script demonstrates image transformations using PyTorch and Kornia. It includes functions for loading an image, applying Gaussian blur, rotating, converting to grayscale, adjusting hue, and contrast. 

### Code for image transformations:


```
import torch
import kornia
import torchvision.transforms as transforms
from PIL import Image

# Load the image and convert to tensor
def load_image(image_path):
    image = Image.open(image_path).convert("RGB")  
    transform = transforms.ToTensor()
    image_tensor = transform(image)
    return image_tensor

# Save tensor as image
def save_image(tensor_image, file_name):
    to_pil = transforms.ToPILImage()
    image = to_pil(tensor_image)
    image.save(file_name)

# Apply Gaussian blur
def blur_image(image_tensor, kernel_size=7, sigma=5.0):
    blurred = kornia.filters.gaussian_blur2d(image_tensor.unsqueeze(0), (kernel_size, kernel_size), sigma=(sigma, sigma))
    return blurred.squeeze(0)

# Rotate image
def rotate_image(image_tensor, angle=45.0):
    angle_tensor = torch.tensor([angle])
    rotated = kornia.geometry.transform.rotate(image_tensor.unsqueeze(0), angle_tensor)
    return rotated.squeeze(0)

# Convert to grayscale
def convert_to_grayscale(image_tensor):
    grayscale = kornia.color.rgb_to_grayscale(image_tensor.unsqueeze(0))
    return grayscale.squeeze(0)

# Adjust hue
def adjust_hue(image_tensor, hue_factor=0.2):
    adjusted = kornia.enhance.adjust_hue(image_tensor.unsqueeze(0), hue_factor)
    return adjusted.squeeze(0)

# Adjust contrast
def adjust_contrast(image_tensor, contrast_factor=1.5):
    adjusted = kornia.enhance.adjust_contrast(image_tensor.unsqueeze(0), contrast_factor)
    return adjusted.squeeze(0)

# Main function
def main():
    image_path = "artist_image.jpg"  
    image_tensor = load_image(image_path)
    print(f"Original Image Size: {image_tensor.shape}")

    # Apply and save each transformation
    save_image(rotate_image(image_tensor), "rotated.jpg")
    save_image(blur_image(image_tensor), "blurred.jpg")
    save_image(convert_to_grayscale(image_tensor), "grayscale.jpg")
    save_image(adjust_hue(image_tensor, 0.2), "hue_adjusted.jpg")
    save_image(adjust_contrast(image_tensor, 1.5), "contrast_adjusted.jpg")
    print("All transformed images saved successfully.")

if __name__ == "__main__":
    main()
```

<h3>The Original Image</h3>
<figure>
  <img src="https://github.com/user-attachments/assets/52935cac-06ce-41c1-a672-ec4bfdabcefe" width="450"/>
</figure>

<h3>The Blurred Image</h3>
<figure>
  <img src="https://github.com/user-attachments/assets/c76004a8-1595-4e16-9808-6ce669ee5229" width="450"/>
</figure>

<h3>The Contrast</h3>
<figure>
  <img src="https://github.com/user-attachments/assets/aad8fad3-f8a1-4cdc-92c5-82f8442e25de" width="450"/>
</figure>

<h3>The Grayscale</h3>
<figure>
  <img src="https://github.com/user-attachments/assets/4b74a2c1-38e9-4e2b-a090-dab8e74422bd" width="450"/>
</figure>

  <h3>The Hue</h3>
  <figure>
  <img src="https://github.com/user-attachments/assets/9d44455c-7aa3-4338-8059-217933f6238a" width="450"/>
</figure>

  <h3>The Rotation</h3>
  <figure>
  <img src="https://github.com/user-attachments/assets/e7fee9d4-d342-4b56-93d4-934065c53541" width="450"/>
</figure>


https://drive.google.com/file/d/10KzdlmW93jHaF7t9ueKvDsRJwb1NiTQt/view?usp=sharing

