## NAME : MUHAMMAD DANIEL ZALEIGH BIN MOHD AMZUKI

## STUDENT ID : 2023240232

## CLASS : CDCS2554A

## TITLE: INTRODUCTION TO BASIC IMAGE PROCESSING USING MAHOTAS IN PHYTON.

### 🎯 Objectives  
* ✅ To understand the basics of image processing  
* ✅ To learn how Mahotas can be used for thresholding and edge detection  
* ✅ To write and run Python code using Mahotas  
* ✅ To demonstrate and explain the output in a video
  
### 🧠 What is Image Processing?  

Image processing is a technique used to manipulate and analyze digital images in order to improve their quality, extract meaningful information, or prepare them for further tasks such as classification or recognition. It involves applying mathematical and algorithmic operations to pixel data, enabling computers to interpret images in ways that are useful for both human understanding and machine automation. Common applications include enhancing photo clarity, detecting objects or patterns, removing noise, segmenting regions of interest, and analyzing textures or shapes. Image processing plays a vital role in various fields such as medical diagnostics, surveillance, robotics, remote sensing, and artificial intelligence, making it a foundational tool in modern technological and scientific development.

### 📦 What is Mahotas?  

Mahotas is an open-source computer vision and  image processing library for phyton. Unlike heavier libraries like OpenCV, Mahotas is lightweight and focuses on numerical operations using NumPy arrays.
* 🚀 Developed in C++ for speed  
* 🧬 Ideal for bio-image analysis and scientific image processing  
* 🔗 Compatible with NumPy and SciPy  

### 🌟 Significance of Mahotas  
* ⚡ Fast performance due to C++ backend  
* 🔄 Easy to integrate with other scientific libraries like NumPy and Matplotlib  
* 🧪 Great for academic and research usage, especially in Biology
  
### 🧰 Libraries Related to Mahotas  
* 📊 NumPy: Used for array handling  
* 🖼️ Matplotlib: For displaying images  
* 📐 SciPy: Sometimes used alongside for mathematical functions  
* 🧠 OpenCV: A more feature-rich alternative for advanced tasks  

### 📚 Modules / Subpackages in Mahotas  
Mahotas contains many modules such as:
* 🔎 `mahotas.thresholding`: Thresholding methods (e.g. Otsu)  
* 🧹 `mahotas.filters`: Filtering like Gaussian, Sobel, etc.  
* 🧠 `mahotas.features`: For Haralick features, Zernike moments  
* 🧱 `mahotas.morph`: Morphological operations (e.g. erosion, dilation)  


### 💻 Python Code Example: Basic Image Processing with Mahotas  
```bash
import mahotas
import numpy as np
import matplotlib.pyplot as plt
import os

image_files = ['bmw.jpg', 'greyscale image.jpg', 'olivia.jpeg']  

for img_name in image_files:
    
    img = mahotas.imread(img_name)
    
    if img.ndim == 3:
        img = img.mean(axis=2).astype(np.uint8)

    gaussian_filtered = mahotas.gaussian_filter(img, 2)
    T_otsu = mahotas.thresholding.otsu(gaussian_filtered.astype(np.uint8))
    thresholded = gaussian_filtered > T_otsu
    edges = mahotas.sobel(gaussian_filtered)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title(f"{img_name} - Original")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(gaussian_filtered, cmap='gray')
    plt.title("Gaussian Filtered")
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(thresholded, cmap='gray')
    plt.title("Otsu Thresholding")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(edges, cmap='gray')
    plt.title("Sobel Edge Detection")
    plt.axis('off')

    plt.tight_layout()

    output_file = f"{os.path.splitext(img_name)[0]}_mahotas_output.png"
    plt.savefig(output_file)
    plt.show()

```
### [Watch My Mahotas Image Processing Demo]
[![Watch the demo](https://img.youtube.com/vi/5yiIxnm_Glk/0.jpg)](https://www.youtube.com/watch?v=5yiIxnm_Glk)
