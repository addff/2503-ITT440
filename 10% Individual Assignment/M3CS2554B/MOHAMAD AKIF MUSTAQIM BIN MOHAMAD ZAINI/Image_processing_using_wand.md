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

#### Installation and Setup

To use Wand and ImageMagick, follow these installation steps:

1. **Install ImageMagick**  
   ImageMagick is a command-line tool for image manipulation, and Wand uses it as a backend. You can install ImageMagick by following the instructions for your operating system:  
   - **Windows**: Download the installer from [ImageMagick Downloads](https://imagemagick.org/script/download.php) and ensure that you select the option to install legacy utilities.
   - **macOS**: You can install ImageMagick using Homebrew:  
     ```bash
     brew install imagemagick
     ```
   - **Linux (Ubuntu/Debian)**:  
     ```bash
     sudo apt-get install imagemagick
     ```

2. **Install Wand**  
   After installing ImageMagick, you need to install the Wand library using pip:
   ```bash
   pip install Wand
