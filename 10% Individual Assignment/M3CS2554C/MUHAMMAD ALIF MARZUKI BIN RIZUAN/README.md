NAME: MUHAMMAD ALIF MARZUKI BIN RIZUAN

STUDENT ID: 2024430792

CLASS: M3CS2554C

# About Image Processing
Image processing is the technique of performing operations on digital images to enhance, analyze, or extract useful information. It involves manipulating pixel data through algorithms for tasks like noise reduction, sharpening, edge detection, color correction, and object recognition. The process typically includes loading an image into a numerical format, applying mathematical transformations or filters, and outputting the modified result. Image processing is widely used in fields such as medical imaging (X-rays, MRIs), photography (filters, corrections), computer vision (object detection), and satellite imagery (terrain mapping). Libraries like Pillow (Python), OpenCV, and MATLAB's Image Processing Toolbox provide tools to automate these operations efficiently. The goal can range from simple visual improvements to complex machine learning-based pattern recognition.

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
**Step 1: Install Python (if not already installed)**

- Download Python from [python.org](python.org.)
  
![python-install](https://github.com/user-attachments/assets/de628f57-a0ad-4bac-8097-a51780b105cb)


- Run the installer and check **"Add Python to PATH"**.

- Click **"Install Now"** and complete the setup.
<br/>

**Step 2: Open Command Prompt (CMD)**

Press `Win + R`, type `cmd`, and hit Enter.

<br/>

**Step 3: Upgrade pip (Python Package Manager)**

Run this command to ensure pip is updated:
```bash
python -m pip install --upgrade pip
```
<br/>

**Step 4: Install Pillow**

Run the following command:
```bash
pip install pillow
```
- Wait for the installation to complete.
<br/>

**Step 5: Verify Installation**

Check if Pillow is installed correctly:
```bash
python -c "from PIL import Image; print(Image.__version__)"
```
- If it prints a version number (e.g., `10.0.0`), Pillow is installed successfully.

# Basic Usage Examples
1. Opening and Displaying an Image
```python
from PIL import Image

# Open an image file
img = Image.open('example.jpg')

# Display the image (opens in default viewer)
img.show()

# Get image information
print(f"Format: {img.format}")
print(f"Size: {img.size}")  # (width, height)
print(f"Mode: {img.mode}")  # RGB, CMYK, etc.
```

Prove:

![image](https://github.com/user-attachments/assets/dc04e69f-54fb-4a7e-84b5-a44b9a9378b3)


2. Image Manipulation
```python
from PIL import Image

img = Image.open("Example.jpg")

# Resize an image
img = image.resize((300, 200))

# Rotate an image
img = image.rotate(45)  # degrees

# Crop an image
box = (100, 100, 400, 400)  # left, upper, right, lower
img = image.crop(box)

# Convert to grayscale
img = image.convert('L')

img.show()
```

**Before**

![Example](https://github.com/user-attachments/assets/1d5440e7-8e2d-4a87-a2e0-52bf53b41609)

**After**

![image](https://github.com/user-attachments/assets/603d2948-a892-422b-b5a0-47e6d251133e)

3. Saving Images
```python
from PIL import Image

img = Image.open("Example.jpg")

# Save in different formats
img.save('output1.png')
img.save('output2.jpg', quality=80)
```

Prove:

![image](https://github.com/user-attachments/assets/88cd643a-832b-49c5-9cc1-f524cac3201e)

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

Prove:

![image](https://github.com/user-attachments/assets/307ad13e-3567-4f17-93d8-73fd37d54231)


5. Image Filters
```python
from PIL import Image, ImageFilter

img = Image.open("Example.jpg")

# Apply blur filter
img = img.filter(ImageFilter.BLUR)

# Apply edge enhancement
img = img.filter(ImageFilter.EDGE_ENHANCE)

# Find edges
img = img.filter(ImageFilter.FIND_EDGES)

img.show()
```

Prove:

![image](https://github.com/user-attachments/assets/90741f6e-cdaf-4e2e-8c7b-0c878f85edac)

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

Prove:

![image](https://github.com/user-attachments/assets/92cf5896-5ba2-472e-8a39-1e1e4e42fc4b)


7. Advanced: Blend Two Images
```python
from PIL import Image

img1 = Image.open("example1.jpg")
img2 = Image.open("example2.jpg").resize(img1.size)  # Resize to match

# Blend with 50% opacity
blended = Image.blend(img1, img2, alpha=0.5)
blended.save("blended.jpg")
```

**Before**

![python-install](https://github.com/user-attachments/assets/2a974e74-3e87-4a3e-af52-022e23eed349)
![pillow-logo-248x250](https://github.com/user-attachments/assets/961e096d-1a43-4990-b2f7-c769cb9b744d)

**After**

![blended](https://github.com/user-attachments/assets/1f015dde-5351-4bd6-a4c6-2846e4ad4c1b)



# Advanced Features
- Color manipulation: Adjust brightness, contrast, etc.

- Alpha compositing: Work with transparent images

- EXIF data handling: Read and write metadata

- Batch processing: Apply operations to multiple images

- Advanced transformations: Perspective transforms, etc.

Pillow is widely used in web applications, data analysis (for image data), computer vision preprocessing, and general image manipulation tasks. Its API is intuitive and well-documented, making it a great choice for Python developers working with images.

# Video Explaination


