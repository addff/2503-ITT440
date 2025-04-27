### SITI NURZURAIDAH BINTI MA ZALAM @ MAZLAN
### 2023260808
### CDCS2554B

# Image Processing using OpenCV

## **INTRODUCTION**

Image processing is the process of converting an image into a digital form and conducting a certain operation on it to get the desired result.  The image processing system often sees all pictures as 2D signals when it uses specific signal processing techniques. The tool utilized to do the processing is OpenCV alongside with the help of Matplotlib using Python. 

![opencv](C:\\Users\\Huawei\\Documents\\image\\opencv.png)

OpenCV stands for Open Source Computer Vision Library. It is a popular tool used for many image processing activities such as: 

Changing images: Rotating, resizing and cropping. 
Improving images: Reducing noise, blurring and adjusting contrast. 
Finding features: Detecting edges, shapes and faces. 
Recognizing objects: Spotting items in a picture. 
Understanding computer vision: Tracking objects and detecting movement. 

When using OpenCV, images are usually in BGR (Blue, Green, Red) format, but if to use Matplotlib, it has to be changed to RGB (Red, Green, Blue) format to see correctly.

## **STEP-BY-STEP to perform IMAGE PROCESSING**

1. Install OpenCV and Matplotlib

   Open command prompt and enter the command

   `pip install opencv-python matplotlib`

2. Prepare a folder that contains images
   Make sure the pictures are in formats that work like JPEG, PNG or BMP.

   Example: `xukai.jgp`

3. Create the new file in OpenCV in order to:
   - write the codes for image processing.
   - upload the image.
   - display the result from the process
   - saves the program  
**ORIGINAL IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read and convert image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw image
ax.imshow(image)

# Hide axes
ax.axis('off')

# Set title
ax.set_title('Original Image')

# Display the result
plt.show()'
```

**RESULT**

**RGB CHANNEL IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read the image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')

# Convert image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

# Draw image
axs[0].imshow(image_rgb[:, :, 0], cmap='Reds')
axs[1].imshow(image_rgb[:, :, 1], cmap='Greens')
axs[2].imshow(image_rgb[:, :, 2], cmap='Blues')

# Hide axes
for ax in axs:
    ax.axis('off')

# Set titles
axs[0].set_title('Red channel')
axs[1].set_title('Green channel')
axs[2].set_title('Blue channel')

# Display the result
plt.show()
```
**RESULT**

**BLACK and WHITE IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read and convert image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw image
ax.imshow(image, cmap='gray')

# Hide axes
ax.axis('off')

# Set title
ax.set_title('Gray')

# Display the result
plt.show()
```
**RESULT**

**SHARP IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read and convert image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Sharp the image
kernel_sharpening = plt.array ([[-1,-1,-1],
			     [-1,9,-1],
			     [-1,-1,-1]])
sharpened = cv2.filter2D(image,-1, kernel_sharpening)

# Create subplot
fig, ax=plt.subplots(figsize=(6,6))

# Dram image
ax.imshow(sharpened)

# Hide axes
ax.axis ('off')

# Set title
ax.set_title ('Sharpened')

# Display result
plt.show()
```
**RESULT**

**BLUR IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read and convert image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Blur image
kernel_3x3=plt.ones((3,3),plt.float32)/5 
blurred=cv2.filter2D(image, -1, kernel_3x3)

# Create subplot
fig, ax=plt.subplots(figsize=(6,6))

# Dram image
ax.imshow(blurred)

# Hide axes
ax.axis ('off')

# Set title
ax.set_title ('Blurred')

# Display result
plt.show()
```
**RESULT**

