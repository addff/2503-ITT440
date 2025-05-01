## NAME : AHMAD NAJWAN BIN ROHIZAT 

## STUDENT ID : 2023273072

## CLASS : CDCS2554A

## TITLE : INTRODUCTION TO IMAGE PROCESSING USING PYVIPS IN PYTHON

# What is Image Processing ?

Image processing is the process of applying operations to digital images to improve them, extract information from them, or get them ready for other activities like analysis or recognition.  Filtering, resizing, colour modifications, and edge detection are some of the methods used to manipulate pixel values.  These adjustments aid in enhancing the image's quality, emphasising particular aspects, or changing the image's look.  In contrast to computer vision, which seeks to decipher and comprehend visual content, image processing concentrates on making low-level changes to the image itself.  It is extensively utilised in disciplines including machine learning, photography, medical imaging, and surveillance.

# What is Pyvips?

pyvips is a Python binding for the libvips image processing library, known for its high speed, low memory usage, and ability to handle large images efficiently. Unlike traditional image libraries that load entire images into memory, pyvips uses lazy evaluation and streaming to process images in chunks. This makes it especially useful for large-scale or server-side applications, such as batch processing, web services, and scientific imaging. pyvips is widely used in domains where performance and scalability are critical.

# Significance of pyvips

✅ Fast and efficient           : Processes large images significantly faster than PIL or OpenCV.

✅ Low memory usage             : Uses streaming and avoids loading full images into RAM.

✅ Handles very large images    : Ideal for gigapixel images or image pyramids.

✅ Scalable                     : Suitable for cloud/image servers where speed and memory efficiency are critical.

✅ Versatile format support      : Handles JPEG, PNG, TIFF, WebP, OpenEXR, SVG, PDF, and more.



# Key Features of pyvips

🧠 Lazy evaluation: Operations are queued until needed.

📉 Streaming pipeline: Efficient processing of image data.

✂️ Advanced image operations: Resize, crop, rotate, flip, blend, sharpen, etc.

🔄 Color space conversion: Support for ICC profiles and color manipulation.

🗂️ Support for multi-page images: PDF, TIFF pages, etc.

🔁 Multi-threading: Uses multiple cores efficiently.


# Module / Subpackage
pyvips is a single module, but it interacts with the core vips operations underneath. You typically use:

import pyvips

Load an image
image = pyvips.Image.new_from_file("input.jpg")

Resize the image to 50%
resized = image.resize(0.5)

Convert to grayscale (by averaging RGB channels)
grayscale = image.colourspace("b-w")

Rotate 90 degrees clockwise
rotated = grayscale.rot90()

brighter image
brighter=image.linear(1.2,10)

sharpen or blur
sharpened = image.sharpen()
blurred = image.gaussblur(2.0)

overlay images 
blended = image1.composite2(image2, "over")
Write result
resized.write_to_file("output.jpg")

# ⚙️ How pyvips Works
Step 1: Lazy loading
pyvips doesn't load the full image immediately. It reads metadata and defers processing.

Step 2: Processing pipeline
When you apply operations like resize() or crop(), it builds a computation graph.

Step 3: Execution
When write_to_file() or .numpy() is called, pyvips processes the image through the pipeline efficiently, using multi-threaded and streamed processing.

# ENVIRONMENT AND CODING
Integrated Development Environment (IDE)


The decision of which environment to use for pyvips image processing tasks ultimately depends on your project requirements, familiarity, and workflow preferences. In this tutorial, we use the Windows Command Prompt (CMD), which is fully compatible with Python and pyvips. In fact, CMD is a simple and effective environment for running pyvips scripts, especially when working on batch image processing or automated workflows. It allows direct interaction with Python files and provides easy access to file paths, system variables, and tools like vips, making it a practical choice for streamlined development and testing with pyvips.

# 💾 How to Install pyvips (Windows)
1. Install libvips:

Download from https://github.com/libvips/libvips/releases

Extract to C:\vips

Add C:\vips\bin to your system PATH environment variable.

2. Install pyvips via pip:

pip install pyvips

3.Verify:
vips --version
python -c "import pyvips; print(pyvips.__version__)"

# Python Code Example for Basic Image Processing with pyvips
The following code demonstrates the use of some functions mentioned earlier which is loading and saving an image, resizing, rotating, changing brightness, convert grayscale, sharpen or blur and overlay images :

import pyvips

Load the original image
image = pyvips.Image.new_from_file(r'C:\images\input.jpg')

Resize the image to 50%
resized = image.resize(0.5)

Convert to grayscale (by averaging RGB channels)
grayscale = image.colourspace("b-w")

Rotate 90 degrees clockwise
rotated = grayscale.rot90()

brighter image
brighter=image.linear(1.2,10)

sharpen or blur
sharpened = image.sharpen()
blurred = image.gaussblur(2.0)

overlay images 
blended = image1.composite2(image2, "over")

Save the processed image as PNG
rotated.write_to_file(r'C:\images\output_rotated.png')


# ▶️ Video Tutorial
Learn how to use the pyvips with this video tutorial: [LETS PROCESSING A CAT](https://youtu.be/xTWOyH7wleQ)

