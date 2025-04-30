## NAME : AHMAD NAJWAN BIN ROHIZAT 

## STUDENT ID : 2023273072

## CLASS : CDCS2554A

## TITLE : INTRODUCTION TO IMAGE PROCESSING USING PGMAGICK IN PYTHON

# What is Image Processing ?

Image processing is the process of applying operations to digital images to improve them, extract information from them, or get them ready for other activities like analysis or recognition.  Filtering, resizing, colour modifications, and edge detection are some of the methods used to manipulate pixel values.  These adjustments aid in enhancing the image's quality, emphasising particular aspects, or changing the image's look.  In contrast to computer vision, which seeks to decipher and comprehend visual content, image processing concentrates on making low-level changes to the image itself.  It is extensively utilised in disciplines including machine learning, photography, medical imaging, and surveillance.

# What is PGMAGICK ?

![Image Name](https://raw.githubusercontent.com/username/repository/branch/path/to/image.jpg)

pgmagick is a Python wrapper around the GraphicsMagick library, which is a powerful image processing tool. It provides a convenient interface for Python developers to perform advanced image manipulation tasks such as resizing, cropping, format conversion, drawing text and shapes, applying filters, and more.


# Significance of pgmagick

GraphicsMagick Backend: It leverages the GraphicsMagick library, which is known for its speed and efficiency in processing images.

Python Interface: pgmagick allows Python developers to access the functionality of GraphicsMagick without needing to work directly with C++ code.

Advanced Image Processing: Like other image manipulation libraries, pgmagick can handle tasks such as format conversion, resizing, blurring, and color adjustments.



# Key Features of pgmagick

Image Manipulation: Resize, crop, rotate, and flip images.

Filtering: Apply filters like blur, sharpen, or emboss to improve or modify image quality.

Image Format Conversion: Convert images from one format to another (e.g., PNG to JPEG).

Drawing: Add text, shapes, or lines onto images.

Complex Operations: You can work with more advanced image processing tasks, like handling alpha channels (transparency) or creating image composites.

# Library Related to pgmagick

The three libraries pgmagick, matplotlib, and NumPy , each play an important role in handling basic image processing in Python. pgmagick is the core image processing library that provides access to powerful features of GraphicsMagick, such as resizing, color manipulation, and applying filters like blur and sharpen. It efficiently processes images at a low level, allowing for high-quality transformations and manipulations. matplotlib complements this by providing a simple yet effective way to visualize the processed images, which is particularly useful for tasks like displaying results, adding annotations, and presenting images in a clear and informative way. Finally, NumPy is used for managing image data as arrays, which is essential for performing pixel-based operations. In this case, it allows for converting the image into a format that can be visualized with matplotlib, making it a critical part of the workflow for manipulating and displaying images in a flexible and computationally efficient manner. Together, these libraries create a powerful yet accessible toolset for working with images in Python.

# Module / Subpackage
pgmagick provided through core classes and objects, rather than a large set of subpackages like in bigger libraries. It's designed to be lightweight and closely mirror the C++ GraphicsMagick++ API.

Resize image	    Image.resize(Geometry(width, height))
Crop image	        Image.crop(Geometry(width, height, x_offset, y_offset))
Rotate image	    Image.rotate(angle)
Convert format	  Image.write('output.png') (changes extension)
Blur image	      Image.blur(radius)
Sharpen image	    Image.sharpen(radius)
Change brightness	Image.modulate(brightness, saturation, hue)
Composite images	Image.composite(other_image, Geometry(x, y), CompositeOperator)


# ENVIRONMENT AND CODING
Integrated Development Environment (IDE)


The decision of which editor or IDE to use for pgmagick image processing jobs ultimately comes down to your needs, project size, and personal preferences.  In this tutorial, we use VS Code, which is fully compatible with Visual Studio Code(VS Code).In fact, VS Code is a great IDE for working with pgmagick and Python image processing projects.



# Python Code Example for Basic Image Processing with pgmagick
The following code demonstrates the use of some functions mentioned earlier which is loading and saving an image, resizing, cropping, rotating, blurring, changing brightness or saturation, drawing text and shapes and compositing images :

from pgmagick import (
    Image, Geometry, Color, DrawableText, DrawableFillColor,
    DrawableStrokeColor, DrawableRectangle, ImageList
)

--- 1. Load the main image ---
img = Image("input.jpg")  # Replace with your image file

--- 2. Resize image ---
img.resize(Geometry(400, 300))  # Resize to 400x300

--- 3. Crop the image (100x100 from top-left corner) ---
img.crop(Geometry(100, 100, 0, 0))

--- 4. Rotate the image 45 degrees ---
img.rotate(45)

--- 5. Blur the image slightly ---
img.blur(1.0)

--- 6. Adjust brightness (120%), saturation (90%), hue (100%) ---
img.modulate(120, 90, 100)

--- 7. Draw text on image ---
img.draw(DrawableFillColor(Color("white")))
img.draw(DrawableStrokeColor(Color("black")))
img.draw(DrawableText(10, 90, "Hello, pgmagick!"))

--- 8. Draw a red rectangle ---
img.draw(DrawableStrokeColor(Color("red")))
img.draw(DrawableFillColor(Color("transparent")))  # Only border
img.draw(DrawableRectangle(10, 10, 80, 80))

--- 9. Composite with another image (overlay) ---
overlay = Image("overlay.png")  # Must be same or smaller size
img.composite(overlay, Geometry(10, 10))  # Place at top-left corner

--- 10. Save the final result ---
img.write("output.jpg")

