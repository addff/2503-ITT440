# NAME : NAUFAL BIN MOHAMAD HAPISOL
# STUDENT ID : 2024665804

---

# Image Processing with Imageio

# 1. What is Image Processing?
Image processing is the technique of manipulating and analyzing digital images to enhance their quality, extract useful information, or automate visual tasks. It involves applying mathematical operations and algorithms to images for:

- *Enhancement* (brightness, contrast, sharpening)
- *Restoration* (noise removal, deblurring)
- *Segmentation* (object detection, edge detection)
- *Compression* (reducing file size)
- *Feature extraction* (pattern recognition)
  
#### Image processing is widely used in fields like medicine, robotics, surveillance, and computer vision.

---

# 2. Image Processing with Imageio

<div align="center">
<img align="center" width="200" height="200" src="https://github.com/Naufalhapisol/ITT440/blob/bb28775928d558c23c5118b29c8fcb25e1c8d3be/imageio.png">
   
</div>

ImageIO is a Python library designed for reading and writing various image formats. It provides a simple, efficient way to handle images in scientific and research applications. Unlike OpenCV or PIL, ImageIO supports animated images, medical formats (DICOM), and volumetric data.

---

# 3. How to Install Imageio

You can install Imageio using pip:

   ``` python
   pip install imageio
   ```
For additional plugins (e.g., for medical imaging):
   ``` python
   pip install imageio[ffmpeg]  # For video support
   pip install imageio[dicom]   # For medical images
   ```
---

# 4. How to Use Imageio

a. Reading an Image

   ``` python
   import imageio.v3 as iio

   # Read an image into a NumPy array
   image = iio.imread("image.jpg")  
   print(image.shape)  # (height, width, channels)
   ```
b. Writing / Saving an Image

   ``` python
  import numpy as np

  # Create a random image (NumPy array)
  random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

  # Save the image
  iio.imwrite("random.png", random_image)
   ```
c. Reading Frames from a Video/Gif
   ``` python
  # Read all frames from a GIF
  frames = iio.imread("animation.gif")  

  # Iterate through frames
  for frame in frames:
  print(frame.shape)  # Each frame is a NumPy array
   ```
d. Converting Image Formats
   ``` python
  # Read a PNG and save as JPEG
  image = iio.imread("input.png")  
  iio.imwrite("output.jpg", image)
   ```
---

# 5. Example: Image Processing with ImageIO & NumPy
Let’s apply a grayscale conversion and edge detection (using Sobel filter) on an image.

Step 1: Install Required Libraries
   ``` python
   pip install numpy scikit-image matplotlib
   ```
Step 2: Code Implementation
   ``` python
   import imageio.v3 as iio
import numpy as np
from skimage import filters
import matplotlib.pyplot as plt

# Read image
image = iio.imread("photo.jpg")

# Convert to grayscale
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Apply Sobel edge detection
edges = filters.sobel(gray_image)

# Display results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Edge Detection")
plt.imshow(edges, cmap="gray")

plt.show()
   ```
Output:
- *The left side shows the original image.*
- *The right side shows the edge-detected version.*
  
---

# 6. Conclusion
- *ImageIO is a powerful yet simple library for reading, writing, and converting images in Python.*
- *It works seamlessly with NumPy, SciPy, and scikit-image for advanced processing.*
- *Useful for medical imaging, video processing, and batch image operations.*

