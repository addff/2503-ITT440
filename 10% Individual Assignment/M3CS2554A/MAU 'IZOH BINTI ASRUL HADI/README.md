NAME : MAU'IZOH BINTI ASRUL HADI

STUDENT ID : 2023298852

CLASS : CDCS2554A
## TITLE : INTRODUCTION TO IMAGE PROCESSING USING SCIPY IN PYTHON
### What is Image Processing ?
Image processing refers to the process of manipulating and enhancing digital images. Using computer algorithms, it is mainly applied to extract useful information, improve image quality and prepare images for future use. It plays a crucial role in various industries, such as security systems where it is used for facial recognition. This highlights how image processing has become an essential tool in both current and future world. 
![scipy-bids-project-banners-template-ob-people-1 5-1-ratio-rectangle](https://github.com/user-attachments/assets/2bb4894c-5e72-408e-9450-7ad0eb23dd58)
### What is SciPy ?
SciPy is a free and open-source library in Python that is built on top of Numpy. It is widely used for scientific and technical computing, including multidimensional image processing. This library extends Python's capabilities by offering high-level functions and classes that are especially useful for data analysis, scientific computation, and image processing tasks. In the context of image processing, SciPy provides tools that are both powerful and accessible, making it an excellent choice for researchers, developers, and engineers working with multidimensional image data.
### Significance of SciPy
- **Free and open-source**: Making it accessible for everyone which is beneficial for image processing where experimentation and frequent testing are required without having to pay any license fees.
- **Enable various operations**: An extensive range of functions are available for image processing tasks which are essential for enhancing, analyzing, and preparing images for further use.
- **Plays critical role**: Widely used among the scientific and engineering community that is heavily relying on image-based data, specifically medical imaging like MRI scans.
- **Extend Python capabilities**: Python does not include specialized image manipulation tools by default. When using modules in SciPy like scipy.ndimage, it expands Python’s funtionality and enables users to analyze multidimensional image data accurately and easily.
- **User-friendly**: Designed to be beginner-friendly, especially for people who are already familiar with NumPy or even for users who are unfamiliar with image processing since its clear syntax and well-documented capabilities make it simple to understand and use.
### Library Related to SciPy
Even though SciPy’s module has powerful image processing capabilities, it mainly depends on **NumPy** for array manipulation with all of NumPy’s functions included in it . Moreover, in order to view processed images, it is necessary to use external libraries such as **Matplotlib**. Hence, SciPy is usually used with other libraries to create a comprehensive workflow for image processing.
### Module / Subpackage
SciPy offers a specifically designed module for image processing and analysis functions, which called .ndimage. This subpackage provide variety of functions including linear and non-linear filtering, object measurements, interpolation and binary morphology. Below are a few of basic image processing functions : 
1) gaussian_filter(input, sigma[, order, ...])
2) median_filter(input[, size, footprint, ...])
3) sobel(input[, axis, output, mode, cval])
4) maximum_position(input[, labels, index])
5) minimum_position(input[, labels, index])
### Integrated Development Environment (IDE)
![images](https://github.com/user-attachments/assets/32ccb994-634d-4d1a-a56b-0a7faa691361)

When it comes to selecting an editor or IDE for image processing tasks using SciPy, the choice ultimately depends on personal preference, project size, and the features you need. In this article, we use **Spyder**, which is designed for scientific computing with built-in support for SciPy, NumPy, and Matplotlib, making it ideal for image processing.
### Python Code Example for Basic Image Processing with SciPy


