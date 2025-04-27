<h4> NAME : NUR ALIEYA BALQIS BT ADNAN</h4>
<h4> CLASS : CDCS2554A </h4>
<h4> STUDENT ID :2023491746</h4> 


<h2> 2503 - ITT450 (INDIVIDUAL ASSIGNMENT) </h2>
<h2> TITTLE : CVG & IMAGE PROCESSING WITH PYTHON </h2> <br>


**<h3>OBJECTIVES :</h3> <br>**

- To understand the concepts of CVG &  Image Processing. <br>
- To apply Python libraries such as Pillow,OpenCV,NumPy for manipulating and analyzing images.<br><br>
**<h3>Library : Pillow (PIL)</h3><br>**

![pillow-logo](https://github.com/user-attachments/assets/acde27e7-5628-4bbf-9905-597be439ff1a)

**<h3>What is image processing ?</h3>** 


Image processing is a method that is used to perform operations of an image such as manipulation and analyze images.It is used to perform tasks like image enhancement,restoration,compression,extraction and recognition.Image processing is divided into two types which is analog image processing that is involves the physical form and digital image processing that is using computer and algorithm.To perform the tasks, it requires on many libraries, including scikit-image,OpenCv, and Pillow.<br><br>


**<h3>What is Pillow ?</h3>** 
	
 Python Pillow is an open-source image processing library 
 that allows us to open,manipulate images and do basic performance of image processing tasks in many image formats .The Python Pillow library is a fork of an older and original library which is called as PIL.Pillow is generally employed for exploratory work and high-performance image processing tasks that don't demand complex image processing skills.It is a flexible tool for various kinds of image processing tasks since it gives us a simple way to open, edit, and save photos in various file formats. <br><br>

**<h3>Characteristics of Pillow</h3>**

**- Image processing operations  :**
  Used to resize,crop,rotate and flip images.In addition to creating drawing like lines,ellipses,rectangles, triangles and more,users may also can add text on the images.<br>

**- Image filtering and conversion  :**
  Convert images to different colour modes such as RGB,CMYK and RGBA.Further, it can change or add effects like contour,detail,blur and sharpen to selected images.<br>

**- Advanced image transformations :**
  Provide powerful imagine manipulation and support image transformations like projective transformations.<br> 

**- Format support :**
  Support a wide range of image formats such as PNG,JPEG,GIF,TIFF,BMP and more which can allow users to perform simple tasks like open,edit and save the image in selected file format. <br>

**- Integration with other Libraries :**
  Pillow enables users access to individual pixels, offering comprehensive image manipulation and analysis. It may be used with other Python libraries, like OpenCV, scikit-image, Mathotas, NumPy, and others, to expand its range of functionality and make it a more powerful library.<br><br>



**<h3>Advantanges of Pillow</h3>** 

**- Simple and user-friendly :**
  Provides a simple and easy to use API that developers can easily understand and use. Its simple syntax and fully described features make image processing procedures more effective.

**- Wide Image Manipulation Functions :**
  Offers a wide range of image processing features, such as adjusting colors, cropping, resizing, rotation, and filter implementation. Users can do both simple and complex image processing tasks because of to these functionalities.

**- Cross-platform compatibility:**
  Can be run on various platforms such as Windows,macOS and Linux.This means that despite of the platform, users can put it into their projects with easily.

**- Open source :**
  Pillow is openly accessible and can be customized with custom functionalities. This enables users to customize the library according to their specific needs while taking part in its ongoing development.<br><br>


**<h3>Basic image proceesing functions :</h3>** 

The Pillow library provides a wide range of basic image processing functions that are simple and easy to use for doing the tasks. In addition to these features, Pillow is a powerful yet user-friendly tool for image editing, transformation, and analysis.

<ol>
  <li>Image.open("example.jpg") </li>
	
  <li>img.save("copy.png") </li>
  
  <li>img.resize((width, height))</li>
  
  <li> img.crop((left, top, right, bottom))</li>

   <li> img.rotate(degrees) 
	<em>- //degrees can be 15,30,45,90 or others</em> </li> 
	
  <li> img.convert("RGB")   
	<em>- //change colour modes like RGB,L(grayscales) or RGBA</em> </li>
  
  <li>img.filter(ImageFilter.BLUR)  
	<em>- //apply built-in filters such as blur,sharpen and contour</em> </li>
  
  <li> ImageEnhance.Brightness(img)  
	<em>- //adjust brightness, contrast, sharpness, and color.</em> </li>
 
</ol> <br>

**<h3>Library related to Pillow (PIL)</h3>** 

A fork of the original Python Imaging Library (PIL), Pillow is a powerful image processing library for Python. NumPy is the Python library most closely related to Pillow. Basic image processing operations like opening, saving, resizing, cropping, and adding basic filters are the main uses for Pillow. With the use of NumPy, you could convert Pillow images into numerical arrays or grids of pixel values that can then be worked with using powerful numerical operations.<br>

**<h3>Editor for Pillow</h3>**

![images](https://github.com/user-attachments/assets/3c52c2f6-24cc-426f-9246-8aad51f1f5d7)


Jupyter Notebook is an easy-to-use and friendly user editor application that can be used together with Pillow to do image processing tasks. We can write and run Pillow image processing code using “cells.” They also will compare the before and after processed images in one notebook.

**<h2>Code for image processing </h2>**

```python

from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

#open image
img = Image.open('cat.jpg')

#crop image
crop_box = (100, 100, 400, 400)
img_cropped = img.crop(crop_box)

#convert grayscale
img_gray = img.convert('L')

#apply Sepia Tone
def apply_sepia(image):
    width, height = image.size
    pixels = np.array(image)
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[j, i]
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            pixels[j, i] = (min(tr, 255), min(tg, 255), min(tb, 255))
    return Image.fromarray(pixels)

img_sepia = apply_sepia(img)

#apply sharpen filter
img_sharpened = img.filter(ImageFilter.SHARPEN)

#rotate the image
img_rotated = img.rotate(45)

#cropped image
plt.subplot(3, 3, 2)
plt.imshow(img_cropped)
plt.title('Cropped Image')
plt.axis('off')

#grayscale image
plt.subplot(3, 3, 3)
plt.imshow(img_gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

#Sepia image
plt.subplot(3, 3, 4)
plt.imshow(img_sepia)
plt.title('Sepia Image')
plt.axis('off')


#sharpened image
plt.subplot(3, 3, 7)
plt.imshow(img_sharpened)
plt.title('Sharpened Image')
plt.axis('off')

#rotated image
plt.subplot(3, 3, 8)
plt.imshow(img_rotated)
plt.title('Rotated Image')
plt.axis('off')

plt.tight_layout()
plt.show()

#save all processed images
img_cropped.save('photo_cropped.jpg')
img_gray.save('photo_gray.jpg')
img_sepia.save('photo_sepia.jpg')
img_sharpened.save('photo_sharpened.jpg')
img_rotated.save('photo_rotated.jpg')
```
**<h3>The sample image of the code</h3>**


Original image :
![cat](https://github.com/user-attachments/assets/63a8c3a9-80d8-4934-b53f-53394bc84d09)

Output : <br>
![Screenshot (152)](https://github.com/user-attachments/assets/00341732-230a-4a14-aefe-6158a65b8277)

**<h3>Code Execution Demonstration</h3>**

[![Watch the video](https://img.youtube.com/vi/1ptX7HPaV68/0.jpg)](https://youtu.be/1ptX7HPaV68?si=LWE60vD6Ga2mshNo)

















 







