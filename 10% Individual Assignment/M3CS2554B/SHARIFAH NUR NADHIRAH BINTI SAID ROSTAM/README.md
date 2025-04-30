#### SHARIFAH NUR NADHIRAH BINTI SAID ROSTAM 2023674486
#### M3CS2554B
#### ITT440 - 10% Individual Assignment
# Image Manipulation with NumPy: Basic Operations and Transformations
### Overview
This project demonstrates how to manipulate image using the **NumPy** library while the **PIL** library wll be used to access the pixel data stored in an image. It is ideal for understanding how row image data can be manipulated with array-based logic - a foundational concept in computer vision and image processing.

![NumPy Logo](https://github.com/user-attachments/assets/f17d4a63-b2c1-42ea-a5bb-9c53044f8956)
### Introduction
Image processing is a type of mathematical computation. It demonstrates core in computer vision, involving techniques to manipulate images to extract useful information or modify visual attributes. NumPy was one of the powerful tools that treat image as arrays. NumPy stands for Numerical Python. It is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourirer transform and matrices.

#### Why Numpy for Image Processing?

- **Efficiency**: A fast array can be processed with NumPy due to its highly optimized numerical operations. 
- **Simplicity**: A direct manipulation of pixel values can be allowed. 
- **Control**: NumPy offers more transparency compared to other high-level libraries.
  
#### Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python but most of the parts that require fast computation are written in C or C++.

### Step-by-step Implementation

#### Step 1: Environment Setup
The following tools need to be installed to perform this project
- Python 3.8+ [Application Installation](https://www.python.org/downloads/release/python-380/)
- Python Packages: PIL, NumPy library in your command prompt

  
#### Step 2: Import and Reduced Image
```
import numpy as np
from PIL import Image
img = Image.open('C:/Users/hp/Downloads/monalisa.jpg')
M = np.array(img)
Image.fromarray(M).show()
reduced_img = img.resize((img.width // 2, img.height // 2))
reduced_M = np.array(reduced_img)
```

#### Step 3: RGB Image
```
def RGB_image(image, image_color):
    if image_color == 'R':
        img_R = image.copy()
        img_R[:, :, (1, 2)] = 0
        return img_R
    elif image_color == 'G':
        img_G = image.copy()
        img_G[:, :, (0, 2)] = 0
        return img_G
    elif image_color == 'B':
        img_B = image.copy()
        img_B[:, :, (0, 1)] = 0
        return img_B
    else:
        raise ValueError("Invalid color. Use 'R', 'G', or 'B'.")

# Show filtered RGB images
Image.fromarray(RGB_image(reduced_M, 'R')).show(title="Red Channel")
Image.fromarray(RGB_image(reduced_M, 'G')).show(title="Green Channel")
Image.fromarray(RGB_image(reduced_M, 'B')).show(title="Blue Channel")
```

#### Step 4: Grayscale Image
```
def grayscale(image):
    grayscale_img = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    grayscale_img = np.clip(grayscale_img, 0, 255).astype(np.uint8)
    return grayscale_img

M_gray = grayscale(reduced_M)
Image.fromarray(M_gray).show(title="Grayscale")
```

#### Step 5: Crop an Image
```
def crop_image(image, crop_ratio, zoom_ratio):
    top = image.shape[0] // crop_ratio 
    bottom = zoom_ratio * image.shape[0] // crop_ratio
    left = image.shape[1] // crop_ratio
    right = zoom_ratio * image.shape[1] // crop_ratio
    focused_part = image[top:bottom, left:right]
    return focused_part

M_cropped = crop_image(reduced_M, 4, 2)
Image.fromarray(M_cropped).show(title="Cropped")
```

#### Step 6: Rotate Image
```
def rotate_image(image, n):
    rotated_img = Image.fromarray(np.rot90(image, k=n, axes=(1, 0)))
    return rotated_img

rotated = rotate_image(reduced_M, 2)
rotated.show(title="Rotated")
```

#### Step 7: Binarize Image
```
def binarize_image(image, threshold):
    binarized = ((image > threshold) * 255).astype(np.uint8)
    return binarized
threshold = 68
M_binarized = binarize_image(M_gray, threshold)
Image.fromarray(M_binarized).show(title="Binarized")
```

Simple Demonstration Using NumPy for Image Processing on YouTube

[Learn How to Use Numpy Here](https://youtu.be/4VK6Rv3i5rk?si=rGZkYNq5uOvJxgGe) 





































