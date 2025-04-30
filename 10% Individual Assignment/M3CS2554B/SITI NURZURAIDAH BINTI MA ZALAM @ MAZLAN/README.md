#### SITI NURZURAIDAH BINTI MA ZALAM @ MAZLAN
#### 2023260808
#### CDCS2554B

# IMAGE PROCESSING USING OPENCV📸

## **INTRODUCTION**

Image processing is the process of converting an image into a digital form and conducting a certain operation on it to get the desired result.  The image processing system often sees all pictures as 2D signals when it uses specific signal processing techniques. The tool utilized to do the processing is OpenCV alongside with the help of Matplotlib using Python. 

![opencv](https://github.com/user-attachments/assets/dd950662-bca0-4562-9a52-da48be435a8f)

OpenCV stands for Open Source Computer Vision Library. It is a popular tool used for many image processing activities **such as**: 

Modifying pictures means turning them, making them bigger or smaller and cutting parts out. Enhancing pictures involves getting rid of unwanted noise, softening them and changing the brightness. Identifying features is about finding lines, forms and faces. Recognizing things is about seeing items in a photo and understanding how computers see includes following objects and noticing movement.

When using **OpenCV**, images are usually in **BGR (Blue, Green, Red) format**, but if to use **Matplotlib**, it has to be changed to **RGB (Red, Green, Blue) format** to see correctly.

## **STEPS to perform IMAGE PROCESSING**

1. Install OpenCV and Matplotlib 🛠️

   Open command prompt and enter the command

   `pip install opencv-python matplotlib`

2. Prepare a folder that contains images

   - Make sure the pictures are in formats that work like JPEG, PNG or BMP.

   - Example:
     
	![xukai](https://github.com/user-attachments/assets/2717d9fb-3804-4457-b2bd-e2dcd8990f0c)

3. Create the new file in OpenCV in order to:
   - write the codes for image processing.
   - upload the image.
   - display the result from the process
   - save the program
## **RGB CHANNEL IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read the image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')

# Convert image
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# create subplots
fig, axs = plt.subplots(1,3,figsize=(10,5))

# Draw image
axs[0].imshow(image_rgb[:,:,0],cmap='Reds')
axs[1].imshow(image_rgb[:,:,1],cmap='Greens')
axs[2].imshow(image_rgb[:,:,2],cmap='Blues')

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
![rgb](https://github.com/user-attachments/assets/710edf62-9f40-418f-a35f-48faca2d2850)

## **GRAY IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read and convert image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Create subplot
fig, ax = plt.subplots(figsize=(8,6))

# Draw image
ax.imshow(image,cmap='gray')

# Hide axes
ax.axis('off')

# Set title
ax.set_title('Gray')

# Display the result
plt.show()
```
**RESULT**

![gray](https://github.com/user-attachments/assets/9df37751-65af-4ba6-a707-a5a98fe8452d)

## **SHARPENED IMAGE**
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
sharpened = cv2.filter2D(image,-1,kernel_sharpening)

# Create subplot
fig,ax=plt.subplots(figsize=(6,6))

# Draw image
ax.imshow(sharpened)

# Hide axes
ax.axis('off')

# Set title
ax.set_title('Sharpened')

# Display the result
plt.show()
```
**RESULT**

![sharp](https://github.com/user-attachments/assets/66bb43f5-b00e-4fe8-b4fc-35635d397c81)

## **BLURRED IMAGE**
**INPUT**
```
import cv2
import matplotlib.pylab as plt

# Read and convert image
image = cv2.imread('C:\\Users\\Huawei\\Documents\\image\\xukai.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Blur image
kernel_3x3=plt.ones((3,3),plt.float32)/5
blurred=cv2.filter2D(image,-1,kernel_3x3)

# Create subplot
fig,ax=plt.subplots(figsize=(6,6))

#Draw image
ax.imshow(blurred)

# Hide axes
ax.axis('off')

# Set title
ax.set_title('Blurred')

# Display the result
plt.show()
```
**RESULT**

![blur](https://github.com/user-attachments/assets/090b4c49-5534-4a81-a0a3-a725f1414db6)

To watch image processing at terminal, click the link below: 

https://youtu.be/Wl0MRtjX658?si=r0zZ18Nl-w-9Kmue

## **SUMMARY**
OpenCV is an amazing tool that helps people work with images. It can do everything from basic changes to really complicated analysis. It is great for making cool visual effects and awesome pictures. OpenCV is not just about images. It can do a lot in different areas. In a nutshell, OpenCV is a free toolkit that helps developers and researchers make smart applications that can use machine learning and understand visual information quickly.
