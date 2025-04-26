NAME : MAU'IZOH BINTI ASRUL HADI

STUDENT ID : 2023298852

CLASS : CDCS2554A
## TITLE : INTRODUCTION TO IMAGE PROCESSING USING SCIPY IN PYTHON
### What is Image Processing ?
Image processing refers to the process of manipulating and enhancing digital images. Using computer algorithms, it is mainly applied to extract useful information, improve image quality and prepare images for future use. It plays a crucial role in various industries, such as security systems where it is used for facial recognition. This highlights how image processing has become an essential tool in both current and future world. 

![scipy-bids-project-banners-template-ob-people-1 5-1-ratio-rectangle](https://github.com/user-attachments/assets/2bb4894c-5e72-408e-9450-7ad0eb23dd58)
### What is SciPy ?
SciPy is a free and open-source library in Python that is built on top of Numpy. It is widely used for scientific and technical computing, including multidimensional image processing. This library extends Python's capabilities by offering high-level functions and classes that are especially useful for data analysis, scientific computation, and image processing tasks. In the context of image processing, SciPy provides tools that are both powerful and accessible, making it an excellent choice for researchers, developers, and engineers working with multidimensional image data.
### Significance of SciPy
- **Free and open-source**: Making it accessible for everyone which is beneficial for image processing where experimentation and frequent testing are required without having to pay any license fees.
- **Enable various operations**: An extensive range of functions are available for image processing tasks which are essential for enhancing, analyzing, and preparing images for further use.
- **Plays critical role**: Widely used among the scientific and engineering community that is heavily relying on image-based data, specifically medical imaging like MRI scans.
- **Extend Python capabilities**: Python does not include specialized image manipulation tools by default. When using modules in SciPy like scipy.ndimage, it expands Python’s funtionality and enables users to analyze multidimensional image data accurately and easily.
- **User-friendly**: Designed to be beginner-friendly, especially for people who are already familiar with NumPy or even for users who are unfamiliar with image processing since its clear syntax and well-documented capabilities make it simple to understand and use.
### Library Related to SciPy
Even though SciPy’s module has powerful image processing capabilities, it mainly depends on **NumPy** for array manipulation, with all of NumPy’s functions included in it . In addition, **skimage** is usually used together to load the image and convert it into 8-bit unsigned integers, which is a proper format for image processing. Moreover, to view the processed images, it is necessary to use external libraries such as **Matplotlib**. Hence, SciPy is often used with other libraries to create a comprehensive workflow for image processing.
### Module / Subpackage
SciPy offers a specifically designed module for image processing and analysis functions, which called .ndimage. This subpackage provide variety of functions including linear and non-linear filtering, object measurements, interpolation and binary morphology. Below are some of basic image processing functions : 
1) gaussian_filter(input, sigma[, order, ...])
3) sobel(input[, axis, output, mode, cval])
4) grey_dilation(input[, size, footprint, ...])
5) maximum_position(input[, labels, index])
6) minimum_position(input[, labels, index])
### Integrated Development Environment (IDE)
![images](https://github.com/user-attachments/assets/32ccb994-634d-4d1a-a56b-0a7faa691361)

When it comes to selecting an editor or IDE for image processing tasks using SciPy, the choice ultimately depends on personal preference, project size, and the features you need. In this article, we use **Spyder**, which is designed for scientific computing with built-in support for SciPy, NumPy, and Matplotlib, making it ideal for image processing.
### Python Code Example for Basic Image Processing with SciPy
Coding below shows the use of some functions that has been listed before which is gaussian filter, sobel, grey dilation : 
``` py
from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

# Importing image
img = img_as_ubyte(io.imread("Downloads/fruits.png", as_gray=True))

# Applying Gaussian filter
gaussian_filtered = ndimage.gaussian_filter(img, sigma=2)

# Applying Sobel filter for edge detection
sobel_x = ndimage.sobel(img, axis=0) # Vertical direction.
sobel_y = ndimage.sobel(img, axis=1) # Horizontal direction.
sobel_combined = np.hypot(sobel_x, sobel_y) # Combine

# Applying Grey Dilation
dilated_img = ndimage.grey_dilation(img, size=(15, 15))

# Plotting the results
plt.figure(figsize=(20, 6))

# Original picture
plt.subplot(1, 6, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')

# Gaussian Filtered picture
plt.subplot(1, 6, 2)
plt.title("Gaussian Blurred")
plt.imshow(gaussian_filtered, cmap='gray')

# Sobel Fitered / Edge Detection picture
plt.subplot(1, 6, 3)
plt.title("Sobel Edge Detection X")
plt.imshow(sobel_x, cmap='gray')

plt.subplot(1, 6, 4)
plt.title("Sobel Edge Detection Y")
plt.imshow(sobel_y, cmap='gray')

plt.subplot(1, 6, 5)
plt.title("Sobel Edge Detection Combined")
plt.imshow(sobel_combined, cmap='gray')

# Grey Dilation picture
plt.subplot(1, 6, 6)
plt.title("Grey Dilation")
plt.imshow(dilated_img, cmap='gray')

plt.tight_layout()
plt.show()
```



