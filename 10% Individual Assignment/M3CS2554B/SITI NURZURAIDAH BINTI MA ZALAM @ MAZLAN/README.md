# SITI NURZURAIDAH BINTI MA ZALAM @ MAZLAN
### Image Processing using OpenCV

**INTRODUCTION**

Image processing is the process of converting an image into a digital form and conducting a certain operation on it to get the desired result.  The image processing system often sees all pictures as 2D signals when it uses specific signal processing techniques. The tool utilized to do the processing is OpenCV alongside with the help of Matplotlib using Python. 

![opencv](C:\\Users\\Huawei\\Documents\\image\\opencv.png)

OpenCV stands for Open Source Computer Vision Library. It is a popular tool used for many image processing activities such as: 

Changing images: Rotating, resizing and cropping. 
Improving images: Reducing noise, blurring and adjusting contrast. 
Finding features: Detecting edges, shapes and faces. 
Recognizing objects: Spotting items in a picture. 
Understanding computer vision: Tracking objects and detecting movement. 

When using OpenCV, images are usually in BGR (Blue, Green, Red) format, but if to use Matplotlib, it has to be changed to RGB (Red, Green, Blue) format to see correctly.

**STEP-BY-STEP to perform IMAGE PROCESSING**

Install OpenCV and Matplotlib

Open command prompt and enter the command
![cmd](C://Users//Huawei//Pictures//Screenshots//cmd.png)

Prepare a folder that contains images
Make sure the pictures are in formats that work like JPEG, PNG or BMP.
Example: 
Create the new file in OpenCV in order to:
write the codes for image processing.
upload the image.
display the result from the process
Saves the program

**ORIGINAL IMAGE**
**INPUT**

'import cv2
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
