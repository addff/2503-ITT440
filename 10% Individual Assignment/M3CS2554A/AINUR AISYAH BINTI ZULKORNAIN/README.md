## NAME: AINUR AISYAH BINTI ZULKORNAIN
## STUDENT ID: 2023226126
## TITLE: Image Processing Using MATLAB Image Processing

### Objective 
- To write an article about Image Processing using MATLAB tools.
- To demonstrate the coding and functions used in MATLAB related to the topic.

### Introduction to Image Processing
Image processing is the use of math and computer techniques to improve and understand digital images. It helps with tasks like cleaning up images, analyzing them and showing results clearly. Image processing is important in many areas, especially in computer vision and machine learning.

![matlabpic](https://github.com/user-attachments/assets/0120101d-5197-4611-a994-37d71181a476)


### What is MATLAB?
MATLAB is a high-level programming language and environment designed for numerical computing, data analysis, and visualization. It also comes with specialized toolboxes that make it easier to tackle specific challenges in fields like engineering and science.

### What is the Image Processing Toolbox?

The Image Processing Toolbox in MATLAB provides a set of tools and functions to help with a variety of image processing operations such as image enhancement, analysis, filtering, segmentation and transformation. This toolbox offers both high levvel and low level operations and is highly customized for engineering and scientific processes which makes it a common choice in both academia and industry.

### Core Features of the Image Processing Toolbox

- Image Enhancement - Contrast adjustment, histogram equalization
- Filtering - Gaussian blur, median filtering and sharpening.
- Edge Detection - Sobel, Prewitt, Canny and Roberts.
- Morphological Operations - Dilation, erosion, opening and closing
- Geometric Transformations - Resize, rotate, flip and crop
- Color Space Transformations - RGB to grayscale, HSV and etc
- Segmentation - Thresholding, region growing and watershed.
- Feature Detection & Extraction - Corners, blobs, Surf and Harris
- Image Registration & Alignment
- Batch Image Processing using MATLAB scripts

### Advantages of MATLAB for Image Processing

1. Comprehensive Toolbox: Built-in functions save development time and are optimized for performance.
2. Ease of Visualization: Offers powerful tools for plotting and displaying images and results.
3. Integration with AI/ML: Can be used with deep learning and has tools to use ready-made models for things like image recognition.
4. Batch Processing: Can edit or change a lot of images at once using simple MATLAB code or built-in apps.
5. Custom Algorithm Development: Users can create and try their own image methods. Apps like Image Segmenter and Color Thresholder make it easy to do hard tasks.

### Basic Image Processing Functions in MATLAB

Below are commonly used image processing functions in MATLAB along with their purposes:

- Flip Image
  fliplr(image): flips the image horizontally (left to right).

- RGB to Grayscale
   rgb2gray(image): Converts an RGB image to grayscale, simplifying the image for further   
   processing.

- Gaussian Blur
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
```
### The Original Image

![LATESTMATLAB](https://github.com/user-attachments/assets/3993013d-b50a-4308-9114-8a37e5c09588)

### Output

![flipped image](https://github.com/user-attachments/assets/4ea00628-66c2-435e-af46-853935a82b5b)

![grayscale image](https://github.com/user-attachments/assets/09954ed3-3388-4f3d-bf73-d53a3ab5e0e6)

![Gaussian blurred image](https://github.com/user-attachments/assets/2e48a0ee-77e8-488d-8a22-11c03149c9b6)

### Demo

https://drive.google.com/file/d/1QxY69D481oXSKIHN8-vvSToBxRSUr__b/view?usp=drive_link
