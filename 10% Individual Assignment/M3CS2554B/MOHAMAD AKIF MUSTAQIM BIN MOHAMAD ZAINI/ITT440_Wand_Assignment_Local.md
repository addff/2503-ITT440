
# ITT-440  
**10% Individual Assignment**  
**TITLE**: *Image Processing Using Wand*  
**NAME**: Mohamad Akif Mustaqim bin Mohamad Zaini  
**MATRIC NUMBER**: 2023298484  
**GROUP**: M3CS2554B  

---

## 📚 LIBRARY  

### Wand

#### What is Wand?  
Wand is an open-source Python library that acts as a binding to [ImageMagick](https://imagemagick.org/), a powerful image manipulation tool. It allows Python developers to perform image processing tasks like resizing, filtering, converting formats, drawing text, and more — all within Python code. Wand simplifies working with images by providing a Pythonic API to ImageMagick's vast features.

#### Significance  
1. **Image Manipulation**: With Wand, developers can handle image tasks like resizing, rotating, and transforming images.  
2. **Format Conversion**: It supports a variety of image formats, including JPEG, PNG, GIF, TIFF, WEBP, and many others.  
3. **Powerful Filters**: You can apply filters, effects, and even draw text onto images.  
4. **Cross-Platform**: Wand works seamlessly on Windows, macOS, and Linux.  
5. **Free & Open Source**: Like ImageMagick, Wand is free to use and open for contributions.  

---

## ⚙️ Installation and Setup

### 1. Install ImageMagick  
ImageMagick is a command-line tool for image manipulation, and Wand uses it as a backend.

- **Windows**:  
  Download from [ImageMagick Downloads](https://imagemagick.org/script/download.php)  
  Ensure the "Install legacy utilities" option is selected during setup.

- **macOS**:  
  ```bash
  brew install imagemagick
  ```

- **Linux (Ubuntu/Debian)**:  
  ```bash
  sudo apt-get install imagemagick
  ```

### 2. Install Wand  
After installing ImageMagick, install Wand via pip:
```bash
pip install Wand
```

---

## 🖼️ Images

### Wand Library  
[Visit Wand GitHub Repository](https://github.com/emcconville/wand)

### ImageMagick Logo  
![ImageMagick Logo](./imagemagick_logo.png)

---

## ▶️ Video Tutorial

Learn how to use the Wand library with this video tutorial:  
[**Watch on YouTube**](https://youtu.be/NbBo3EIWG_Q?si=rxToA6sIL5pk1I-v)

---

## 🧪 Python Code (Image Processing)

The following code demonstrates how to convert an image to **black & white**, apply **blur**, and **flip** it vertically using Wand.

---

### Code
```python
from wand.image import Image
from wand.display import display

# Load image
with Image(filename='input.jpg') as img:
    # Convert to black & white (grayscale)
    img.type = 'grayscale'
    img.save(filename='output_bw.jpg')
    print("Saved black & white image.")

    # Apply blur
    img.blur(radius=0, sigma=5)
    img.save(filename='output_blur.jpg')
    print("Saved blurred image.")

    # Flip the image vertically
    img.flip()
    img.save(filename='output_flip.jpg')
    print("Saved flipped image.")
```

> **Note**: Replace `'input.jpg'` with your actual image file path.

---

## ✅ Output Description

- **output_bw.jpg**: Grayscale version of the original image.  
- **output_blur.jpg**: Image with a blur effect applied.  
- **output_flip.jpg**: Vertically flipped version of the original image.
