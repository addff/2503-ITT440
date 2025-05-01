**NAME : NURHIDAYAH BINTI AB HAMID**

**STUDENT ID : 2023260926**

**GROUP : M3CDCS2554A**

**SUBJECT : ITT440**

**TITLE : INTRODUCTION TO IMAGE PROCESSING USING NUMPY IN PYTHON**    
===

**Objective** :
--

- To write article about image processing using Python.
- To demonstrate coding use related to the article

**What is Image Processing ?**
---

Image processing refers to the technique of modifying and analyzing images to imrove their quality, extract useful information, or make them suitable for specific applications. This process typically involves converting images into digital form and using various algorithms to enhance, restore, compress, or analyze the visual data.

![image](https://github.com/user-attachments/assets/c3dc6655-0ad5-4517-9c9a-999f6ad2a043)

**What is NumPy?**
---

The name NumPy comes from "Numerical Python". NumPy is fundamental library for numerical computing. It offers a powerful multidimensional array object, along with a variety of tools such as matrices, masked arrays, and a wide range of efficient functions for performing operations on arrays. These operations include mathematical and logical calculations, reshaping, sorting, selection, input/output, Fourier transforms, basic linear algebra, statistical analysis, random number generation, and more. Developed by Travis Oliphant in 2005, NumPy is an open-source project that is freely available.

**What is NumPy used for?**
---

NumPy's capability to handle a complex mathematical operations on a large datasets make it a vital tool in fields that depend heavily on numerical analysis.

* Scientific computing : NumPy is widely used in physics, biology, finance, and engineering, particularly for simulations and modeling of real-world systems.
* Data Preparation and Analysis : It supports various stages of data processing, including cleaning, transformation, aggregation and more.
* Data Science, Machine Learning and AI: With strong support for linear algebra, NumPy plays a foundational role in machine learning and AI. It simplifies and accelrates matrix operations essential for tasks like data transformation, applying feature weights, making predictions, and enabling natural language processing through wordembeddings. Technologies like large language models (LLMs), including ChatGPT, rely heavily on matrix computations.
* Image processing: Since images are essentially multi-dimensional arrays, NumPy is a natural fit for performing image-related operations.

**Advantage of NumPy :**
---

* Speed and Performace: NumPy is much faster than regular Python lists for numerical computations because it's implemented in  C and uses optimized routines. 
* Memory efficiency: NumPy arrays store elements of the same data type contiguously in memory, resulting in less memory consumption compared to Python list, which can hold heterogeneous data.
* Multidimensional Array Support: Provide the ndarray object, which handles multi-dimensional arrays and matrices with ease.
* Broadcasting: Enables operations on arrays of different shapes and sizes without writing additional code.
* Open source and Well-Documented: Free available with strong community supoort and extensive documentation.

**Why NumPy is essential in image processing?**
---

NumPy is a foundational tool in image processing due to its ability to efficiently handle large-scale numerical data such as pixel values in digital images. Numpy's features become particularly powerful when applied to image-related tasks.
* Images are just arrays: Digital images are made up of pixels, and each pixel is a numerical value. NumPy represents images as multi-dimensional arrays and make it easy to access, modify, and analyze pixel data.
* Efficient Operations: Image processing often involves manipulating millions of pixel values. NumPy allows you to perform operations like brightness adjustment, filtering, and transformation using fast, vectorized computations without the need for slow loops.
* Memory Optimization: compared to Python lists, NumPy arrays use much less memory and process large images more efficiently, which is essential in real-time or batch processing tasks.
* Seamless Library Integration: Libraries like OpenCV, Pillow(PIL), scikit-image and Matplotlib use or support NumPy arrays. This makes it easy to combine NumPy with tools for image I/O, visualization, and advanced analysis. 

**How NumPy works with other libraries?**
---
NumPy is at the core of image processing in Python, but it works better when combines with libraries like Pillow or OpenCV for reading or writing images, Matplotlib for visualization, and scikit-image or Scipy for more advanced operations. Each tool handles specific part and NumPy will connect them through a data format call NumPy array.

**Basic NumPy Functions**
---
* np.array([1,2,3])   //create a 1D array
* np.eye(3)   //identity matrix(3x3)
* a.shape
* a.reshape(4,)   //flatten to 1D
* np.clip(a, 0, 255)   //limit values for brightness changes
* np.mean(image, axis=2)   //convert colour to grayscale by averaging RGB channels

**Python Code Example for image processing with NumPy**
---
```p
from PIL import Image 
import numpy as np

image = Image.open("image.png")

image_np = np.array(image)

//convert to grayscale
if len(image_np.shape) == 3:
    grayscale = np.mean(image_np,axis=2).astype(np.uint8)
else:
    grayscale = image_np

grayscale_img = Image.fromarray(grayscale, mode='L')

grayscale_img.save("grayscale_output.png")

print("Grayscale PNG saved successfully.")

//crop from (x=50, y=50) to (x=200, y=200)
cropped = image_np[50:200, 50:200]
cropped_img = Image.fromarray(cropped)
cropped_img.save("cropped_image.png")

//flip image
flipped = np.fliplr(image_np)
flipped_img = Image.fromarray(flipped)
flipped_img.save("flipped_image.png")

// increase brightness by 50 (max 255)
brighter = np.clip(image_np + 50, 0, 255).astype(np.uint8)
bright_img = Image.fromarray(brighter)
bright_img.save("brighter_image.png")

```
**Sample output**
---
![image](https://github.com/user-attachments/assets/763299d3-fc85-473f-9ae4-caf57f45c9e1)
original image

![brighter_image](https://github.com/user-attachments/assets/9175f75f-b989-48be-96c4-e9e85af36319) 
brighter image

![grayscale_output](https://github.com/user-attachments/assets/22c5541d-900c-4467-a737-8c74b4a6f7ef) 
grayscale image

![cropped_image](https://github.com/user-attachments/assets/e06ce34b-a196-4f54-8235-e29655b3079f)
cropped image

![flipped_image](https://github.com/user-attachments/assets/e1ed8265-3a42-4473-90ee-1984ab116cc6)
flipped image

**Demonstration image processing using NumPy in Python**
---

[![Watch the video](https://img.youtube.com/vi/UAIPT4ihvS0/maxresdefault.jpg)](https://youtu.be/UAIPT4ihvS0)

### [Watch this video on YouTube](https://youtu.be/UAIPT4ihvS0)


### [Watch this video on YouTube](https://youtu.be/UAIPT4ihvS0)
