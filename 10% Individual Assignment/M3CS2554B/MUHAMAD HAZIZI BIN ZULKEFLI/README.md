# MUHAMAD HAZIZI BIN ZULKEFLI
ITT440 - Individual Assignment

Student ID: 2023643902

# Introduction
Using methods like filtering, resizing, color adjustment, and object detection, image processing is the branch of computer science that focuses on enhancing images, extracting valuable information, or preparing them for additional tasks like recognition, analysis, or visualization.

# Tools 
Matplotlib

# What is Matplotlib?
Matplotlib is a popular data visualization library in Python. It provides functions and tools for creating a wide variety of static, animated, and interactive plots.

Key Features
2D Plotting: Line charts, bar graphs, scatter plots, histograms, etc.
Customization: Control over figure size, colors, fonts, labels, etc.
Integration: Works well with libraries like NumPy, Pandas, and Jupyter Notebooks.
Sub-library: pyplot is the most commonly used module in Matplotlib (often imported as plt).

# How It Works
Matplotlib functions by enabling to produce charts and plots that visually display data.  Importing the library and getting data ready—typically in the form of lists or arrays—come first.  Instruct Matplotlib on the type of chart to be produced (line, bar, scatter) using functions such as plt.plot().
To make the visualization understandable and educational, we can then alter the storyline by using titles, labels, legends, and other elements.  
Lastly, we can print the plot in a notebook or display it in a window by using plt.show().  Matplotlib creates a figure in the background, inserts one or more axes (plot regions) into it, and then turns your data into visuals.

There's a handy chapter in the docs explaining how libvips opens files, which gives some more background.

(https://hub.gesis.mybinder.org/user/matplotlib-mpl-brochure-binder-66gjdkjn/doc/tree/MatplotlibExample.ipynb)

# How to Install Matplotlib?
1. Using pip
   
pip install matplotlib

2. After installation, open Phyton and try

import matplotlib.pyplot as plt

# Source Code

import matplotlib.pyplot as plt

import numpy as np

from scipy import ndimage

import imageio

Load the image

image = imageio.v2.imread

1. Apply Sobel filters for edge detection
   
sobel_x = ndimage.sobel(image, axis=0)

sobel_y = ndimage.sobel(image, axis=1)

edges = np.hypot(sobel_x, sobel_y)


2. Plot the original and processed images
   
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)

plt.title("Original Grayscale")

plt.imshow(image, cmap='gray')

plt.axis('off')

plt.subplot(1, 3, 2)

plt.title("Sobel X")

plt.imshow(sobel_x, cmap='gray')

plt.axis('off')

plt.subplot(1, 3, 3)

plt.title("Edge Detection")

plt.imshow(edges, cmap='gray')

plt.axis('off')

plt.tight_layout()

plt.show()

# Output Description

- Loads a grayscale image

- Detects edges using Sobel operators

- Visualizes the original and processed images side by side

# Video Tutorial

- https://www.youtube.com/watch?v=aUw47Xey8sg








