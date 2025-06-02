# MUHAMMAD ALIFF LUQMAN BIN MOHD SABRI (2024745785)
### ITT440 - Individual Assignment
# Image Processing Using SciPy
![image](https://github.com/user-attachments/assets/9e7fc749-caa9-410c-b6d2-82ea21180dc8)


## Introduction

SciPy is a scientific computing library in Python, built on top of NumPy. While it’s not primarily an image processing library, its `scipy.ndimage` module provides powerful functions for image manipulation. It’s ideal for tasks like filtering, transforming, and basic analysis of images. SciPy's image processing capabilities are particularly well-suited for scientific and research-oriented tasks—especially in domains such as biology, medicine, astronomy, and engineering where images are often analyzed not just visually but quantitatively.

## Objectives

- Set up SciPy for image processing.
- Load and display images using `matplotlib`.
- Perform basic image operations: rotate, zoom, blur, and edge detection.
- Save the modified images.
- Understand SciPy's position in the scientific Python ecosystem.

## Core Concepts

### Images as NumPy Arrays
- Grayscale: 2D arrays (height x width)
- RGB: 3D arrays (height x width x 3)

### Filters and Convolution Kernels
- Gaussian, Median, Uniform filters
- Sobel, Laplace for edge detection

### Geometric Transformations
- Rotate, zoom, shift, crop

### Labeling and Morphological Operations
- `ndimage.label` to identify connected components
- Morphology: erosion, dilation, opening, closing

## 1. Setup the Environment

Install required libraries:

```bash
pip install scipy matplotlib imageio
```

Import them in your script:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import imageio
```

## 2. Load and Display an Image

```python
# Load an image
image = imageio.imread('example.jpg')

# Display the original image
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')
plt.show()
```

## 3. Convert to Grayscale

```python
# Convert to grayscale (if the image is RGB)
if image.ndim == 3:
    gray = np.mean(image, axis=2)
else:
    gray = image

plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()
```

## 4. Rotate the Image

```python
rotated = ndimage.rotate(gray, 45)
plt.imshow(rotated, cmap='gray')
plt.title("Rotated Image (45°)")
plt.axis('off')
plt.show()
```

## 5. Zoom the Image

```python
zoomed = ndimage.zoom(gray, 1.5)  # 150% zoom
plt.imshow(zoomed, cmap='gray')
plt.title("Zoomed Image")
plt.axis('off')
plt.show()
```

## 6. Apply Gaussian Blur

```python
blurred = ndimage.gaussian_filter(gray, sigma=3)
plt.imshow(blurred, cmap='gray')
plt.title("Blurred Image")
plt.axis('off')
plt.show()
```

## 7. Edge Detection (Sobel Filter)

```python
sx = ndimage.sobel(gray, axis=0, mode='reflect')
sy = ndimage.sobel(gray, axis=1, mode='reflect')
sobel_edges = np.hypot(sx, sy)

plt.imshow(sobel_edges, cmap='gray')
plt.title("Sobel Edge Detection")
plt.axis('off')
plt.show()
```

## 8. Save the Processed Image

```python
imageio.imwrite('sobel_edges.jpg', sobel_edges.astype(np.uint8))
```


## Key Functions in `scipy.ndimage`

| Function | Description |
|----------|-------------|
| `rotate()` | Rotates the image by a given angle |
| `zoom()` | Zooms in or out |
| `shift()` | Translates the image |
| `gaussian_filter()` | Applies a Gaussian blur |
| `median_filter()` | Reduces noise |
| `sobel()` | Detects edges along a given axis |
| `label()` | Labels connected regions |
| `binary_erosion()`, `binary_dilation()` | Morphological operations |

## Use Cases

| Field | Use Case |
|--------|----------|
| Microscopy | Cell and bacteria detection |
| Astronomy | Noise reduction, object localization |
| Medical Imaging | Edge enhancement, segmentation |
| Remote Sensing | Texture and land pattern analysis |
| Engineering | Visualization and image-based calculations |



## Conclusion

While SciPy isn’t specialized for image processing like OpenCV, its `ndimage` module is extremely valuable for scientific workflows where images are treated as data arrays. If you’re working with biological data, remote sensing, or scientific research, SciPy is an excellent, efficient tool. SciPy is especially powerful when images are viewed not just as pictures, but as data: arrays of values that can be measured, transformed, and analyzed. This makes it incredibly useful for researchers, data scientists, and engineers working in domains where image data is core to experiments or diagnostics.


