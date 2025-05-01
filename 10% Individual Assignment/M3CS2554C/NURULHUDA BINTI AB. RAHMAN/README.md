# NURULHUDA BINTI AB. RAHMAN

## Identifying Colors with OpenCV and Pandas

### Introduction to OpenCV and Pandas

In this project, I use computer vision and image processing to identify the color at a specific pixel location from an image or a webcam feed. It employs the OpenCV library for real-time image capture and processing, alongside pandas for handling color data. The color detection system uses a CSV file containing RGB values and corresponding color names to map a selected color to its closest known name.

OpenCV (Open Source Computer Vision Library) is a powerful library used for image processing and computer vision tasks. It provides tools for manipulating images and videos, detecting objects, applying filters, and even performing machine learning-based image analysis. OpenCV is widely used in applications such as facial recognition, augmented reality, and automated image classification.

Pandas is a data manipulation and analysis library designed for handling structured data efficiently. It provides tools for loading, filtering, and transforming datasets using intuitive data structures like DataFrames. In these scripts, Pandas is used to read a CSV file containing color names and RGB values, allowing easy comparison and matching of colors.

By combining OpenCV for image processing and Pandas for data handling, these scripts efficiently identify and display color names from images and webcam feeds.

### Objective
The primary objective of both scripts is to allow a user to interactively identify the name of a color present in an image or a live video stream.

For the image processing script, the objectives are:

To enable the user to select one or more image files.
To allow the user to click on any pixel within the image.
To determine the RGB values of the clicked pixel.
To find the closest matching color name from the colors.csv file based on these RGB values.
To display a colored rectangle along with the identified color name and the RGB values on the image.

For the webcam color detection script, the objectives are:

To capture live video from the user's webcam.
To display the webcam feed in a window.
To track the mouse cursor's position within the video frame.
To continuously determine the RGB values of the pixel under the mouse cursor.
To find the closest matching color name from the colors.csv file based on these RGB values.
To display a colored rectangle along with the identified color name and the RGB values on the webcam feed.
To provide a real-time color identification experience.

### How it Works
1) Loading Color Data by using the Pandas library to load color information from a CSV file named colors.csv. This file is expected to have columns like "color_name", "R", "G", and "B" containing the names of colors and their respective Red, Green, and Blue integer values.

   ![Screenshot_150](https://github.com/user-attachments/assets/e96aa977-eb27-44a1-8427-7a9283771dcd)
2)The **get_color_name(R, G, B)** function finds the closest matching color by comparing the input RGB values with those in the **colors.csv** file. It calculates a simplified Manhattan distance and returns the color with the smallest difference.

   ![image](https://github.com/user-attachments/assets/818da0b7-f50b-456f-87ad-e7929f6c7b4d)







