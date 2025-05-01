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
- 
 ### ✅ Method 1: Install with Conda (Recommended)

This is the easiest and most reliable method.
### 🪟 Step-by-Step Guide for Windows

1. Go to the official Miniconda page:  
   [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

<p align="center">
  <img src="https://github.com/Wafiy2003/IMAGE/blob/6f5c4dbc8e27ed56db5f6adf5e99f564d4778601/Screenshot%202025-05-01%20154418.png" alt="image alt">
</p>
3. Download the **Miniconda Installer for Windows**:  
   Choose the **64-bit version** for Python **3.9 or newer**.

4. Run the downloaded `.exe` installer.

5. Click **Next**, agree to the terms, and choose **"Install Just for Me"**.

6. ⚙When asked, check the box that says:  
   **"Add Miniconda to my PATH environment variable"** (optional but helpful).

   ## 🧪 Sample Code: PyImageJ in Action

This example shows how to:

- Initialize PyImageJ using the Fiji distribution  
- Load and display an image  
- Apply a Gaussian blur  
- Convert the result to a NumPy array (optional)

---

# PyImageJ: Image Processing in Python

## Basic Usage Examples

---

### 1. Opening and Displaying an Image

```python
import imagej

# Initialize ImageJ (Fiji)
ij = imagej.init('sc.fiji:fiji', headless=False)

# Load image
image = ij.io().open('sample_image.jpg')

# Show image
ij.ui().show("Original Image", image)

# Print image info
dims = image.getDimensions()
print("Image Dimensions:", dims)

```
### 2.Applying a Gaussian Blur
```python
# Apply Gaussian blur (sigma = 2.0)
blurred = ij.op().run("filter.gaussian", image, 2.0)

# Show blurred image
ij.ui().show("Blurred Image", blurred)
```

### 3.Converting to NumPy Array
```python

# Convert the result to NumPy
image_np = ij.py.from_java(blurred)

print("Image shape (NumPy):", image_np.shape)

```
