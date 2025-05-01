### **NAME: MOHAMAD AZIM IRFAN FIRDAUS BIN MOHD AZMI**
### **STUDENT ID: 2024213842**
### **CLASS: CDCS2554C**
### **TITLE: INTRODUCTION TO BASIC IMAGE PROCESSING USING SIMPLEITK IN PYTHON** 

# **WHAT IS IMAGE PROCESSING** <img align="center" width="200" height="200" src="https://github.com/azimirfan/IMAGE/blob/a934caedeaef9f11372b734f2e95edf55b2c0510/art%20geometry%20GIF%20by%20Michel%20Poisson.gif">
Image processing is the manipulation and analysis of images, typically digital ones, to enhance their visual quality, extract information, or prepare them for further use. It involves converting images or video sequences into digital formats that can be analyzed by algorithms. This process can involve various techniques like enhancement, noise reduction, edge detection, and more, ultimately aiming to improve the image or extract meaningful data. 

# **TOOLS**
<div align="center">
<img align="center" width="200" height="200" src="https://github.com/azimirfan/IMAGE/blob/72fec3e54d5fd5b2f9edb60f3e30d14d3c0402aa/SimpleITK-removebg-preview.png">
   
</div>
               <div align="center"> Insight Segmentation and Registration Toolkit (ITK) </div>                        

# WHAT IS SIMPLEITK 
SimpleITK is a simplified, easy-to-use interface to the Insight Segmentation and Registration Toolkit (ITK), a powerful library widely used for medical image processing. SimpleITK is designed to be accessible from scripting languages like Python, R, and Java, making it suitable for rapid development, education, and research.

| **FEATURES OF SIMPLEITK** |
|---------------------------|
|1. Multi-language support: Works with Python, R, C#, Java, and more.|  
|2. N-dimensional image support: Typically works with 2D, 3D, and even 4D (time series) images.|
|3. IO operations: Read/write many medical image formats (DICOM, NIfTI, MetaImage, NRRD, etc.).|
|4. Image types: Supports scalar, vector, and label images.|
|5. Image types: Supports scalar, vector, and label images.|

# **CORE CONCEPTS**
SimpleITK represents images as multi-dimensional arrays with associated metadata:

* Physical spacing between pixels
* Origin coordinates
* Direction cosines (orientation)

  # ADVANTAGES AND DISADVANTAGES USING SIMPLEITK IMAGE PROCESSING
  ## ADVANTAGES
 * Simplified, consistent API across multiple programming languages
 * Specialized for medical imaging with robust metadata handling
 * Comprehensive toolkit with 280+ filters for segmentation, registration, and analysis
 * Physical space awareness (maintains origin, spacing, orientation)
 * Cross-platform compatibility (Windows, macOS, Linux)
 * Strong support for multi-dimensional data (2D, 3D, 4D)

   ## DISADVANTAGES
 *  Steeper learning curve for advanced parameter tuning
 *  Performance overhead for simple operations
 * Limited GPU acceleration compared to deep learning frameworks
 *  Smaller community and fewer resources than general-purpose libraries
 *  Not ideal for non-medical computer vision tasks
 *  Can lag behind cutting-edge research implementations


> [!IMPORTANT]
> # BASIC OPERATIONS 
1. **Image I/O:** Reading and writing various medical image formats (DICOM, NIFTI, etc.)
2. **Filtering:** Smoothing, edge detection, morphological operations
3. **Segmentation:** Thresholding, region growing, level sets
4. **Registration:** Aligning images from different sources or time points

   # Common Workflow
   ``` python
   import SimpleITK as sitk
   
   # Read an image
   image = sitk.ReadImage("example.dcm")

   # Apply Gaussian smoothing
   smoothed = sitk.DiscreteGaussian(image, sigma=2.0)

   # Segment using thresholding
   segmentation = sitk.BinaryThreshold(smoothed, lowerThreshold=100, upperThreshold=200)

   # Save the result
   sitk.WriteImage(segmentation, "output.nii")
   ```

   # INSTALLATION AND SETUP
  #### SimpleITK can be installed using package managers:

``` PYTHON

# Using pip
pip install SimpleITK

# Using conda
conda install -c simpleitk simpleitk
```
  # IMAGE TYPES AND DIMENSIONS 
  #### SimpleITK supports:
  * 2D, 3D, and 4D (3D+time) images
  * Various pixel types: uint8, int16, float32, vector pixel types, etc.
    ``` python
    import SimpleITK as sitk
    
    # Create a blank 3D image (100x100x100) with float32 pixels
    image = sitk.Image([100, 100, 100], sitk.sitkFloat32)
    
    # Get image properties
    size = image.GetSize()  # (100, 100, 100)
    spacing = image.GetSpacing()  # Default: (1.0, 1.0, 1.0)
    origin = image.GetOrigin()  # Default: (0.0, 0.0, 0.0)
    ```
 # ACCESSING AND MODIFYING PIXEL DATA

 ``` python
# Converting to/from NumPy arrays (Python)
import numpy as np

# SimpleITK to NumPy
array = sitk.GetArrayFromImage(image)  # Note: axes order is reversed!

# Modify in NumPy
array[50, 50, 50] = 1.0

# NumPy to SimpleITK
modified_image = sitk.GetImageFromArray(array)

```

# NOISE REDUCTION
``` python
# Gaussian smoothing
gaussian = sitk.DiscreteGaussian(image, sigma=2.0)

# Median filtering (robust to outliers)
median = sitk.Median(image, [3, 3, 3])  # 3x3x3 kernel

# Anisotropic diffusion (edge-preserving smoothing)
anisotropic = sitk.CurvatureAnisotropicDiffusion(image, 
                                                timeStep=0.0625,
                                                conductanceParameter=3.0,
                                                numberOfIterations=5)

```

# EXAMPLE OF SIMPLE DEMONSTRATION
### CODING
``` python
import SimpleITK as sitk
import matplotlib.pyplot as plt

# Step 1: Read on image
image_path = 'imageSimpleitk.png' 
image = sitk.ReadImage(image_path)

# Step 2: Apply a Gaussian filter
sigma = 2.0  # Standard deviation for Gaussian kernel
filtered_image = sitk.SmoothingRecursiveGaussian(image, sigma)

# Step 3: Convert images to numpy arrays for visualization
original_array = sitk.GetArrayFromImage(image)
filtered_array = sitk.GetArrayFromImage(filtered_image)

# Step 4: Display the original and filtered images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(original_array, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Filtered Image (Gaussian)')
plt.imshow(filtered_array, cmap='gray')
plt.axis('off')


plt.show()

```
### OUTPUT


