## NAME: FATIN AIDA BINTI OTHMAN
## STUDENT NO: 2023406298
## CLASS: M3CS2554A
## TITLE: IMAGE PROCESSING USING SCIKIT-IMAGE

Objective
To write an article about Image Processing using SCIKIT-IMAGE tools
To demonstrate the coding and functions used in SCIKIT-IMAGE related to the topic.

Introduction to Image Processing

Image processing involves enhancing and analyzing digital images through algorithmic and mathematical techniques. The scikit-image library in Python offers a wide range of tools for image preprocessing, analysis, and visualization. It is widely used in practical applications such as industrial inspection, surveillance, and medical imaging, reflecting its growing relevance in fields like computer vision and machine learning.

What is SCIKIT-IMAGES ?

Scikit-image (also known as skimage) is one of the open-source image-processing libraries for the Python programming language. It provides a powerful toolbox of algorithms and functions for various image processing and computer vision tasks and it is built on top of popular scientific libraries like NumPy and SciPy.ndimage. Scikit-image also known image processing Python package that works with NumPy arrays which is a collection of algorithms for image processing.

Feature of SCIKIT-IMAGES:

1. Open-source and free:  Available at no cost and without usage restrictions.
2. Supports many image formats: Can read and write JPEG, PNG, TIFF, and more.
3. Uses NumPy arrays: Images are stored as NumPy `ndarray`, so you can use NumPy functions to manipulate them.
4. Provides many image processing tools: Functions for filtering, segmentation, feature extraction and morphological operations
5. Easy to use: Beginner-friendly and consistent API.


EXAMPLE CODE 
'''from skimage import io, color, filters, feature, exposure
import matplotlib.pyplot as plt

# === Load image from file ===
image_path = r"C:\Users\USER\cat.png"  # Use raw string to handle Windows paths
image = io.imread(image_path)

# === Fix: Remove alpha channel if present (RGBA → RGB) ===
if image.shape[-1] == 4:
    image = image[..., :3]

# === Convert to grayscale ===
gray_image = color.rgb2gray(image)

# === Apply Gaussian blur to reduce noise ===
blurred_image = filters.gaussian(gray_image, sigma=1)

# === Detect edges using Canny edge detection ===
edges = feature.canny(blurred_image, sigma=1)

# === Enhance contrast using histogram equalization ===
equalized_image = exposure.equalize_hist(gray_image)

# === Plot all images ===
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title("Original Image")

ax[1].imshow(gray_image, cmap='gray')
ax[1].set_title("Grayscale")

ax[2].imshow(blurred_image, cmap='gray')
ax[2].set_title("Gaussian Blur")

ax[3].imshow(edges, cmap='gray')
ax[3].set_title("Canny Edges")

ax[4].imshow(equalized_image, cmap='gray')
ax[4].set_title("Histogram Equalization")

# Leave the last subplot blank
ax[5].axis('off')

# Remove axes ticks
for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()'''




