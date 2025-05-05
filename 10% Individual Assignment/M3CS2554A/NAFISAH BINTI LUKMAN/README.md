# NAME : AMER HAFIZ BIN AZMAN
# STUDENT ID : 2024643642

---

# What is Image Processing?

Image processing refers to the manipulation or analysis of images to enhance them or extract useful information. Typical tasks include:

- *Image enhancement* (contrast adjustment, noise removal)
- *Image filtering* (blurring, sharpening)
- *Edge detection*
- *Segmentation* (object detection and boundary identification)
- *Morphological operations* (dilation, erosion)

---

# Image Processing Using Mahotas
![Image](https://github.com/user-attachments/assets/2c0ea612-b95f-4715-b439-3d779334f528)

Image processing is an essential technique in various industries such as medical imaging, remote sensing, and computer vision. Among the many tools available for image processing, *Mahotas* stands out due to its simplicity, speed, and seamless integration with the Python programming language. Developed in C++ for performance and callable from Python for ease of use, Mahotas offers a rich set of functions suitable for both basic and advanced image processing tasks.

---

# Why Mahotas?

Mahotas is a fast computer vision and image processing library for Python, with all heavy computation implemented in C++ for speed. It is particularly effective for:

- *High-speed processing*: Optimized using C++, achieving excellent performance for large images.
- *Ease of use*: Python API makes it simple to integrate into data science and engineering workflows.
- *Rich functionality*: Offers over 100 functions including image filtering, morphological operations, feature extraction, and more.
- *Minimal dependencies*: Only relies on NumPy, making it lightweight compared to other libraries.

---

# Key Functions in Mahotas for Image Processing

Here are some commonly used Mahotas functions:

- mahotas.imread() – Read an image from a file.
- mahotas.imsave() – Save an image to a file.
- mahotas.gaussian_filter() – Apply a Gaussian blur to an image.
- mahotas.sobel() – Perform edge detection using the Sobel operator.
- mahotas.thresholding.otsu() – Automatically determine an optimal threshold.
- mahotas.label() – Label connected components in binary images.

---

# How To Install Mahotas?

Here are the step to install Mahotas in your Laptop/PC

1) Go to Anaconda website (https://www.anaconda.com/download) and enter your email. The download link will be sent in your email
  ![Image](https://github.com/user-attachments/assets/ef4904de-e888-4215-98e8-0f435ea372fc)
  
2) Click "Download Now". After finish download Anaconda, lunch it
  ![Image](https://github.com/user-attachments/assets/0613a50e-f8c4-4489-b6bf-5fe62cf6abff)
  
3) Click "Lunch" at Jupyter Notebook. It will open a new tab on your browser
  ![Image](https://github.com/user-attachments/assets/5734c263-ad08-4d33-ac81-e6b5b01abd60)
  
4) Click "New" and after that click "Python". It will open a new tab in your browser
  ![Image](https://github.com/user-attachments/assets/3701b206-f576-4387-a4d2-911ae1d67e84)
  
  
5) Write "!pip install mahotas" in the prompt box and your Mahotas is ready to use after the download finish.
  ![Image](https://github.com/user-attachments/assets/55c3f5a5-5efc-4afa-b04e-01977dc7ab4b)

---

# Example Coding with Mahotas

```python
# Example: Simple Edge Detection
import mahotas
import mahotas.demos
import numpy as np
import matplotlib.pyplot as plt

# Load an example image
image = mahotas.demos.load('nuclear')

# Convert to grayscale if necessary
if len(image.shape) == 3:
    image = np.mean(image, axis=2)

# Apply Sobel edge detection
edges = mahotas.sobel(image)

# Display the result
plt.figure(figsize=(10,5))
plt.subplot(1,2,1) 
plt.title('Original Image') 
plt.imshow(image, cmap='gray') 
plt.axis('off')

plt.subplot(1,2,2) 
plt.title('Edge Detection with Sobel') 
plt.imshow(edges, cmap='gray') 
plt.axis('off')

plt.show()
```

---


# Applications of Image Processing with Mahotas

- *Medical Imaging*: Pre-processing MRI, CT scans, and other medical images.
- *Industrial Inspection*: Detecting defects in manufacturing processes.
- *Remote Sensing*: Enhancing satellite images and analyzing terrain data.
- *Document Processing*: Binarization and feature extraction from scanned documents.
- *Scientific Research*: Feature extraction in biological imaging (e.g., cell analysis).

---

# Real World Applications of Image Processing
In the real world, image processing technologies like those powered by Mahotas are used in many industries:

- *Healthcare*: Medical institutions use image processing to improve diagnostic accuracy. Techniques like MRI enhancement and tumor detection rely heavily on image filtering and segmentation.
- *Manufacturing*: Automated quality control systems capture product images and use image processing to detect defects or assembly errors in real-time.
- *Agriculture*: Drones equipped with cameras capture crop images, and image processing is used to assess plant health, detect disease, and optimize irrigation.
- *Automotive Industry*: Advanced Driver Assistance Systems (ADAS) process camera images to detect lanes, pedestrians, and obstacles to support safe driving.
- *Security and Surveillance*: Motion detection, facial recognition, and abnormal event detection in CCTV systems are powered by computer vision and image processing.
- *Space Exploration:* NASA and other space agencies use image processing for analyzing satellite images, surface mapping, and astronomical imaging.

---

# Conclusion

Mahotas provides a fast, lightweight, and easy-to-use framework for performing image processing tasks in Python. Its C++ backend ensures efficient computation, while its Python interface offers simplicity and flexibility. Whether for academic research, industrial applications, or personal projects, Mahotas is a powerful choice for developers and researchers who need quick and reliable image processing solutions

---

# Here are demonstrate using Mahotas

https://youtu.be/TKKcg88uUUY 
