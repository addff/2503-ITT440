## NAME: FATIN AIDA BINTI OTHMAN
## STUDENT NO: 2023406298
## CLASS: M3CS2554A
## TITLE: IMAGE PROCESSING USING SCIKIT-IMAGE

**Objective**

To write an article about Image Processing using SCIKIT-IMAGE tools
To demonstrate the coding and functions used in SCIKIT-IMAGE related to the topic.

**Introduction to Image Processing**

Image processing involves enhancing and analyzing digital images through algorithmic and mathematical techniques. The scikit-image library in Python offers a wide range of tools for image preprocessing, analysis, and visualization. It is widely used in practical applications such as industrial inspection, surveillance, and medical imaging, reflecting its growing relevance in fields like computer vision and machine learning.

**What is SCIKIT-IMAGES ?**

Scikit-image (also known as skimage) is one of the open-source image-processing libraries for the Python programming language. It provides a powerful toolbox of algorithms and functions for various image processing and computer vision tasks and it is built on top of popular scientific libraries like NumPy and SciPy.ndimage. Scikit-image also known image processing Python package that works with NumPy arrays which is a collection of algorithms for image processing.

**Feature of SCIKIT-IMAGES:**

1. **Open-source and free**:  Available at no cost and without usage restrictions.
2. **Supports many image formats**: Can read and write JPEG, PNG, TIFF, and more.
3. **Uses NumPy arrays**: Images are stored as NumPy `ndarray`, so you can use NumPy functions to manipulate them.
4. **Provides many image processing tools**: Functions for filtering, segmentation, feature extraction and morphological operations
5. **Easy to use**: Beginner-friendly and consistent API.

**Advantages of SCIKIT-IMAGE**

1. **Works Well with Other Python Tools**  
   - Used popular libraries like NumPy and SciPy.
   - Can mix image processing with data analysis, machine learning, or math easily.

2. **Has Many Built-in Image Tools**  
   - Can do lots of things: blur, sharpen, resize, detect edges, find shapes, and more.
   - It's like a toolbox for images where everything you need is included.

3. **Easy to See What user's Doing**  
   - It works with matplotlib so user can easily show images and results.
   - Great for learning and testing what happens when user change the settings.

4. **Beginner-Friendly and Well-Documented**  
   - Lots of examples and guides to help user get started.
   - Simple to understand even if user are new to image processing.

5. **Lightweight and Easy to Install**  
   - Pure Python because it is not complicated to setup.
   - Works on Windows, Mac, and Linux.

**Example code processing image using Scikit-image tools**

```
from skimage import io, filters, feature, exposure
import matplotlib.pyplot as plt
import numpy as np

# === Load image ===
image_path = r"C:\Users\USER\cat.png"
image = io.imread(image_path)

# === Remove alpha channel if present ===
if image.shape[-1] == 4:
    image = image[..., :3]

# === Normalize image to [0, 1] for processing ===
image = image / 255.0  # Ensure all values are float between 0 and 1

# === Apply Gaussian blur to color image ===
blurred_image = filters.gaussian(image, sigma=1, channel_axis=-1)

# === Convert to grayscale for edge detection only ===
gray = np.dot(image[..., :3], [0.299, 0.587, 0.114])  # manual grayscale conversion
edges = feature.canny(gray, sigma=1)

# === Create red edge overlay ===
edge_overlay = np.copy(image)
edge_overlay[edges] = [1, 0, 0]  # red edges

# === Apply histogram equalization to each color channel ===
equalized_image = np.zeros_like(image)
for i in range(3):  # R, G, B channels
    equalized_image[..., i] = exposure.equalize_hist(image[..., i])

# === Plot everything ===
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
ax = axes.ravel()

# 1. Original
ax[0].imshow(image)
ax[0].set_title("Original Image")

# 2. Gaussian Blur (color)
ax[1].imshow(blurred_image)
ax[1].set_title("Gaussian Blur")

# 3. Edge Overlay (in red)
ax[2].imshow(edge_overlay)
ax[2].set_title("Canny Edges (Red Overlay)")

# 4. Histogram Equalization (color-enhanced)
ax[3].imshow(equalized_image)
ax[3].set_title("Histogram Equalization")

# 5. Optional: Side-by-side (Blur + Edges)
combined = 0.5 * blurred_image + 0.5 * edge_overlay
ax[4].imshow(np.clip(combined, 0, 1))
ax[4].set_title("Blur + Edges Combo")

# 6. Empty
ax[5].axis('off')

# Hide axes
for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
```

**Output**


<img width="959" alt="image" src="https://github.com/user-attachments/assets/bdb36fc4-cf6e-422e-aad0-4e065e876a3b" />


