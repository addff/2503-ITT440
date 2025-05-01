<h1>SCIKIT-IMAGE : A POWERFUL TOOL FOR COMPUTER VISION IN PHYTON</h1>
<h2>SHAZLEEN HANI BINTI MOHD SUHAIMI JIMMY (2023261282)</h2>

<h4>Introduction</h4>
Computer vision is a fast-growing area focused on enabling machines to understand visual data. Scikit-image is a widely used open-source Python library for image processing. Built on SciPy, NumPy, and Matplotlib, it offers a broad set of tools for image manipulation, feature extraction, segmentation, and other essential computer vision tasks for researchers, developers, and data scientists.
<h4>Key Features</h4>
Scikit-image has the following main capabilities:


  &nbsp;&nbsp;&nbsp;&nbsp;• Color space conversions, including RGB to LAB, HSV, and grayscale.
  
  &nbsp;&nbsp;&nbsp;&nbsp;• Reading and writing images in a range of formats is known as image I/O.
  
  &nbsp;&nbsp;&nbsp;&nbsp;• Filtering: edge detection, median filters, and Gaussian blur.
  
  &nbsp;&nbsp;&nbsp;&nbsp;• Segmentation: Instruments like as thresholding, active contours, and watersheds.
  
  &nbsp;&nbsp;&nbsp;&nbsp;• Morphological processes: opening, closure, dilation, and erosion.
  
  &nbsp;&nbsp;&nbsp;&nbsp;• Feature extraction: HOG (Histogram of Oriented Gradients), blob detection, and corner detection.
  
  &nbsp;&nbsp;&nbsp;&nbsp;• Geometric changes include resizing, warping, scaling, and rotation.
  
  &nbsp;&nbsp;&nbsp;&nbsp;• Image restoration using deconvolution and denoising.
<h4>Getting Started with Scikit-Image</h4>
  <h5>Installation</h5>
  <h5>Scikit-image can be installed via pip or conda:</h5>
  <code>pip install scikit-image</code> or <code>conda install -c conda-forge scikit-image</code>
  <h5>Basic Image Processing Example</h5>
  &nbsp;&nbsp;&nbsp;&nbspA simple example of loading an image, applying a Gaussian blur, and detecting edges using the Canny edge detector:
  
  &nbsp;&nbsp;&nbsp;<code>import matplotlib.pyplot as plt
  &nbsp;&nbsp;&nbsp;from skimage import io, filters, feature
  &nbsp;&nbsp;&nbsp;# Load an image
  &nbsp;&nbsp;&nbsp;image = io.imread('example.jpg', as_gray=True)
  &nbsp;&nbsp;&nbsp;# Apply Gaussian blur
  &nbsp;&nbsp;&nbsp;blurred = filters.gaussian(image, sigma=1.0)
  &nbsp;&nbsp;&nbsp;# Detect edges using Canny
  &nbsp;&nbsp;&nbsp;edges = feature.canny(blurred, sigma=1.0)
  &nbsp;&nbsp;&nbsp;# Display results
  &nbsp;&nbsp;&nbsp;fig, axes = plt.subplots(1, 3, figsize=(15, 5))
  &nbsp;&nbsp;&nbsp;axes[0].imshow(image, cmap='gray')
  &nbsp;&nbsp;&nbsp;axes[0].set_title('Original Image')
  &nbsp;&nbsp;&nbsp;axes[1].imshow(blurred, cmap='gray')
  &nbsp;&nbsp;&nbsp;axes[1].set_title('Blurred Image')
  &nbsp;&nbsp;&nbsp;axes[2].imshow(edges, cmap='gray')
  &nbsp;&nbsp;&nbsp;axes[2].set_title('Edge Detection (Canny)')
  &nbsp;&nbsp;&nbsp;plt.show()</code>
  <h5>Image Segmentation Example</h5>
  <code>from skimage import filters
  # Apply Otsu's threshold
  threshold = filters.threshold_otsu(image)
  binary = image > threshold
  plt.imshow(binary, cmap='gray')
  plt.title('Binary Image (Otsu Thresholding)')
  plt.show()</code>
<h4>Advantages of Scikit-Image</h4>

  - Free & Open-Source: It is perfect for both commercial and academic use because there are no license fees.
  
  - High-Level Abstractions: Makes complicated processes like feature extraction and segmentation simpler.
    
  - Machine Learning Integration: Scikit-learn is a good tool for training vision-based machine learning models.
    
  - Performance: C/C++ backend optimized for computationally demanding jobs

<h4>Limitations</h4>

  - Limited Support for Deep Learning: Libraries such as TensorFlow or PyTorch are better suited for vision workloads that rely on deep learning.
  
  - Scikit-image is designed for user-friendliness rather than real-time performance, which makes it slower than OpenCV for real-time processing.
<h4>Conclusion</h4>
Scikit-image is a flexible and easy-to-use Python package for image processing.  Regardless of whether you're working on satellite image analysis, medical     imaging, or basic photo processing, scikit-image offers a comprehensive range of tools to do the task quickly.  Its ease of use and compatibility with the Python ecosystem make it a great option for research and experimentation, even though it might not be able to completely replace specialized libraries like OpenCV for real-time applications.
<h4>References</h4>

Image’s documentation#. scikit. (n.d.). https://scikit-image.org/docs/stable/ 

Mirakyan, M. (2023, April 10). Mastering image processing in python with scikit-image - a comprehensive guide to image processing... Medium. https://martinxpn.medium.com/mastering-image-processing-in-python-with-scikit-image-a-comprehensive-guide-to-image-processing-389ced0eb6f2 

(PDF) scikit-image: Image processing in python. (n.d.). https://www.researchgate.net/publication/264197576_scikit-image_Image_processing_in_Python 
  

