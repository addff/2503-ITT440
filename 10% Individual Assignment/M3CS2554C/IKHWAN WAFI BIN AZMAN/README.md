# Project: Exploring Image Processing Techniques Using PyImageJ

### NAME : IKHWAN WAFI BIN AZMAN  
### **STUDENT ID : 2024807134**  
### **CLASS : DCS2554C**  
### **TITLE : Exploring Image Processing Techniques Using PyImageJ**


## Introduction to Image Processing

Image processing is a technique used to manipulate or analyze digital images through computer algorithms. It involves performing operations on an image to extract information, enhance visual quality, or modify certain features. This field is widely used in various applications such as medical imaging, remote sensing, robotics, computer vision, and multimedia.

### Key Concepts in Image Processing:
- **Image Enhancement**: Techniques to improve the quality of an image, such as adjusting contrast, brightness, or applying filters to reduce noise.
- **Image Segmentation**: Dividing an image into different regions based on specific features (e.g., color, texture) to simplify its analysis.
- **Edge Detection**: Identifying boundaries within an image, often used in object recognition and scene analysis.
- **Object Recognition**: Detecting and identifying objects or patterns in an image, such as detecting faces or vehicles.
- **Image Transformation**: Geometric transformations, like rotation, scaling, or resizing, to modify the spatial properties of an image.

Image processing can be carried out using various software and libraries. With the rise of tools like **ImageJ** and libraries such as **OpenCV**, **scikit-image**, and **PyImageJ**, it has become easier to automate and integrate image processing tasks into larger workflows.

By transforming images into useful data, image processing plays a crucial role in many industries, from enhancing medical diagnoses to improving security systems.

<p align="center">
  <img src="https://github.com/Wafiy2003/IMAGE-2/blob/0ccee1aa512a3311040718eb5b03f3e85e68f1c7/images.jpg" alt="image alt">
</p>

## What is PyImageJ?

**PyImageJ** is a Python library that provides access to ImageJ2 — a powerful, Java-based image processing software — from within Python. It allows users to run ImageJ operations, open and analyze images, and use ImageJ plugins directly in Python scripts.

PyImageJ makes it possible to:
- Combine ImageJ tools with Python libraries like NumPy, SciPy, OpenCV, and matplotlib.
- Run ImageJ macros and plugins from Python code.
- Convert images between Java (ImageJ) and Python (NumPy/xarray) formats.
- Automate image processing tasks in research, medical imaging, and computer vision.

It is especially useful when you want the power of ImageJ with the flexibility and simplicity of Python.

## Tools

<p align="center">
  <img src="https://github.com/Wafiy2003/IMAGE/blob/b55f90915f6aa46cac7f824424f7b05e31ee0f25/1268233.png" alt="image alt">
</p>

## Benefits of Using PyImageJ

### ✔️ **Powerful Image Processing**
- **Hybrid Power**: Leverage the robust image processing capabilities of **ImageJ** alongside the flexibility and rich libraries of **Python**, like **NumPy**, **TensorFlow**, **OpenCV**, and **scikit-image**.
- **Access to 1,000+ ImageJ Plugins**: Utilize a wide variety of community-contributed plugins for tasks like segmentation (e.g., **Trainable Weka**), image morphing, colocalization analysis, and more.

### ✔️ **Seamless Data Interoperability**
- **Image Conversion**: Effortlessly convert images between **ImageJ’s ImgLib2** format and **Python’s NumPy arrays**, allowing for smooth integration with other Python-based tools and workflows.
- **Preserve Data Integrity**: Keep the integrity of image data intact when working across both ImageJ and Python.

### ✔️ **Automation & Scalability**
- **Headless Operation**: Run complex image processing tasks without the need for a graphical user interface (GUI), making it ideal for batch jobs, server-side processing, or cloud deployments.
- **Reproducibility**: Replace manual GUI steps with reproducible Python scripts, ensuring consistency across analyses and experiments.

### ✔️ **Cross-Platform Flexibility**
- **Supports Multiple Platforms**: Works seamlessly across **Windows**, **macOS**, and **Linux** systems, making it accessible to a wide range of users.
- **Cloud and Jupyter Notebook Integration**: Run PyImageJ in cloud environments or directly within **Jupyter notebooks** and **Google Colab**, enabling collaborative and scalable workflows.

### ✔️ **Domain-Specific Expertise**
- **Biomedical and Scientific Imaging**: PyImageJ is an excellent choice for **microscopy**, **MRI analysis**, and **bioimaging** workflows, where precision and flexibility are essential.
- **Scientific Rigor**: Leverage ImageJ’s peer-reviewed operations, such as **TrackMate** for particle tracking or **Bio-Formats** for high-performance file handling.

### ✔️ **Enhanced Customization and Extensibility**
- **Legacy Macro Support**: Run traditional **ImageJ** macros directly from Python, ensuring compatibility with older workflows while gaining the benefits of Python-based automation.
- **Extensive Customization**: Create custom workflows and integrate additional Python tools or external libraries to enhance the capabilities of **ImageJ**.

## How to install PyImageJ

To use **PyImageJ**, you need:
- Python (recommended: version 3.8 or 3.9)
- Java (OpenJDK 8 is ideal)
- A package manager: either **conda** (recommended) or **pip**
- Or you can use Google Colab through browser
 ### Method 1: Install with Conda (Recommended)

