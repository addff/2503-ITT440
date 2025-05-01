## NAME: AINUR AISYAH BINTI ZULKORNAIN
## STUDENT ID: 2023226126
## TITLE: Image Processing Using MATLAB Image Processing ToolBox

### Objective 
- To write an article about Image Processing using MATLAB tools.
- To demonstrate the coding and functions used in MATLAB related to the topic.

### Introduction to Image Processing
Image processing enhances and analyzes digital images using algorithmic and mathematical procedures. The Image Processing Toolbox in MATLAB offers preprocessing, analysis and visualization capabilities. It is widely used in practical applications like industrial inspection, surveillance and medical imaging which highlights its increasing significance in domains like computer vision and machine learning.

### MATLAB
 
-

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
Gaussian Blur
imgaussfilt(image, sigma): Smooths the image and reduces noise or detail.

1. Median Blur
   medfilt2(image): Removes salt-and-pepper noise from the image.

2. Sharpening
   imsharpen(image): Makes the edges and details in the image clearer.

3. Brightness & Contrast Adjustment
   imadjust(image): Changes the brightness and contrast of the image.

4. Histogram Equalization
   histeq(image):  Improves the overall contrast by spreading out intensity values.

###### Code:
```py
% Read the image from the current folder
imageFileName = 'formatlab.jpg';  
if exist(imageFileName, 'file') ~= 2
    error('Image file "%s" not found in the current folder.', imageFileName);
end

% Load and convert to grayscale
originalImage = imread(imageFileName);
grayImage = rgb2gray(originalImage);

% Apply Gaussian Blur
gaussianBlur = imgaussfilt(grayImage, 2);  % sigma = 2

% Apply Histogram Equalization
equalizedImage = histeq(grayImage);

% Detect Edges using Canny method
edges = edge(grayImage, 'Canny');

% Display results in a 2x3 grid
figure('Name', 'Image Processing Demo', 'NumberTitle', 'off');

subplot(2,3,1);
imshow(originalImage);
title('Original Image');

subplot(2,3,2);
imshow(grayImage);
title('Grayscale');

subplot(2,3,3);
imshow(gaussianBlur);
title('Gaussian Blur');

subplot(2,3,4);
imshow(edges);
title('Canny Edges');

subplot(2,3,5);
imshow(equalizedImage);
title('Histogram Equalization');


