# SHARIFAH NUR NADHIRAH BINTI SAID ROSTAM
# M3CS2554B
## ITT440 - 10% Individual Assignment
# Image Manipulation with NumPy: Basic Operations and Transformations
#### Overview
This project demonstrates how to manipulate image using the **NumPy** library while the **PIL** library wll be used to access the pixel data stored in an image. It is ideal for understanding how row image data can be manipulated with array-based logic - a foundational concept in computer vision and image processing.

![NumPy Logo](https://github.com/user-attachments/assets/f17d4a63-b2c1-42ea-a5bb-9c53044f8956)
#### Introduction
Image processing is a type of mathematical computation. It demonstrates core in computer vision, involving techniques to manipulate images to extract useful information or modify visual attributes. NumPy was one of the powerful tools that treat image as arrays. NumPy stands for Numerical Python. It is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourirer transform and matrices.
#### Why Numpy for Image Processing?
- **Efficiency**: A fast array can be processed with NumPy due to its highly optimized numerical operations. 
- **Simplicity**: A direct manipulation of pixel values can be allowed. 
- **Control**: NumPy offers more transparency compared to other high-level libraries.
#### Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python but most of the parts that require fast computation are written in C or C++.

#### Step-by-step Implementation

#### Step 1: Environment Setup
The following tools need to be installed to perform this project
- Python 3.8+
- Python Packages: PIL, NumPy

  
#### Step 2: Import Image 
```
import numpy as np

#Use PIL to access image data
from PIL import Image
img = Image.open('monalisa.jpg')

#Create array from image data 
M = np.array(img)

#Display array from image data 
display(Image.fromarray(M))
```

The results:

![image](https://github.com/user-attachments/assets/df822af8-e50f-44ff-b2d1-2d744e7d240a)


#### Step 3: Rotate Image

```
def rotate_image (image, n):
  # rotate image using rot90, use n to determine number of rotation 
  rotated_img = Image.fromarray(np.rot90(image, k=n, axes=(1, 0)))
  return rotated_img

#rotate image twice (n=2)
display(rotate_image(reduced_M, 2))
```

The results:

![image](https://github.com/user-attachments/assets/d9fcc465-6c19-4a8c-a3e6-3e1d60936366)

#### Step 4: Crop an Image
```
def crop_image(image, crop_ratio, zoom_ratio):

  #create focused part using crop_ratio and zoom_ratio of choice
  
  top = image.shape[0] // crop_ratio 
  bottom = zoom_ratio * image.shape[0] // crop_ratio
  left = image.shape[1] // crop_ratio
  right = zoom_ratio * image.shape[1] // crop_ratio

  # Extract the focused part using array slicing
  focused_part = image[top:bottom, left:right]
  return focused_part

display(crop_image(reduced_M, 4, 2))
```

The results:

![image](https://github.com/user-attachments/assets/744da381-84f7-4001-a347-4a6a0a5de391)

#### Step 5: Binarize Image
```
def binarize_image(image, threshold):

  #set pixel value greater than threshold to 255
  binarize_image = ((image > threshold) * 255).astype(np.uint8)
  
  return binarize_image

#set threshold
threshold = 68

M_binarized = Image.fromarray(binarize_image(reduced_M, threshold))

display(M_binarized)
```

The results:

![image](https://github.com/user-attachments/assets/e4d95688-7349-430f-a89c-ca1557c0b7d7)

#### Step 6: Grayscale Image
```
import numpy as np

def grayscale(image):
    # Convert the RGB image to grayscale using weighted average
    grayscale_img = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

    # Ensure values are within valid range [0, 255]
    grayscale_img = np.clip(grayscale_img, 0, 255)

    # Convert to uint8 data type
    grayscale_img = grayscale_img.astype(np.uint8)

    return grayscale_img

# Convert the image to grayscale
M_gray = grayscale(reduced_M)

display(M_gray)
```

The results:

![image](https://github.com/user-attachments/assets/04ea948a-32ad-44bb-8d39-3409c4358301)































