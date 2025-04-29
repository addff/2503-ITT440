# AMIRAH BINTI TALIB
# ITT440 - INDIVIDUAL ASSIGNMENT

# COLOR MANIPULATING USING SIMPLECV

![SimpleCV_Logo](https://github.com/user-attachments/assets/b686c8d9-feb1-47aa-a57c-d5ad96dcd834 "SimpleCV Logo")

## SIMPLECV
SimpleCV is an open-source framework for building computer vision applications using Python. It provides a simple interface for accessing and processing images and videos, making it ideal for beginners and rapid prototyping. In this tutorial, we will learn to run Color Manipulation with SimpleCV.

### COLOR MANIPULATION
Color Manipulation refers to changing, analyzing, or adjusting the colors in an image to achieve a certain goal, such as finding specific objects, highlighting features, or preparing an image for further processing. 

### Tools and Libraries Used
- **Phyton 3** - Main programming language used to write and run the script.
- **SimpleCV** - Library for color manipulation.
- **OpenCV** - Handle much of the heavy lifting behind SimpleCV's color operations
  
## Steps to Manipulate Color with SimpleCV

### Step 1: Install SimpleCV
```bash
pip install SimpleCV
pip install opencv-python
```
### Step 2: Write python script using notepad
#### Save the script in 'all files' types 

```python
import cv2
import numpy as np

#Step 1: Load the image
img = cv2.imread('ORANG UTAN.jpg')

#Step 2: Convert from BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Step 3: Define range for red color in HSV
lower_red1 = np.array([0,120,70])
upper_red1 = np.array ([10,255,255])

lower_red2 = np.array ([170,120,70])
upper_red2 = np.array ([180,255,255])

#Step 4: Create two masks and combine them
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = mask1 + mask2

#Step 5: Apply the mask to get only red regions
red_output = cv2.bitwise_and(img,img,mask=red_mask)

#Step 6: Highlight red areas with different color (Optional)
#Create a green image
green = np.full_like(img,(0,255,0))

#Apply the green only where red was detected
highlighted = np.where(red_mask[:,:, np.newaxis]==255, green, img)

#Step 7: Show the images
cv2.imshow('Original Images', img)
cv2.imshow('Red Areas Only', red_output)
cv2.imshow ('Red Highlighted Green', highlighted)

#Step 8: Save the output images
cv2.imwrite('Output_red_only.jpg', red_output)
cv2.imwrite('Output_highlighted.jpg', highlighted)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Step 3: Folder
- **i** - Create a folder
- **ii** - Sace python script inside the folder
- **iii** - Save the image that want to color manipulate in the folder

### Step 4: Run the script using python
- **1.** - Open python
- **2.** - Open the script file
- **3.** - Run the file to get output

## SAMPLE IMAGE

### Original Image
![ORANG UTAN](https://github.com/user-attachments/assets/43200466-5326-4fbe-a9bd-29ebd0f3ea0f)

### Red Areas Only Image
![Output_red_only](https://github.com/user-attachments/assets/65ee7659-9609-4b0f-8f0f-2d82946ab4ed)

### Red Highlighted Green
![Output_highlighted](https://github.com/user-attachments/assets/338f26b8-b554-488e-bff7-db742fd80334)

- **Color Space Conversion** - The image is converted from BGR (Blue, Green, Red) to HSV (Hue, Saturation, Value) color space.
- **Red Color Range Definition** - This is necessary because red has a hue that wraps around the color spectrum. Therefore, two separate ranges are used to capture all red hues.
- **Mask Creation** - The code generates two binary masks that represent areas where the image's hue values fall within the red color range. These two masks are combined into one.
- **Highlighting Red Areas** - An optional step is performed where the detected red areas are highlighted in green. This is achieved by replacing the red regions with green pixels.

## CONCLUSION
This project provides valuable insights into color-based image segmentation using OpenCV, specifically for detecting and isolating red areas in an image. It demonstrates essential techniques such as converting color spaces (BGR to HSV), creating masks to filter out specific colors, and applying these masks to extract or highlight desired regions. By highlighting red areas with green, the project showcases how to manipulate images for better analysis and visualization. Overall, this project lays the foundation for more complex computer vision tasks, such as object detection and tracking, by emphasizing the importance of color manipulation and filtering in image processing.

## DEMONSTRATION VIDEO
