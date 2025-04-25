# 2503-ITT440 (10% INDIVIDUAL ASSIGNMENT)

## NURDINA BINTI AZURA SYARIZAN (2023239276 | M3CS2554A)

## TITLE: CVG AND IMAGE PROCESSING WITH PYTHON


### OBJECTIVE
- To write article about CVG and Image Processing using Python tools or library.
- To demonstrate coding used related to the article.

### Editor: Notepad ++


![notepad++](https://github.com/----)

Notepad++ is a popular and free source code editor and text editor for Windows. It was developed by Don Ho and is distributed under the GNU General Public License. Notepad++ is known for its user-friendly interface and its extensive support for various programming languages and file formats.


###### Significance Of Notepad++ :

- Free and Open Source: Notepad++ is free to use, and its open-source nature means that its source code is publicly available. This transparency allows users to inspect and modify the software, as well as contribute to its development.

- Lightweight: Notepad++ is a lightweight application, which means it doesn't consume a significant amount of system resources. It loads quickly and runs smoothly even on older or less powerful computers.

- Extensible: Notepad++ supports a wide range of plugins that can be used to enhance its functionality. This extensibility allows users to add features and capabilities as needed.

- Multi-Language Support: It supports a wide variety of languages and character encodings, making it a versatile choice for users around the world.

- Community and Support: It has a strong and active user community, which means you can find help, tutorials, and plugins created by other users to extend its functionality.


## LIBRARY: OPENCV
<img src="https://github.com/user-attachments/assets/9b29b3a7-4590-42b1-b614-acf8f2a770ab" width="300" />


### What is OpenCV?

OpenCV (Open Source Computer Vision Library) is a powerful open-source Python library focused on real-time image processing and computer vision tasks. It was originally developed by Intel and has become a standard in the CV community.
With OpenCV, you can easily manipulate images, detect objects, track movements, apply filters, and even power up AI models with vision capabilities. Whether you're building facial recognition systems or just playing around with filters like Snapchat, OpenCV is your go-to library!

#### Key Features
- Image transformation: Resizing, cropping, rotating, flipping.
- Object detection: Face, eyes, body detection using pretrained Haar cascade models.
- Color filtering: Convert RGB to HSV, grayscale.
- Edge detection: Canny edge detection, Sobel filters.
- Contour Detection: Useful for detecting shapes, outlines, and blobs.
- Video Processing: Reading and writing videos, webcam feeds, frame-by-frame manipulation.

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
import matplotlib.pyplot as plt

# Load the image using OpenCV
image = cv2.imread("example.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Resize the image to 256x256
resized_image = cv2.resize(image, (256, 256))

# Flip the image horizontally (mirror effect)
flipped_image = cv2.flip(resized_image, 1)

# Adjust brightness and contrast
alpha = 1.2  # Contrast (1.0 = normal)
beta = 30    # Brightness (0 = no change)
bright_contrast_image = cv2.convertScaleAbs(flipped_image, alpha=alpha, beta=beta)

# Rotate the image by 15 degrees
(h, w) = bright_contrast_image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 15, 1.0)
rotated_image = cv2.warpAffine(bright_contrast_image, rotation_matrix, (w, h))

# Display the final image using matplotlib
plt.imshow(rotated_image)
plt.title("Augmented Image (OpenCV Only)")
plt.axis('off')
plt.show()




### DEMONSTRATION OF INSTALLATION AND HOW TO USE OPENCV


