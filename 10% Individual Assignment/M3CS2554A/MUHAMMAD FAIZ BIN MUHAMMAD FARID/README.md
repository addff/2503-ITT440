NAME : MUHAMMAD FAIZ BIN MUHAMMAD FARID

STUDENT ID : 2023870676

CLASS : CDCS255 4A

# TITTLE :INTRODUCTION TO IMAGE PROCESSING BY USING IMAGEIO
# INTRODUCTION
What is image processing ?
----
Image processing is the field of computer science and engineering focused on performing operations on image to enhace them, extraxt useful information or prepare them for further analysis, it involve techniques that take an image as input,process it and produce either a modified version of the image or information realted to the original image.

What is imageio ?
----
Imageio is a phython library designed for reading and writing a wide range image and video formats in a simple and cosistant way.It allows users to load images from file,URLs or bytes streams and save them in variety of formats such as PNG, JPEG,TIFF and MP4. Imageio is built to be an easy platform to use while still being one of the most powerful and flexible, making it ideal for tasks in image processing. It is a popular choice for both beginner and advanced users in the Phython.

Main website: ( https://imageio.readthedocs.io/ )

It can be install directly from PyPI using pip by using this basic comand :

..

    $ pip install imageio


What can imageio do ?
----
1. Read images
   - image can open and read image files in many formats like PNG,JPEG,BMP,and TIFF.
   - Examples :
   
  ..
  
    $  import imageio
    #  img = imageio.imread('photo.jpg')


2. Write image
   - it can save images to different file formats.
   - Examples:

..

    $ imageio.imwrite('edited.png', img)

3. Read and write Videos
   - read video frames one by one or save series of images as a video.
   - examples:
     
  ..
  
    $  reader = imageio.get_reader('video.mp4')
    $  for frame in reader:
          # Process each frame

      
4. Handle Animated Images
  - It can extract and process each frame from GIF files and create animated GIFs by saving a        sequence of images.
  - exmaples:

   ..
    
     $ gif = imageio.mimread('animation.gif')
      

5. Work with Volumetric Data
  - Imageio supports 3D image stacks like multi-page TIFF or medical images (e.g., DICOM).
    
6. Read from URLs or Stream
  - It can read images directly from URLs or in-memory bytes streams.
  - exmaples:
    
  ..
  
    $ img = imageio.imread('https://example.com/image.jpg')

# Library Related to imageio
``imageio`` work closely with several ohter libraries to read and write images and videos. These libraries act as backbends that imageio uses to handle specific file formats. Such as ``Pillow`` was use to handle common images cause it popular library for opening many different file format. ``MumPy`` also use by imageio to return image as NumPy array to make it easy to process image mathematically.

# Terminology of imageio
1.imageio.core
----
The user-facing APIs (legacy + v3) and plugin manager. You send requests to iio.core and it uses a set of plugins to figure out which backend to use to fullfiled your request. it does so by searching a matching plugin or by sending the request to the plugin you specificed explicity. 

2.imageio.plugin
----
it act as an adapter or wrapper between the core and a backend library. it reponsible for translating request from iio.core into a sequence of operations that the backend ca execute (reading or writing). it also knowns if it associated backend library is isntalled or missing. if the backend ins't installed, the plugin will gracefully deactivate itself to avoud error.
as examples :
- ``imageio.plugins.pillow``– Uses the Pillow backend for standard image formats (PNG, JPG, etc.)
- ``imageio.plugins.ffmpeg`` – Handles reading/writing of video formats using FFmpeg.
- ``imageio.plugins.freeimage`` – Legacy plugin for many image formats (deprecated in newer
  versions).
- ``imageio.plugins.tifffile`` – For handling multi-page TIFF images.
- ``imageio.plugins.dicom`` – For medical DICOM image files (if installed).

3.Backend Library
----
A (potentially 3rd party) library that can read and write image data. every backen is optional, so it up the users to choose which backends they install depending on what file formats or feature they need.

4.ImageResource
----
The data source for images, usually a file, but could also be from the web (HTTP) or memory (file-like objects).

# integrated Development enviroment (IDE) by imageio
imageio is a library and odes not come with its own (IDE). Homever , it is designed to be used within any standard Phython IDE or code editor such as PyCharm, VS Code, Spyder, Thonny/IDLE and Jupyter Notebook/ JupyterLab. as examples from Jupyter Notebookthat suite for interaction image processing, visualizations, and quick testing :

..

    $ import imageio.v3 as iio
    $ import matplotlib.pyplot as plt
  
    $ img = iio.imread('photo.jpg')
    $ plt.imshow(img)
    $ plt.show()

# Phython code example using imageio for basic image processing
This example use NumPy for pixel manipulation and Matplotlib for displaying the images. The code will do :
- Loads an image using Imageio.
- Converts it to grayscale.
- Applies a simple Sobel edge detection filter.
- Saves the result.
- Displays original, grayscale, and processed images side by side.
  
..

    import imageio.v3 as iio
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Step 1: Read the image
    img = iio.imread("example.jpg")  # Replace with your image path
    
    # Step 2: Convert to grayscale using a weighted sum formula
    def rgb2gray(rgb):
        return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    
    gray_img = rgb2gray(img)
    
    # Step 3: Apply a basic edge detection (Sobel filter)
    def simple_edge_detect(gray):
        # Sobel filter kernels
        Kx = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])
    
        Ky = np.array([[1, 2, 1],
                       [0, 0, 0],
                       [-1, -2, -1]])
    
        # Pad image
        padded = np.pad(gray, ((1, 1), (1, 1)), mode='constant')
    
        # Create output
        G = np.zeros_like(gray)
    
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                region = padded[i:i+3, j:j+3]
                gx = np.sum(Kx * region)
                gy = np.sum(Ky * region)
                G[i, j] = np.sqrt(gx**2 + gy**2)
    
        # Normalize
        G = (G / np.max(G)) * 255
        return G.astype(np.uint8)
    
    edges = simple_edge_detect(gray_img)
    
    # Step 4: Save the result
    iio.imwrite("edges_output.png", edges)
    
    # Step 5: Display original and processed images
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.axis("off")
    
    plt.subplot(1, 3, 2)
    plt.title("Grayscale")
    plt.imshow(gray_img, cmap="gray")
    plt.axis("off")
    
    plt.subplot(1, 3, 3)
    plt.title("Edge Detection")
    plt.imshow(edges, cmap="gray")
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()
