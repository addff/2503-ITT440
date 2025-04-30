# MUHAMMAD SUFI AIMAN BIN SHAHRUL AMIN (20238376284b)
# Computer Visual Graphic with Imgaug

## Introduction
In the context of computer vision, image processing, or data visualisation, computer visual graphic is refers to the use of code to create or display visual content, such as diagrams, interactive graphics, or photographs.

---

## Features
-Apply various image augmentations (rotation, flipping, brightness,     noise, etc.)
-Visualize augmented images side-by-side with the original
-Draw bounding boxes on images before and after augmentation
-Useful for debugging and understanding how augmentations affect your   dataset

---

## Core Concept
- **Preprocessing**: Resize, normalize, blur, denoise
- **Feature Extraction**: Improve generalization with augmented variants
- **Segmentation**: Synchronized image-mask transformations
- **Classification**: Increase robustness through image variety

---

![image](https://github.com/user-attachments/assets/2aa0aa5d-23b4-4203-b40d-6f4b0d829841)

---

## 🛠️ **Why** imgaug?

imgaug is a flexible and powerful image augmentation library that supports:

Geometric transformations (flip, rotate, scale)
Color and brightness adjustments
Noise addition and blurring
Object-aware augmentation (bounding boxes, keypoints, segmentation masks)

---
## Installation and setup

### 1.🦅 Standard Installation 
This is the most common that people use to install imgaug:

```bash 
pip install imgaug
```

### 2.📦 Recommended Extra Packages

To work with images and visualize them, you’ll likely want:

```bash
pip install imageio matplotlib opencv-python
```
### 3.🧪 Check Installation

Open a Python shell or script and run:

```bash
import imgaug
print(imgaug.__version__)
```
If no error occurs, it’s installed correctly.

---
##Installation 

👉 https://imgaug.readthedocs.io/en/latest/source/installation.html

---
## 🔍 Python Code (Computer Visual Graphic)

Here's a simple script to load an image and apply several augmentations using imgaug.

---

```bash
import imgaug.augmenters as iaa
import imageio
import matplotlib.pyplot as plt

# Load an image
image = imageio.imread('example.jpg')  # Replace with your image path

# Define the augmentation pipeline
aug = iaa.Sequential([
    iaa.Fliplr(0.5),                      # Flip horizontally with 50% probability
    iaa.Affine(rotate=(-20, 20)),        # Rotate between -20 and +20 degrees
    iaa.AdditiveGaussianNoise(scale=(10, 60)),  # Add Gaussian noise
    iaa.GaussianBlur(sigma=(0.0, 1.0))   # Apply Gaussian blur
])

# Apply augmentation
augmented_image = aug(image=image)

# Display the result
plt.imshow(augmented_image)
plt.axis('off')
plt.title("Augmented Image")
plt.show()
```
---

## 🖼️ Expected Output Description

### When you run this script with a valid image file like example.jpg, the output will be:

✅ Original Image with Augmentations:
The displayed image (augmented_image) will look like a randomly transformed version of the original, with these effects:

**Horizontal Flip (50% chance):** The image might be flipped left-to-right.
**Rotation:** Randomly rotated between -20° and +20°.
Gaussian Noise: The image will have visual "static" or noise added—like a grainy texture.
**Blur:** A soft blur effect, simulating slight out-of-focus or camera shake.

Each time you run the script, a different variation may appear due to the random nature of the augmentations.








