NAME : NUR AZRIL BIN AZRUL

STUDENT ID : 2023406182

CLASS : CDCS2554A
## TITLE : INTRODUCTION TO IMAGE PROCESSING USING PYWAVELETS IN PYTHON
### What is Image Processing ?
Image processing in Python involves manipulating and analyzing digital images using various libraries and techniques. It is used to enhance images, extract information, and perform various computer vision tasks. Common applications include image enhancement, object detection, image segmentation, and feature extraction.
### What is Pywavelets ?
![Wavelet Tools in Python](https://miro.medium.com/v2/resize:fit:500/1*8mh5bZVmgvgGC5Rj0UN7gg.png)


PyWavelets is a Python library designed for wavelet analysis, which includes image processing. Wavelet transform decomposes an image into different frequency components, enabling various image processing tasks. These tasks include image compression, denoising, feature extraction, and analysis.

The main features of PyWavelets are:

  * 1D, 2D and nD Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
  * 1D, 2D and nD Multilevel DWT and IDWT
  * 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
  * 1D and 2D Wavelet Packet decomposition and reconstruction
  * 1D Continuous Wavelet Transform
  * Computing Approximations of wavelet and scaling functions
  * Over 100 `built-in wavelet filters`_ and support for custom wavelets
  * Single and double precision calculations
  * Real and complex calculations
  * Results compatible with Matlab Wavelet Toolbox (TM)

### Library related to pywavelets ?
While PyWavelets is powerful on its own, it's often used alongside:

- **NumPy** – For numerical array manipulation (PyWavelets depends on it).
- **scikit-image (`skimage`)** – For loading, converting, and preparing image formats.
- **Matplotlib** – To visualize the original and processed images.
- **OpenCV (optional)** – For more advanced image manipulation and pre-processing.

These libraries create a full workflow from image loading, transformation, to display and analysis.

### Module / Subpackage in PyWavelets

PyWavelets offers the `pywt` module with key image processing tools such as:

- `pywt.dwt2()` – 2D Discrete Wavelet Transform
- `pywt.idwt2()` – 2D Inverse Discrete Wavelet Transform
- `pywt.wavedec2()` – Multilevel 2D wavelet decomposition
- `pywt.waverec2()` – Multilevel 2D wavelet reconstruction
- `pywt.threshold()` – For wavelet-based denoising

These functions are used for tasks like image compression, edge detection, and noise reduction through wavelet-based techniques.

### Python Code Example for Basic Image Processing with PyWavelets

## 🌀 Basic Image Processing with PyWavelets

This example demonstrates how to use the PyWavelets library to perform image decomposition and reconstruction using the Haar wavelet.

### 🔧 Step 1: Import Required Libraries

```python
from skimage import io, img_as_float
import pywt
import matplotlib.pyplot as plt
```
### 🔧Step 2: Load the Grayscale Image
```
image = img_as_float(io.imread("Downloads/fruits.png", as_gray=True))
```
### 🔧Step 3: Apply 2D Discrete Wavelet Transform (DWT)
```
coeffs2 = pywt.dwt2(image, 'haar')
cA, (cH, cV, cD) = coeffs2
```
### 🔧Step 4: Reconstruct the Image Using Inverse DWT
```
reconstructed = pywt.idwt2(coeffs2, 'haar')
```
### 🔧Step 5: Display the Results
```
plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title("Approximation (cA)")
plt.imshow(cA, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title("Horizontal Detail (cH)")
plt.imshow(cH, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title("Vertical Detail (cV)")
plt.imshow(cV, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title("Diagonal Detail (cD)")
plt.imshow(cD, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title("Reconstructed Image")
plt.imshow(reconstructed, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
```
### final code
```
from skimage import io, img_as_float
import pywt
import matplotlib.pyplot as plt

# Load and normalize image
image = img_as_float(io.imread("Downloads/fruits.png", as_gray=True))

# Apply 2D Discrete Wavelet Transform
coeffs2 = pywt.dwt2(image, 'haar')
cA, (cH, cV, cD) = coeffs2  # Approximation and detail coefficients

# Reconstruct the image
reconstructed = pywt.idwt2(coeffs2, 'haar')

# Plotting the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(2, 3, 2)
plt.title("Approximation (cA)")
plt.imshow(cA, cmap='gray')

plt.subplot(2, 3, 3)
plt.title("Horizontal Detail (cH)")
plt.imshow(cH, cmap='gray')

plt.subplot(2, 3, 4)
plt.title("Vertical Detail (cV)")
plt.imshow(cV, cmap='gray')

plt.subplot(2, 3, 5)
plt.title("Diagonal Detail (cD)")
plt.imshow(cD, cmap='gray')

plt.subplot(2, 3, 6)
plt.title("Reconstructed Image")
plt.imshow(reconstructed, cmap='gray')

plt.tight_layout()
plt.show()
```


