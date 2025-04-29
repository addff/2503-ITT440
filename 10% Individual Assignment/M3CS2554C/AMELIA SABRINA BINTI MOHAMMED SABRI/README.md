# AMELIA SABRINA BINTI MOHAMMED SABRI
## Image Processing with Filters using OpenCV
-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈.ᐟ
## 💡 Introduction
Image processing is an essential part of computer vision that focuses on enhancing and transforming images to make them more useful for analysis or artistic effects.
Applying filters to images is one of the simplest and most effective ways to explore image processing.
### Applications of image filtering include:
- Photo editing and enhancement
- Medical image analysis
- Object detection preprocessing
- Artistic effects and augmented reality
- Improving image quality for machine learning tasks

In this project, we use OpenCV, a powerful open-source computer vision library to apply various filters to images such as grayscale, invert, cartoon, fisheye and edges.
## 📍 Core Concepts
- Image Reading: Loading the original images using OpenCV.
- Color Transformations: Changing the color space, like converting to grayscale or inverting colors.
- Smoothing: Blurring the image to remove noise and soften details.
- Stylization: Applying artistic effects such as cartoon or fisheye distortion.
- Edge Detection: Finding and highlighting the boundaries inside an image.
- Visualization: Displaying and saving the filtered images for presentation.
## 🛠️ Tools Used
- OpenCV: Image processing functions and filters.
- NumPy: Handling matrix operations for image manipulation.
- Thonny IDE: A Simple Python environment for writing and running code.
## 📖 Library
<img src="https://github.com/user-attachments/assets/7432de34-33b7-4794-891b-f1bb6b99ad3e" width="150" alt="OpenCV_logo_black svg">

OpenCV (Open Source Computer Vision Library) is a free and popular open-source library for computer vision and image processing tasks.
Developed by Intel, it is widely used in academia, research and industry for building real-time image and video processing systems. OpenCV is fast, efficient and beginner-friendly, especially with Python.
## 📝 Overview
- Type: Image Processing / Computer Vision
- Language: Python
- License: Apache 2.0 License
## ✨ Key Features
1. Color Filters
   - Grayscale (convert to black and white)
   - Invert (reverse the colors)
2. Style Filters
   - Cartoon Effect (simplify image details and edges)
3. Effects Filters
   - Fisheye Distortion (wide-angle lens effect)
   - Edge Detection (highlight object boundaries)
## 🪜 Steps
Step 1: Install OpenCV
```
pip install opencv-python
```
Step 2: Import libraries
```
import cv2
import numpy as np
```
Step 3: Load the images
```
image = cv2.imread('image1.jpg')
```
Step 4: Check if images are loaded successfully
```
if image is None:
    print("Error: Image not loaded properly. ")
    exit()
```
Step 5: Define filter functions
```
# Grayscale Filter
def apply_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert Filter
def apply_invert(img):
    return cv2.bitwise_not(img)

# Brightness Increase Filter
def apply_brighter(image, value=50):
    brighter_image = cv2.convertScaleAbs(image, alpha=1, beta=value)
    return brighter_image

# Edges Filter
def apply_edges(img):
    return cv2.Canny(img, 100, 200)
```
Step 6: Apply filters to the image
```
gray_image = apply_grayscale(image)
inverted_image = apply_invert(image)
brightness_image = apply_brighter(image)
edges_image = apply_edges(image)
```
Step 7: Display the filtered images
```
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Inverted Image', inverted_image)
cv2.imshow('Brightness Image', brightness_image)
cv2.imshow('Edges Image', edges_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
## ▶ Final Code
```
import cv2
import numpy as np

image = cv2.imread('image1.jpg')

if image is None:
    print("Error: Image not loaded properly. ")
    exit()

# Grayscale Filter
def apply_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert Filter
def apply_invert(img):
    return cv2.bitwise_not(img)

# Brightness Increase Filter
def apply_brighter(image, value=50):
    brighter_image = cv2.convertScaleAbs(image, alpha=1, beta=value)
    return brighter_image

# Edges Filter
def apply_edges(img):
    return cv2.Canny(img, 100, 200)

gray_image = apply_grayscale(image)
inverted_image = apply_invert(image)
brightness_image = apply_brighter(image)
edges_image = apply_edges(image)

cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Inverted Image', inverted_image)
cv2.imshow('Brightness Image', brightness_image)
cv2.imshow('Edges Image', edges_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
## 🔎 Output Preview
Original Image:  
<img src="https://github.com/user-attachments/assets/2c4f2615-083b-4c36-85a8-7d2b94bccb07" width="150" alt="Original Image">

Grayscale Filter:  
<img src="https://github.com/user-attachments/assets/0ef30593-2e81-4818-be81-2fe2fb6c110d" width="150" alt="Grayscale Filter">

Inverted Filter:  
<img src="https://github.com/user-attachments/assets/55fb7579-269c-4b16-9e7d-025e46da18e5" width="150" alt="Inverted Filter">

Brightness Filter:  
<img src="https://github.com/user-attachments/assets/3085ea31-0f30-4a4d-929e-8f01e722015e" width="150" alt="Brightness Filter">

Edges Filter:  
<img src="https://github.com/user-attachments/assets/117c0a17-4f50-45bf-81e9-b8d3f2b8614a" width="150" alt="Edges Filter">

## 🎥 Video Demonstration
## 🧠 Conclusion
In this assignment, I learned:
- How to apply basic image processing filters using OpenCV such as grayscale, invert, edge detection and brightness adjustment.
- How image data is stored and manipulated as arrays using NumPy, allowing direct control over pixel values.
- How different filters can highlight or transform features in an image for analysis or visual effect.
- How OpenCV functions like cvtColor(), bitwise_not(), convertScaleAbs(), and Canny() work and how to use them in real-world image filtering tasks.


-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈.ᐟ




