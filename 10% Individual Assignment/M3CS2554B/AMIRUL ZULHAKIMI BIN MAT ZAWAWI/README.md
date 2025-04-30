# NAME : AMIRUL ZULHAKIMI BIN MAT ZAWAWI
# STUDENT ID : 2023298656

---

# Image Processing Using MATLAB
<p align="center">
  <img src="https://github.com/user-attachments/assets/892a55ea-56d5-4f47-91af-9f692787dba4" alt="MATLAB Logo" width="250">
</p>

Image processing has become an integral part of numerous fields including medical imaging, remote sensing, computer vision, and industrial automation. Among the various tools and programming environments available, **MATLAB** stands out as one of the most powerful and widely used platforms for image processing applications. Its comprehensive Image Processing Toolbox and user-friendly interface make it ideal for both beginners and advanced users.

## What is Image Processing?

Image processing refers to the technique of performing operations on an image to enhance it or extract useful information. It involves tasks such as:

- Image enhancement (contrast adjustment, noise removal)
- Image transformation (rotation, scaling, translation)
- Filtering (blurring, sharpening)
- Edge detection
- Segmentation (object detection and boundary identification)
- Morphological operations (dilation, erosion)

## Why MATLAB?

MATLAB (Matrix Laboratory) is a high-level programming language and environment developed by MathWorks. It is specifically designed for numerical computation, visualization, and algorithm development. For image processing, MATLAB offers:

- **Image Processing Toolbox**: A collection of functions and apps for analyzing, preprocessing, and visualizing images.
- **Easy Prototyping**: Users can quickly test algorithms using built-in functions without writing code from scratch.
- **Interactive Apps**: Tools like the Image Segmenter and Color Thresholder help users perform complex tasks visually.
- **Extensive Documentation**: MATLAB provides extensive help and examples, making learning easier.
- **Support for Various File Formats**: It can read and write a wide range of image formats such as JPEG, PNG, TIFF, BMP, etc.

## How to Install Matlab
  
  1. Go to [**mathworks.com**](https://www.mathworks.com)
  2. Create an account.
  3. Download MATLAB from [**mathworks.com/downloads**](https://www.mathworks.com/downloads)
  4. Open the installer and follow the steps.
  5. Activate and start MATLAB.

## Key Functions in MATLAB for Image Processing

Here are some commonly used MATLAB functions for image processing:

- `imread()` – Reads an image file into MATLAB.
- `imshow()` – Displays an image in a figure window.
- `rgb2gray()` – Converts a color image to grayscale.
- `imresize()` – Resizes an image to a specified size.
- `imfilter()` – Applies a filter to an image.
- `edge()` – Detects edges in an image using methods like Sobel, Prewitt, or Canny.
- `bwlabel()` – Labels connected components in a binary image.
- `regionprops()` – Measures properties of labeled regions.

## Example: Simple Edge Detection

```matlab
% Read the image
img = imread('example.jpg');

% Convert to grayscale
grayImg = rgb2gray(img);

% Perform edge detection
edges = edge(grayImg, 'Canny');

% Display the result
imshow(edges);
title('Edge Detection using Canny');
```

## Applications of Image Processing in MATLAB

1. **Medical Imaging**: Enhancing MRI or CT scans, tumor detection, and image segmentation.
2. **Agriculture**: Analyzing satellite imagery for crop monitoring.
3. **Security**: Facial recognition, motion detection in surveillance footage.
4. **Industrial Automation**: Quality control through visual inspection.
5. **Robotics**: Object detection and tracking in autonomous systems.

## Demostration Video 

[**Watch on YouTube**]()

## Conclusion

MATLAB provides a rich and flexible environment for image processing that combines powerful built-in functions with an intuitive programming language. Whether you're working on academic projects, research, or industry-level applications, MATLAB offers the tools needed to process and analyze images efficiently. Its visualization capabilities and interactive tools make it an excellent choice for developing and testing image processing algorithms.

## References

- MATLAB. (2018, May 21). How to install MATLAB [Video]. YouTube. https://www.youtube.com/watch?v=f1UoHTf_Kgk
  
- GeeksforGeeks. (2021b, February 23). Digital Image Processing Algorithms using MATLAB. GeeksforGeeks. https://www.geeksforgeeks.org/digital-image-processing-algorithms-using-matlab/
  
- EFY Bureau. (2023, September 13). Image processing using MATLAB: Basic operations. Electronics for You. https://www.electronicsforu.com/electronics-projects/image-processing-using-matlab-part-1

---
