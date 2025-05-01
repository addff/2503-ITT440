# NURULHUDA BINTI AB. RAHMAN

## Identifying Colors with OpenCV and Pandas

### Introduction to OpenCV and Pandas
OpenCV (Open Source Computer Vision Library) is a powerful library used for image processing and computer vision tasks. It provides tools for manipulating images and videos, detecting objects, applying filters, and even performing machine learning-based image analysis. OpenCV is widely used in applications such as facial recognition, augmented reality, and automated image classification.

Pandas is a data manipulation and analysis library designed for handling structured data efficiently. It provides tools for loading, filtering, and transforming datasets using intuitive data structures like DataFrames. In these scripts, Pandas is used to read a CSV file containing color names and RGB values, allowing easy comparison and matching of colors.

By combining OpenCV for image processing and Pandas for data handling, these scripts efficiently identify and display color names from images and webcam feeds.

### Objective
The primary objective of both scripts is to allow users to interactively identify colors in images or live video streams. The image processing script lets users select images, click on pixels to determine their RGB values, and match them with the closest color name from a CSV file, displaying this information in a colored rectangle. The webcam color detection script captures live video, tracks the mouse cursor’s position, continuously detects RGB values of the pixel under the cursor, and displays the matching color name in real time. Both scripts provide an intuitive way to recognize colors through interactive image and video processing.

### How it Works
1) Loading Color Data by using the Pandas library to load color information from a CSV file named colors.csv. This file is expected to have columns like "color_name", "R", "G", and "B" containing the names of colors and their respective Red, Green, and Blue integer values.




