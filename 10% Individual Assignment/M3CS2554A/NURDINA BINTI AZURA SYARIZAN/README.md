# 2503-ITT440 (10% INDIVIDUAL ASSIGNMENT)

NAME: NURDINA BINTI AZURA SYARIZAN

STUDENT ID: 2023239276

GROUP: M3CS2554A

## TITLE: CVG AND IMAGE PROCESSING WITH PYTHON


### OBJECTIVE
- To write article about CVG and Image Processing using Python tools or library.
- To demonstrate coding used related to the article.

## LIBRARY: OPENCV
<img src="https://github.com/user-attachments/assets/9b29b3a7-4590-42b1-b614-acf8f2a770ab" width="300" />

### What is OpenCV?

OpenCV (Open Source Computer Vision Library) is an open-source library primarily focused on real-time image processing and computer vision tasks. Originally developed by Intel, OpenCV has since grown into one of the most widely used libraries in computer vision and AI. With OpenCV, developers can easily manipulate images, detect objects, track movements, apply filters, and even build complex machine learning and AI systems with visual capabilities.

Whether you're building advanced systems like facial recognition, object tracking, or simpler image transformations such as rotating or scaling, OpenCV is a tool you can't overlook. Its ability to handle both simple and complex tasks with ease has made it the go-to library in the field of computer vision.

#### Key Features
- Image transformation: OpenCV provides an array of functions to manipulate images, such as resizing, cropping, rotating, and flipping. This makes it ideal for adapting images for different uses or performing basic editing tasks
  
- Object detection: Through Haar cascade classifiers, OpenCV enables real-time face, eye, and body detection. This allows developers to build applications such as security systems or face recognition software.
  
- Color filtering: Convert RGB to HSV, grayscale, allowing users to perform operations like color-based segmentation, which is vital for object detection tasks.
  
- Edge detection: Techniques like Canny edge detection and Sobel filters help identify the boundaries within images, making it easier to analyze objects and structures within an image.
  
- Contour Detection: Contours are essential for identifying shapes, boundaries, and blobs in images. OpenCV’s contour detection features are used in a variety of applications, from identifying shapes to image segmentation.
  
- Video Processing: Beyond still images, OpenCV allows the processing of video streams, webcam feeds, and frame-by-frame analysis. This is crucial for applications involving motion analysis or video surveillance.

#### Advantages of OpenCV
***
* __Fast and Efficient__
	* Designed for real-time processing, perfect for time-sensitive applications like live video analysis.
* __Cross-platform__
	* Works on Windows, macOS, Linux, and even mobile (Android/iOS).
* __Python-friendly__
	* Easy to integrate with other Python libraries like NumPy, TensorFlow, PyTorch, etc.
* __Massive Community__
	* Tons of tutorials, forums, and GitHub repos to learn from.
* __Supports AI/ML__
	* You can integrate deep learning models (e.g., YOLO, SSD) directly with OpenCV for object detection and recognition.
* __Free and Open Source__
	* Zero cost, maximum power.

###### Exact code used:
```py
import cv2
import numpy as np

# create a numpy array filled with zeros to use as a blank image
image = np.zeros((512,512,3), np.uint8)

# draw a green line on the image
cv2.line(image, (0,0), (511, 511), (0, 255, 0), 5)

# draw a red rectangle on the image
cv2.rectangle(image, (384,0), (510, 128), (0, 0, 255), 3)

# draw a blue circle on the image
cv2.circle(image, (447,63), 63, (255, 0, 0), -1)

# display the image
cv2.imshow('Image', image)

# wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

```
### SAMPLE OUTPUT
<img src="https://github.com/user-attachments/assets/9b29b3a7-4590-42b1-b614-acf8f2a770ab" width="300" />

----
### DEMO AND INSTALLATION OF PYTHON AND OPENCV
##### Video included below: 
[![Video included below](https://img.youtube.com)




