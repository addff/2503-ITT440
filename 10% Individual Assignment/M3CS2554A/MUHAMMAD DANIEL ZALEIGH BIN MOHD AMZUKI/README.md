## NAME : MUHAMMAD DANIEL ZALEIGH BIN MOHD AMZUKI

## STUDENT ID : 2023240232

## CLASS : CDCS2554A

## TITLE: INTRODUCTION TO BASIC IMAGE PROCESSING USING MAHOTAS IN PHYTON.

### Objectives 
* To understand the basics of image processing
* To learn how Mahotas can be used for thresholding and edge detection
* To write and run Phyton code using Mahotas
* To demonstrate and explain the output in a video
  
### What is Image Processing?

Image processing is a technique used to manipulate and analyze digital images in order to improve their quality, extract meaningful information, or prepare them for further tasks such as classification or recognition. It involves applying mathematical and algorithmic operations to pixel data, enabling computers to interpret images in ways that are useful for both human understanding and machine automation. Common applications include enhancing photo clarity, detecting objects or patterns, removing noise, segmenting regions of interest, and analyzing textures or shapes. Image processing plays a vital role in various fields such as medical diagnostics, surveillance, robotics, remote sensing, and artificial intelligence, making it a foundational tool in modern technological and scientific development.

### What is Mahotas?

Mahotas is an open-source computer vision and  image processing library for phyton. Unlike heavier libraries like OpenCV, Mahotas is lightweight and focuses on numerical operations using NumPy arrays.
* Developed in C++ for speed
* Ideal for bio-image analysis and scientific image processing
* Compatible with NumPy and SciPy

### Significance of Mahotas 
* Fast performance due to C++ backend
* Easy to intergrate with other scientific libraries like NumPy and Matplotlib
* Great for academic and research usage, especially in Biology

### Library related to Mahotas
* NumPy: Used for array handling
* Matplotlib: For displaying images
* SciPy: Sometimes used alongside for mathematical functions
* OpenCV: A more feature-rich alternative for advanced tasks

### Module / Subpackages in Mahotas
Mahotas contains many modules such as:
* mahotas.thresholding: Thresholding methods (e.g Otsu)
* mahotas.filters: Filtering like Gaussian, Sobel, etc.
* mahotas.features: For Haralick features, Zernike moments
* mahotas.morph: Morphological operations (e.g erosion, dilation)

### Phyton Code Example: Basic Image Processing with Mahotas
```bash
import mahotas
import numpy as np
import matplotlib.pyplot as plt
from mahotas.thresholding import otsu
from mahotas import sobel

# Load a sample image (grayscale)
image = mahotas.demos.load('nuclear')  # or load your own with mahotas.imread()

# Apply Otsu thresholding
T_otsu = otsu(image)
binary = image > T_otsu

# Apply Sobel filter for edge detection
edges = sobel(image)

# Display results
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(binary, cmap='gray')
ax[1].set_title(f'Otsu Thresholding (T={T_otsu})')
ax[1].axis('off')

ax[2].imshow(edges, cmap='gray')
ax[2].set_title('Sobel Edge Detection')
ax[2].axis('off')

plt.tight_layout()
plt.show()

```
### [Watch My Mahotas Image Processing Demo]
(https://img.youtube.com/vi/5yiIxnm_Glk/0.jpg)(https://www.youtube.com/watch?v=5yiIxnm_Glk)
