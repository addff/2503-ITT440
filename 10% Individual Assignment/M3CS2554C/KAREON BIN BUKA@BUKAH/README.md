# KAREON BIN BUKA@BUKAH

# 🖼️ CVG & Image Processing with Matplotlib (Python)

##  Course: 2503-ITT440  
**Individual Assignment**  


---

##  Objective
- Understand the basics of **Computer Vision, Graphics & Image Processing** (CVG).
- Explore image processing techniques using Python.
- Demonstrate usage of **Matplotlib**, a powerful visualization library in Python.

---

##  What is CVG & Image Processing?

**Computer Vision & Graphics (CVG)** involves enabling computers to interpret and process visual data such as images and videos.  
**Image Processing** is a subset of CVG that focuses on operations like:
- Enhancing images
- Transforming images
- Extracting useful information from visual content

 **Real-world examples**:
- Medical imaging (X-ray enhancements)
- Face detection and recognition
- Autonomous vehicles (lane detection)
- Satellite imagery analysis

---

##  Why Matplotlib?

**Matplotlib** is a Python library used primarily for 2D plotting and image visualization.  
With `matplotlib.pyplot` and `matplotlib.image`, you can:
- Display and save images
- Create grayscale versions
- Visualize color channels
- Apply simple filters and effects

---

##  How to Install

Make sure Python is installed. Then install Matplotlib:

```bash
pip install matplotlib numpy
```

---

## Code (Python)

```bash
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load image
img = mpimg.imread('sample.jpg')

# Display original image
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')
plt.show()

# Convert to grayscale
gray = np.mean(img, axis=2)

plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Apply threshold to create binary image
binary = gray > 0.5  # you can change the threshold

plt.imshow(binary, cmap='gray')
plt.title("Binary Image")
plt.axis('off')
plt.show()

# Save images
plt.imsave('gray_image.jpg', gray, cmap='gray')
plt.imsave('binary_image.jpg', binary, cmap='gray')
```

---

## Output Preview

- This code will:
- Load and show a color image.
- Convert it to grayscale.
- Convert grayscale into binary.
- Save both new images.
- Example inputs: sample.jpg

---

## Video Demonstration



---

## Conclusion

In this assignment, I learned:

- How matplotlib can be used not just for plots, but also for basic image processing.
- How to visualize and convert color images into grayscale and binary formats.
- How to use NumPy arrays to manipulate pixel data.
- gg
