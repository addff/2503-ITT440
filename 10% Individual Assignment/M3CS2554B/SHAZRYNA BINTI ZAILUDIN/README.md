# IMAGE PROCESSING USING PILLOW
#### NAME: SHAZRYNA BINTI ZAILUDIN
#### NO MATRIC: 2023479862
#### GROUP: M3CDCS2554B

---
##### INTRODUCTION

![image alt](https://github.com/inaee/website/blob/e11a3c418b70d08af7a40bab2610633721391291/pillow_picture1.png)
###### IMAGE PROCESSING
Image processing is the technique of performing operations on an image to enhance it, extract useful information, or transform it into another format. It is widely used in fields such as computer vision medical imaging, remote sensing, and photography editing. 

###### PILLOW (PIL)
The Pillow (PIL) package for Python offers strong capabilities for quickly and effectively completing image processing tasks. Pillow allows you to read, edit, crop, resize, rotate, add filters and save photos in a variety of image formats, including JPEG, PNG, and others.  The Python Pillow library is a fork of an older library called PIL. The Python Imaging Library (PIL) was the first library to allow Python to work with images. PIL only supports Python 2 and was deprecated in 2011. According to its creators, Pillow is the amiable PIL fork that supported Python 3 and preserved the library.

##### OBJECTIVES
* To explore and apply advanced image processing techniques using the Pillow library.
* To manipulate images through resizing, filtering, rotating, blending, masking, and enhancement.
* To automate a series of image operations through Python programming.

##### ADVANTAGES OF USING PILLOW
* **Support multiple image formats:** Easily works with JPEG, PNG, GIF, BMP and more, allowing users to work with almost any type of image file without needing additional converters or tools.
* **Easy to learn and use:** Designed with simplicity in mind, providing an intuitive and straightforward API that enables even beginners in Python programming to perform complex image processing tasks easily and quickly.
* **Wide range of features:** Rich collection of features such as image resizing, cropping, rotating, filtering, blending, and drawing on images, making it a one-stop solution for both basic and advanced image manipulation needs.
* **Easy Integration with other python libraries:** Can be easily combined with other libraries like NumPy, OpenCV and Matplotlib, making it possible to combine powerful image processing with scientific computing, machine learning, or data visualization.
* **Lightweight and fast:** Lightweight and efficient, ensuring that applications using it remain fast, responsive, and do not consume excessive memory or processing power.
* **Cross-platform compatibility:** Works on Windows, MacOs and Linux, providing flexibility and convenience for developers working in different environments.

##### BASIC OPERATIONS IN PILLOW
1. Open - *image = image.open(‘example.jpg’)*
2. Resized - *resized_image = image.resize((300,300))*
3. Rotated - *rotated_image = image.rotate(90)*
4. Crop - *cropped_image = image.crop((100,100,300,300))*
5. Flip - *flipped _image = image.transpose(image.FLIP_LEFT_RIGHT)*
6. Grayscale - *gray_image = image.convert(‘L’)*
7. Blur - *blurred_image = image.filter(imageFilter.BLUR)*
8. Sharpen - *sharpened_image = image.filter(image.Filter.Sharpen)*
9. Brightness - *enhancer = imageEnhance.Brightness(image)*
10. Contrast - *enhancer = imageEnhance.Contrast(image)*
11. Draw - *draw = imageDraw.Draw(image)*
12. Blended two image - *blended_image = image.blend(image1, image2, alpha = 0.5)*
13. Save - *image.save(‘example.jpg’)*

