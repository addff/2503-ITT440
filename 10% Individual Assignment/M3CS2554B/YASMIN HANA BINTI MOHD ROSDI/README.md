Name :  YASMIN HANA BINTI MOHD ROSDI 

GROUP: M3CDCS2554B

SUBJECT: ITT440

# OPENCV : A POWERFUL COMPUTER VISION LIBRARY

## :brain: What is computer vision?

Computer vision is a field of artificial intelligence that focuses on extracting information from input images or videos. It involves teaching computers to interpret visuals and understand visual data, allowing them make predictions or decisions based on what they **"see"** similar to how humans perceive the world. 


## :memo: The role OpenCV plays in making computer vision accessible in Python.

OpenCV plays an important role in computer vision as an open-source library for computer vision. Thanks to its open-source functionality, researchers and developers are allowed to collaborate, expand its functionality and apply computer vison algorithm across a wide range of fields. The python bindings make OpenCV especially user-friendly for beginners who are interested in exploring the vast world of computer vision. By simply importing the python interface `cv2` , developers can access powerful tools with clean, readable code to use the tools with ease and readable code. This ease of use makes computer vision techniques more approachable, even for those without deep experience in the field. 

## 🌐 Why OpenCV is still relevant in modern CV applications.

First launched in 1999 at Intel by Gary Bradsky. Since then, OpenCV has played a major role in the fields of computer vision and continues to be widely used today. 
With its extensive set of tools, OpenCV has become a go-to library for developers working in image processing and computer vision. It also provides a seamless integration with other popular libraries and frameworks such as numPy, TensorFlow and more. The compatibility makes OpenCV incredibly versatile, allowing it to constantly evolve alongside the fast-paced innovations of the global tech company.


## 🧪 Simple tutorial on using the tools in <ins>OpenCV</ins> to implement computer vision 
+ The tutorial goal is to remove the background of the image
+ The tutorial highlights one of the elements of computer vision - <ins>Segmentation</ins> that analyze and separate the object (in tis case: person) from the background.

```
python

#import opencv
import cv2

#import numpy
import numpy as np

#Load the image (from the specified file)
image = cv2.imread(r'image_path')

#Convert to HSV color space (good for color and object detection)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Define blue color range in HSV
#lower limit of blue
lower_blue = np.array([90, 50, 50])  
#upper limit of blue
upper_blue = np.array([130, 255, 255])  

#Create a mask for blue areas
mask = cv2.inRange(hsv, lower_blue, upper_blue) 

#Invert the mask: foreground (not blue) = white
mask_inv = cv2.bitwise_not(mask)

#Create 4-channel image (BGRA)
b, g, r = cv2.split(image)

#alpha will be 255 for object, 0 for background
alpha = mask_inv  

#merge all the channels 
result = cv2.merge([b, g, r, alpha])

#save the new image
output_path = 'output_no_blue_background.png'
cv2.imwrite(output_path, result)
cv2.imshow('Result', result)
```

>[!Note]
>The code is specifically for removing blue background from images only!

Click [here](https://youtu.be/phayb3zSE24) to see the demonstration clearly!

**Computer Vison element from the video:**
+ 

## 🥇 Why use OpenCV for computer vision?
+ fast performance
+ rich algorithm library
+ easy integration with deep learning





