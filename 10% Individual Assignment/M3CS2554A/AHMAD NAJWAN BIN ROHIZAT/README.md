NAME : AHMAD NAJWAN BIN ROHIZAT 

STUDENT ID : 2023273072

CLASS : CDCS2554A

TITLE : INTRODUCTION TO IMAGE PROCESSING USING PGMAGICK IN PYTHON

What is Image Processing ?

Image processing is the process of applying operations to digital images to improve them, extract information from them, or get them ready for other activities like analysis or recognition.  Filtering, resizing, colour modifications, and edge detection are some of the methods used to manipulate pixel values.  These adjustments aid in enhancing the image's quality, emphasising particular aspects, or changing the image's look.  In contrast to computer vision, which seeks to decipher and comprehend visual content, image processing concentrates on making low-level changes to the image itself.  It is extensively utilised in disciplines including machine learning, photography, medical imaging, and surveillance.

What is PGMAGICK ?

![Image Name](https://raw.githubusercontent.com/username/repository/branch/path/to/image.jpg)

pgmagick is a Python wrapper around the GraphicsMagick library, which is a powerful image processing tool. It provides a convenient interface for Python developers to perform advanced image manipulation tasks such as resizing, cropping, format conversion, drawing text and shapes, applying filters, and more.


Significance of pgmagick

GraphicsMagick Backend: It leverages the GraphicsMagick library, which is known for its speed and efficiency in processing images.

Python Interface: pgmagick allows Python developers to access the functionality of GraphicsMagick without needing to work directly with C++ code.

Advanced Image Processing: Like other image manipulation libraries, pgmagick can handle tasks such as format conversion, resizing, blurring, and color adjustments.



Key Features of pgmagick

Image Manipulation: Resize, crop, rotate, and flip images.

Filtering: Apply filters like blur, sharpen, or emboss to improve or modify image quality.

Image Format Conversion: Convert images from one format to another (e.g., PNG to JPEG).

Drawing: Add text, shapes, or lines onto images.

Complex Operations: You can work with more advanced image processing tasks, like handling alpha channels (transparency) or creating image composites.



Module / Subpackage
pgmagick provided through core classes and objects, rather than a large set of subpackages like in bigger libraries. It's designed to be lightweight and closely mirror the C++ GraphicsMagick++ API.

Resize image	    Image.resize(Geometry(width, height))
Crop image	      Image.crop(Geometry(width, height, x_offset, y_offset))
Rotate image	    Image.rotate(angle)
Convert format	  Image.write('output.png') (changes extension)
Blur image	      Image.blur(radius)
Sharpen image	    Image.sharpen(radius)
Change brightness	Image.modulate(brightness, saturation, hue)
Composite images	Image.composite(other_image, Geometry(x, y), CompositeOperator)


ENVIRONMENT AND CODING
Integrated Development Environment (IDE)
images

When it comes to selecting an editor or IDE for image processing tasks using SciPy, the choice ultimately depends on personal preference, project size, and the features you need. In this article, we use Spyder, which is designed for scientific computing and comes with built-in support for SciPy, NumPy, scikit-image (skimage), and Matplotlib making it ideal for image processing. This means we don't need to install these libraries separately, as they are pre-installed.

Python Code Example for Basic Image Processing with SciPy
The following code demonstrates the use of some functions mentioned earlier which is gaussian filter, sobel, and grey dilation :

from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

# Importing image
img = img_as_ubyte(io.imread("Downloads/fruits.png", as_gray=True))

# Applying Gaussian filter
gaussian_filtered = ndimage.gaussian_filter(img, sigma=2)

# Applying Sobel filter for edge detection
sobel_x = ndimage.sobel(img, axis=0) # Vertical direction.
sobel_y = ndimage.sobel(img, axis=1) # Horizontal direction.
sobel_combined = np.hypot(sobel_x, sobel_y) # Combine

# Applying Grey Dilation
dilated_img = ndimage.grey_dilation(img, size=(15, 15))

# Plotting the results
plt.figure(figsize=(20, 6))

# Original picture
plt.subplot(1, 6, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')

# Gaussian Filtered picture
plt.subplot(1, 6, 2)
plt.title("Gaussian Blurred")
plt.imshow(gaussian_filtered, cmap='gray')

# Sobel Fitered / Edge Detection picture
plt.subplot(1, 6, 3)
plt.title("Sobel Edge Detection X")
plt.imshow(sobel_x, cmap='gray')

plt.subplot(1, 6, 4)
plt.title("Sobel Edge Detection Y")
plt.imshow(sobel_y, cmap='gray')

plt.subplot(1, 6, 5)
plt.title("Sobel Edge Detection Combined")
plt.imshow(sobel_combined, cmap='gray')

# Grey Dilation picture
plt.subplot(1, 6, 6)
plt.title("Grey Dilation")
plt.imshow(dilated_img, cmap='gray')

plt.tight_layout()
plt.show()