This is the easiest and most reliable method.
### 🪟 Step-by-Step Guide for Windows

1. Go to the official Miniconda page:  
   [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

<p align="center">
  <img src="https://github.com/Wafiy2003/IMAGE/blob/6f5c4dbc8e27ed56db5f6adf5e99f564d4778601/Screenshot%202025-05-01%20154418.png" alt="image alt">
</p>
2. Download the **Miniconda Installer for Windows**:  
   Choose the **64-bit version** for Python **3.9 or newer**.

3. Run the downloaded `.exe` installer.

4. Click **Next**, agree to the terms, and choose **"Install Just for Me"**.

5. ⚙When asked, check the box that says:  
   **"Add Miniconda to my PATH environment variable"** (optional but helpful).

 ## Sample Code: PyImageJ in Action

This example shows how to:

- Initialize PyImageJ using the Fiji distribution  
- Load and display an image  
- Apply a Gaussian blur  
- Convert the result to a NumPy array (optional)

---

# Installation and setup
---

### 1.Install PyImageJ

```python
# Install Java and PyImageJ
!apt-get install openjdk-8-jdk -qq > /dev/null
!update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
!pip install pyimagej

print("✅ Installation complete!")

```
### 2.Upload Your Image
```python
from google.colab import files
import matplotlib.pyplot as plt

# Upload your image file
uploaded = files.upload()

# Get the filename of your uploaded image
your_image = list(uploaded.keys())[0]

# Show your image
plt.imshow(plt.imread(your_image))
plt.axis('off')  # Hide axes
plt.title("Your Uploaded Image")
plt.show()
```

### 3.Process with ImageJ
```python

import imagej
import numpy as np

# Start ImageJ (this takes about 1 minute)
ij = imagej.init('sc.fiji:fiji:2.14.0')
print(f"🎉 ImageJ version: {ij.getVersion()}")

# Convert your image to ImageJ format
image_data = plt.imread(your_image)
ij_image = ij.py.to_java(image_data)

# Example 1: Gaussian Blur
blurred = ij.op().filter().gauss(ij_image, 5.0)

plt.figure(figsize=(15,5))
plt.subplot(131)
plt.imshow(image_data)
plt.title("Original")
plt.axis('off')

plt.subplot(132)
plt.imshow(ij.py.from_java(blurred))
plt.title("Blurred")
plt.axis('off')

# Example 2: Edge Detection
edges = ij.op().filter().sobel(ij_image)
plt.subplot(133)
plt.imshow(ij.py.from_java(edges), cmap='gray')
plt.title("Edges")
plt.axis('off')

plt.show()

```
### 4.Save the result
```python
from skimage.io import imsave

# Save blurred image
imsave('blurred.png', ij.py.from_java(blurred))

# Download to your computer
files.download('blurred.png')

```

### Output

<p align="center">
  <img src="https://github.com/Wafiy2003/IMAGE/blob/588d97f380ec92bec34c2b64a065039c28fc111b/Screenshot%202025-05-01%20222051.png" alt="image alt">
</p>

# Conclusion

**PyImageJ** offers a versatile bridge between Python’s rich ecosystem and ImageJ’s decades of bioimage analysis expertise. It delivers a unique solution for researchers who need both scripting flexibility and access to specialized ImageJ plugins.

Seamlessly combine Python’s machine learning tools (like TensorFlow or scikit-learn) with ImageJ’s powerful library of microscopy, segmentation, and quantification tools—all while preserving metadata and handling multi-dimensional image data.

---

## Strengths and Specialization

- ✔ **Plugin Ecosystem**  
  Directly leverage 500+ ImageJ plugins (e.g., *Fiji*, *TrackMate*, *Bio-Formats*) within Python workflows.

- ✔ **Multi-Dimensional Data**  
  Native support for 5D (XYZCT) images—critical for time-lapse microscopy and volumetric analysis.

- ✔ **Interoperability**  
  Effortlessly convert between `NumPy` arrays and ImageJ data structures to create hybrid Python-ImageJ pipelines.

- ✔ **Cloud & Reproducibility**  
  Fully compatible with Google Colab, MyBinder, or Jupyter Notebooks—perfect for collaborative and educational use.

---

## Challenges

- **Java Dependency**  
  Requires OpenJDK, which can complicate deployment in certain environments.

- **Performance Trade-Offs**  
  Converting between Python and ImageJ data formats may introduce overhead with large datasets.

- **Learning Curve**  
  Users must become familiar with both ImageJ’s macro language and Python APIs.

---

## Ideal Use Cases

- 🔬 **Bioimage Analysis**  
  Perform automated cell segmentation, colocalization studies, or FRET analysis.

- 🔄 **Batch Processing**  
  Script large-scale image workflows using Python loops while applying ImageJ’s algorithms.

- 🤖 **AI-Augmented Workflows**  
  Combine ImageJ’s classical tools with modern ML models (e.g., *StarDist*, *CellPose*).

- 📚 **Education & Training**  
  Teach bioimage analysis with reproducible and shareable Jupyter notebooks.

---

# Demonstration video
https://youtube.com/watch?v=kflDHefWxtc&feature=shared

