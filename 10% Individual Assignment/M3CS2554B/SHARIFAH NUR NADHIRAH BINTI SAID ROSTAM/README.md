# SHARIFAH NUR NADHIRAH BINTI SAID ROSTAM
# M3CS2554B
## ITT440 - 10% Individual Assignment
# Image Manipulation with NumPy: Basic Operations and Transformations
#### Overview
This project demonstrates how to perform simple image processing tasks using only **NumPy**. It is ideal for understanding how row image data can be manipulated with array-based logic - a foundational concept in computer vision and image processing.
![NumPy Logo](https://github.com/user-attachments/assets/f17d4a63-b2c1-42ea-a5bb-9c53044f8956)
#### Introduction
Image processing is a core in computer vision, involving techniques to manipulate images to extract useful information or modify visual attributes.While other libraries like OpenCV and PIL are often used, NumPy offers a powerful low-level approach by treating image as arrays. NumPy stands for Numerical Python. It is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourirer transform and matrices.
#### Why Numpy for Image Processing?
- **Efficiency**: NumPy can perform a fast array processing due to the highly optimized numerical operations.
- **Simplicity**: It allows direct manipulation of pixel values.
- **Control**: Offers more transparency than using high-level libraries.
#### Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python but most of the parts that require fast computation are written in C or C++.
#### Step-by-step Implementation
#### Tools and Libraries Used
- **Python 3.x**
- **NumPy** – for matrix manipulation.
- **OpenCV** – for loading/saving/displaying images.
- **Matplotlib** – for visualization in Jupyter or Python scripts.
The dependencies was included to visualize the results clearly.
#### Dependencies Summary

This project uses three essential Python libraries — each one handling a different part of the workflow:

| Library         | Purpose                               | Why It's Needed |
|----------------|----------------------------------------|------------------|
| **NumPy**       | Image manipulation using arrays        | Performs all pixel-level operations like grayscale conversion, cropping, and inversion |
| **OpenCV**      | Reading, writing, and color conversion | Loads real images, converts BGR to RGB, and saves processed images |
| **Matplotlib**  | To visualize the image output          | Displays images inline or in pop-up windows using subplots |

#### Install dependencies using:
```bash
pip install numpy opencv-python matplotlib
```
#### How to Implement?
#### Step 1: Create or Load an Image
A simple image created using NumPy or any image can be loaded using `cv2.imread()`.
```python
img_rgb = np.zeros((200, 200, 3), dtype=np.uint8)
img_rgb[50:150, 50:150] = [255, 100, 50]  # Colored square
```
#### Step 2: Grayscale Conversion
Convert the image to grayscale by averaging the Red, Green and Blue.
```python
grayscale = np.mean(img_rgb, axis=2).astype(np.uint8)
```
#### Step 3: Image Conversion
Inverts the image by substracting pixel values from 255.
```python
inverted = 255 - img_rgb
```
#### Step 4: Brightness Enhancement
Increase the image brightness by adding a scalar to all pixel values using `np.clip()` to avoid overflow.
```python
bright = np.clip(img_rgb + 50, 0, 255).astype(np.uint8)
```
#### Step 5: Image Croppig
Crop the center region of the image using slicing.
```python
h, w, _ = img_rgb.shape
cropped = img_rgb[h//4:h*3//4, w//4:w*3//4]
```











