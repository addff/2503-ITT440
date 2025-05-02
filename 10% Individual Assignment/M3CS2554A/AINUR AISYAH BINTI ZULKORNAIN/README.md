## NAME: AINUR AISYAH BINTI ZULKORNAIN
## STUDENT ID: 2023226126
## TITLE: Image Processing Using MATLAB Image Processing

### Objective 
- To write an article about Image Processing using MATLAB tools.
- To demonstrate the coding and functions used in MATLAB related to the topic.

### Introduction to Image Processing
Image processing enhances and analyzes digital images using algorithmic and mathematical procedures. The Image Processing Toolbox in MATLAB offers preprocessing, analysis and visualization capabilities. It is widely used in practical applications like industrial inspection, surveillance and medical imaging which highlights its increasing significance in domains like computer vision and machine learning.

 
![unnamed.png](https://github.com/addff/2503-ITT440/blob/main/10%25%20Individual%20Assignment/M3CS2554A/AINUR%20AISYAH%20BINTI%20ZULKORNAIN%EF%80%8D/matlabpic.png)

### What is MATLAB?
MATLAB is a high-level programming language and environment designed for numerical computing, data analysis, and visualization. It also comes with specialized toolboxes that make it easier to tackle specific challenges in fields like engineering and science.

### What is the Image Processing Toolbox?

The Image Processing Toolbox in MATLAB provides a set of tools and functions to help with a variety of image processing operations such as image enhancement, analysis, filtering, segmentation and transformation. This toolbox offers both high levvel and low level operations and is highly customized for engineering and scientific processes which makes it a common choice in both academia and industry.

### Core Features of the Image Processing Toolbox

1. Image Enhancement - Contrast adjustment, histogram equalization
2. Filtering - Gaussian blur, median filtering and sharpening.
3. Edge Detection - Sobel, Prewitt, Canny and Roberts.
4. Morphological Operations - Dilation, erosion, opening and closing
5. Geometric Transformations - Resize, rotate, flip and crop
6. Color Space Transformations - RGB to grayscale, HSV and etc
7. Segmentation - Thresholding, region growing and watershed.
8. Feature Detection & Extraction - Corners, blobs, Surf and Harris
9. Image Registration & Alignment
10. Batch Image Processing using MATLAB scripts

### Advantages of MATLAB for Image Processing

1. Comprehensive Toolbox: Built-in functions save development time and are optimized for performance.
2. Ease of Visualization: Offers powerful tools for plotting and displaying images and results.
3. Integration with AI/ML: Can be used with deep learning and has tools to use ready-made models for things like image recognition.
4. Batch Processing: Can edit or change a lot of images at once using simple MATLAB code or built-in apps.
5. Custom Algorithm Development: Users can create and try their own image methods. Apps like Image Segmenter and Color Thresholder make it easy to do hard tasks.

### Basic Image Processing Functions in MATLAB

Below are commonly used image processing functions in MATLAB along with their purposes:

1. Flip Image
  fliplr(image): flips the image horizontally (left to right).

2. RGB to Grayscale
   rgb2gray(image): Converts an RGB image to grayscale, simplifying the image for further   
   processing.

3. Gaussian Blur
imgaussfilt(image, sigma): Smooths the image and reduces noise or detail.

###### Code:
```py
% Read the color image
imageFileName = 'LATESTMATLAB.jpeg';  % 
originalImage = imread(imageFileName);

%% 1. Flip Image (only RGB)
% Flip the image horizontally (left-right)
flippedImage = fliplr(originalImage);

% Display the flipped image
figure;
imshow(flippedImage);
title('Flipped Image (Left-Right)');

%% 2. RGB to Grayscale
% Convert the RGB image to grayscale
grayImage = rgb2gray(originalImage);

% Display the grayscale image
figure;
imshow(grayImage);
title('Grayscale Image');

%% 3. Gaussian Blur
% Apply Gaussian Blur to the grayscale image
blurredImage = imgaussfilt(grayImage, 2);  % Sigma = 2 for smoothing

% Display the Gaussian blurred image
figure;
imshow(blurredImage);
title('Gaussian Blurred Image');

