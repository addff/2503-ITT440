# IMAGE PROCESSING USING PILLOW
#### NAME: SHAZRYNA BINTI ZAILUDIN
#### NO MATRIC: 2023479862
#### GROUP: M3CDCS2554B

---
#### INTRODUCTION

![image alt](https://github.com/inaee/website/blob/e11a3c418b70d08af7a40bab2610633721391291/pillow_picture1.png)
##### IMAGE PROCESSING
Image processing is the technique of performing operations on an image to enhance it, extract useful information, or transform it into another format. It is widely used in fields such as computer vision medical imaging, remote sensing, and photography editing. 

##### PILLOW (PIL)
The Pillow (PIL) package for Python offers strong capabilities for quickly and effectively completing image processing tasks. Pillow allows you to read, edit, crop, resize, rotate, add filters and save photos in a variety of image formats, including JPEG, PNG, and others.  The Python Pillow library is a fork of an older library called PIL. The Python Imaging Library (PIL) was the first library to allow Python to work with images. PIL only supports Python 2 and was deprecated in 2011. According to its creators, Pillow is the amiable PIL fork that supported Python 3 and preserved the library.

#### OBJECTIVES
* To explore and apply advanced image processing techniques using the Pillow library.
  
* To manipulate images through resizing, filtering, rotating, blending, masking, and enhancement.
  
* To automate a series of image operations through Python programming.

#### ADVANTAGES OF USING PILLOW
* **Support multiple image formats:** Easily works with JPEG, PNG, GIF, BMP and more, allowing users to work with almost any type of image file without needing additional converters or tools.
  
* **Easy to learn and use:** Designed with simplicity in mind, providing an intuitive and straightforward API that enables even beginners in Python programming to perform complex image processing tasks easily and quickly.
  
* **Wide range of features:** Rich collection of features such as image resizing, cropping, rotating, filtering, blending, and drawing on images, making it a one-stop solution for both basic and advanced image manipulation needs.
  
* **Easy Integration with other python libraries:** Can be easily combined with other libraries like NumPy, OpenCV and Matplotlib, making it possible to combine powerful image processing with scientific computing, machine learning, or data visualization.
  
* **Lightweight and fast:** Lightweight and efficient, ensuring that applications using it remain fast, responsive, and do not consume excessive memory or processing power.
  
* **Cross-platform compatibility:** Works on Windows, MacOs and Linux, providing flexibility and convenience for developers working in different environments.

#### BASIC OPERATIONS IN PILLOW
1. Open - *image = image.open(‘example.jpg’)*
2. Save - *image.save(‘example.jpg’)*
3. Resized - *resized_image = image.resize((300,300))*
4. Rotated - *rotated_image = image.rotate(90)*
5. Crop - *cropped_image = image.crop((100,100,300,300))*
6. Flip - *flipped _image = image.transpose(image.FLIP_LEFT_RIGHT)*
7. Grayscale - *gray_image = image.convert(‘L’)*
8. Blur - *blurred_image = image.filter(imageFilter.BLUR)*
9. Sharpen - *sharpened_image = image.filter(image.Filter.Sharpen)*
10. Brightness - *enhancer = imageEnhance.Brightness(image)*
11. Contrast - *enhancer = imageEnhance.Contrast(image)*
12. Draw - *draw = imageDraw.Draw(image)*
13. Blended two image - *blended_image = image.blend(image1, image2, alpha = 0.5)*

---

#### INSTALLATIONS
Python Pillow does not come in-built with Python. To install it type the below command in the terminal.
* Windows
```bash
pip install pillow
```
* MacOs & Linux
```bash
pip3 install pillow
```

---

#### CODE FOR IMAGE PROCESSING
```python
from PIL import Image

# 1.Open the image
img = Image.open("input.jpg") 
# Show the image
img.show()

# 2.Open the image
img = Image.open("input.jpg")
# Save the image to a new file
img.save("output.jpg")

# 3.Resize the image (width, height)
resized_img = img.resize((300, 300))  # Resize to 300x300 pixels
# Save the resized image
resized_img.save("resized_output.jpg")

# 4.Rotate the image 90 degrees counter-clockwise
rotated_img = img.rotate(90)
# Save the rotated image
rotated_img.save("rotated_output.jpg")

# 5.Crop the image (left, top, right, bottom)
cropped_img = img.crop((50, 50, 300, 300))
# Save the cropped image
cropped_img.save("cropped_output.jpg")

# 6.Flip horizontally (mirror left ↔ right)
horizontal_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.save("flipped_horizontal.jpg")
# Flip vertically (mirror top ↔ bottom)
vertical_flip = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.save("flipped_vertical.jpg")

# 7.Convert to grayscale
gray_img = img.convert("L")  # "L" stands for luminance (grayscale)
# Save the grayscale image
gray_img.save("grayscale_output.jpg")

# 8.Apply blur filter
blurred_img = img.filter(ImageFilter.BLUR)
# Save the blurred image
blurred_img.save("blurred_output.jpg")

# 9.Apply sharpen filter
sharpened_img = img.filter(ImageFilter.SHARPEN)
# Save the sharpened image
sharpened_img.save("sharpened_output.jpg")

# 10.Create brightness enhancer
enhancer = ImageEnhance.Brightness(img)
# Increase brightness (1.0 = original, >1 = brighter, <1 = darker)
bright_img = enhancer.enhance(1.5)  # Try 0.5 for darker, 2.0 for more bright
# Save the brightened image
bright_img.save("brightness_output.jpg")

# 11.Create contrast enhancer
enhancer = ImageEnhance.Contrast(img)
# Increase contrast (1.0 = original, >1 = more contrast, <1 = less contrast)
contrast_img = enhancer.enhance(1.8)  # Try 0.5 for low contrast, 2.0 for high contrast
# Save the contrast-adjusted image
contrast_img.save("contrast_output.jpg")

# 12.Create a drawing context
draw = ImageDraw.Draw(img)
# Draw a rectangle (left, top, right, bottom)
draw.rectangle([50, 50, 250, 250], outline="red", width=5)
# Draw a circle (bounding box coordinates)
draw.ellipse([100, 100, 300, 300], outline="blue", width=5)
# Draw text on the image
font = ImageFont.load_default()  # Load a default font
draw.text((100, 350), "Sample Text", fill="green", font=font)
# Save the image with drawings
img.save("drawn_output.jpg")

# 13.Open the two images
img1 = Image.open("input1.jpg")
img2 = Image.open("input2.jpg")
# Resize both images to the same size (optional, if images are not the same size)
img1 = img1.resize((400, 400))
img2 = img2.resize((400, 400))
# Blend the images (img1 and img2)
blended_img = Image.blend(img1, img2, alpha=0.5)  # alpha controls the blend ratio
# Save the blended image
blended_img.save("blended_output.jpg")
```

---

#### OUTPUT
