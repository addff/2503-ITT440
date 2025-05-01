## NAME: FATIN AIDA BINTI OTHMAN
## STUDENT NO: 2023406298
## CLASS: M3CS2554A
## TITLE: IMAGE PROCESSING USING SCIKIT-IMAGE

**Objective**

- To write an article about Image Processing using SCIKIT-IMAGE tools.
- To demonstrate the coding and functions used in SCIKIT-IMAGE related to the topic.

**Introduction to Image Processing**

Image processing involves enhancing and analyzing digital images through algorithmic and mathematical techniques. The scikit-image library in Python offers a wide range of tools for image preprocessing, analysis, and visualization. It is widely used in practical applications such as industrial inspection, surveillance, and medical imaging, reflecting its growing relevance in fields like computer vision and machine learning.

**What is SCIKIT-IMAGES ?**

Scikit-image (also known as skimage) is one of the open-source image-processing libraries for the Python programming language. It provides a powerful toolbox of algorithms and functions for various image processing and computer vision tasks and it is built on top of popular scientific libraries like NumPy and SciPy.ndimage. Scikit-image also known image processing Python package that works with NumPy arrays which is a collection of algorithms for image processing.

**Feature of SCIKIT-IMAGES:**

1. **Open-source and free**:  Available at no cost and without usage restrictions.
2. **Supports many image formats**: Can read and write JPEG, PNG, TIFF, and more.
3. **Uses NumPy arrays**: Images are stored as NumPy `ndarray`, so you can use NumPy functions to manipulate them.
4. **Provides many image processing tools**: Functions for filtering, segmentation, feature extraction and morphological operations
5. **Easy to use**: Beginner-friendly and consistent API.

**Advantages of SCIKIT-IMAGE**

1. **Works Well with Other Python Tools**  
   - Used popular libraries like NumPy and SciPy.
   - Can mix image processing with data analysis, machine learning, or math easily.

2. **Has Many Built-in Image Tools**  
   - Can do lots of things: blur, sharpen, resize, detect edges, find shapes, and more.
   - It's like a toolbox for images where everything you need is included.

3. **Easy to See What user's Doing**  
   - It works with matplotlib so user can easily show images and results.
   - Great for learning and testing what happens when user change the settings.

4. **Beginner-Friendly and Well-Documented**  
   - Lots of examples and guides to help user get started.
   - Simple to understand even if user are new to image processing.

5. **Lightweight and Easy to Install**  
   - Pure Python because it is not complicated to setup.
   - Works on Windows, Mac, and Linux.

**Example code processing image using Scikit-image tools**

```
from skimage import io, color
from skimage.transform import rotate
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the original image
image_path = r'C:\Users\USER\cat.png'  # Change this path as needed
original_image = io.imread(image_path)

# Step 2: Handle RGBA images by removing the alpha channel
if original_image.shape[2] == 4:
    original_image = original_image[:, :, :3]

# Step 3: Convert to grayscale
grayscale_image = color.rgb2gray(original_image)

# Step 4: Flip the image horizontally
flipped_image = np.fliplr(original_image)

# Step 5: Crop the image (e.g., top-left 150x150 region)
cropped_image = original_image[0:150, 0:150]

# Step 6: Rotate the image by 45 degrees
rotated_image = rotate(original_image, angle=45, mode='reflect')

# Step 7: Display all images in a neat and organized way
fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # 2 rows, 3 columns for the images

# Display Original Image
axs[0, 0].imshow(original_image)
axs[0, 0].set_title("Original")
axs[0, 0].axis('off')

# Display Grayscale Image
axs[0, 1].imshow(grayscale_image, cmap='gray')
axs[0, 1].set_title("Grayscale")
axs[0, 1].axis('off')

# Display Flipped Image
axs[0, 2].imshow(flipped_image)
axs[0, 2].set_title("Flipped Horizontally")
axs[0, 2].axis('off')

# Display Cropped Image
axs[1, 0].imshow(cropped_image)
axs[1, 0].set_title("Cropped")
axs[1, 0].axis('off')

# Display Rotated Image
axs[1, 1].imshow(rotated_image)
axs[1, 1].set_title("Rotated by 45°")
axs[1, 1].axis('off')

# Remove the empty subplot (axs[1, 2])
axs[1, 2].axis('off')

# Adjusting space between subplots (further decreased spacing)
plt.subplots_adjust(hspace=0.15, wspace=0.15)  # Slightly decreased horizontal and vertical spacing

# Show the final layout
plt.tight_layout()
plt.show()

```

**Output**


<img width="959" alt="image" src="https://github.com/user-attachments/assets/1a1cb70e-afa6-4986-a5f1-af773424384b" />



