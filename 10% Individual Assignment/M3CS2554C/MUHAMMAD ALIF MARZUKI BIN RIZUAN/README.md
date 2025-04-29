NAME: MUHAMMAD ALIF MARZUKI BIN RIZUAN

STUDENT ID: 2024430792

CLASS: M3CS2554C
# Pillow (PIL Fork) - Python Imaging Library

![pillow-logo-248x250](https://github.com/user-attachments/assets/9c35053e-a575-487a-8939-6372c92b7395)

Pillow is a friendly fork of the Python Imaging Library (PIL), which adds support for opening, manipulating, and saving many different image file formats. It's a powerful library for image processing in Python.

# Key Features of Pillow
- Supports a wide range of image formats (JPEG, PNG, GIF, BMP, TIFF, etc.)

- Basic image operations (cropping, rotating, resizing, etc.)

- Image filtering and enhancement

- Color space conversions

- Drawing on images

- Text rendering

- Image sequence handling (for animations)

# Installation
```bash
pip install pillow
```

# Basic Usage Examples
1. Opening and Displaying an Image
```python
from PIL import Image

# Open an image file
image = Image.open('example.jpg')

# Display the image (opens in default viewer)
image.show()

# Get image information
print(f"Format: {image.format}")
print(f"Size: {image.size}")  # (width, height)
print(f"Mode: {image.mode}")  # RGB, CMYK, etc.
```

2. Image Manipulation
```python
# Resize an image
resized = image.resize((300, 200))

# Rotate an image
rotated = image.rotate(45)  # degrees

# Crop an image
box = (100, 100, 400, 400)  # left, upper, right, lower
cropped = image.crop(box)

# Convert to grayscale
grayscale = image.convert('L')
```

3. Saving Images
```python
# Save in different formats
image.save('output.png')
image.save('output.jpg', quality=85)  # specify JPEG quality
```

4. Drawing on Images
```python
from PIL import Image, ImageDraw, ImageFont

# Create a blank image
img = Image.new('RGB', (500, 300), color='white')

# Initialize drawing context
draw = ImageDraw.Draw(img)

# Draw a rectangle
draw.rectangle([(100, 100), (400, 200)], fill='blue', outline='red')

# Draw text
font = ImageFont.truetype('arial.ttf', size=36)
draw.text((150, 150), 'Hello Pillow!', fill='white', font=font)

img.show()
```

5. Image Filters
```python
from PIL import ImageFilter

# Apply blur filter
blurred = image.filter(ImageFilter.BLUR)

# Apply edge enhancement
edge_enhanced = image.filter(ImageFilter.EDGE_ENHANCE)

# Find edges
edges = image.filter(ImageFilter.FIND_EDGES)
```

6. Working with Image Sequences (GIFs)
```python
# Extract frames from a GIF
gif = Image.open('animation.gif')

frames = []
try:
    while True:
        frames.append(gif.copy())
        gif.seek(gif.tell() + 1)
except EOFError:
    pass  # end of sequence

# Save frames as individual images
for i, frame in enumerate(frames):
    frame.save(f'frame_{i}.png')
```

# Advanced Features
- Color manipulation: Adjust brightness, contrast, etc.

- Alpha compositing: Work with transparent images

- EXIF data handling: Read and write metadata

- Batch processing: Apply operations to multiple images

- Advanced transformations: Perspective transforms, etc.

Pillow is widely used in web applications, data analysis (for image data), computer vision preprocessing, and general image manipulation tasks. Its API is intuitive and well-documented, making it a great choice for Python developers working with images.
