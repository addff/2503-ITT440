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

### 🔧 Step 1: Install Required Libraries
```
pip install numpy pywt matplotlib scikit-image
```
### 🔧Step 2: Import Necessary Libraries
```
import numpy as np
import pywt
import matplotlib.pyplot as plt
from skimage import io
```
### 🔧Step 3: Upload Your Own Image
```
image = io.imread("car.jpeg")
```
### 🔧Step 4: Apply 2D Discrete Wavelet Transform (DWT)
```
coeffs2 = pywt.dwt2(image, 'bior1.3')
LL, (LH, HL, HH) = coeffs2
```
### 🔧Step 5: Display Results of Wavelet Transform
```
plt.figure(figsize=(12, 12))

# Approximation (LL)
plt.subplot(2, 2, 1)
plt.imshow(LL, cmap='gray')
plt.title("Approximation (LL)")
plt.axis('off')

# Horizontal Detail (LH)
plt.subplot(2, 2, 2)
plt.imshow(LH, cmap='gray')
plt.title("Horizontal Detail (LH)")
plt.axis('off')

# Vertical Detail (HL)
plt.subplot(2, 2, 3)
plt.imshow(HL, cmap='gray')
plt.title("Vertical Detail (HL)")
plt.axis('off')

# Diagonal Detail (HH)
plt.subplot(2, 2, 4)
plt.imshow(HH, cmap='gray')
plt.title("Diagonal Detail (HH)")
plt.axis('off')

plt.tight_layout()
plt.show()

```
### final code
```
import numpy as np
import pywt
import matplotlib.pyplot as plt
from skimage import io

# === Upload your own image ===
image = io.imread("car.jpeg")


# Apply 2D discrete wavelet transform (DWT)
coeffs2 = pywt.dwt2(image, 'bior1.3')  # 'bior1.3' is a type of wavelet filter
LL, (LH, HL, HH) = coeffs2  # LL - Approximation coefficients, LH, HL, HH - Detail coefficients

# Display the results of the wavelet transform
plt.figure(figsize=(12, 12))

# Approximation (LL)
plt.subplot(2, 2, 1)
plt.imshow(LL, cmap='gray')
plt.title("Approximation (LL)")
plt.axis('off')

# Horizontal Detail (LH)
plt.subplot(2, 2, 2)
plt.imshow(LH, cmap='gray')
plt.title("Horizontal Detail (LH)")
plt.axis('off')

# Vertical Detail (HL)
plt.subplot(2, 2, 3)
plt.imshow(HL, cmap='gray')
plt.title("Vertical Detail (HL)")
plt.axis('off')

# Diagonal Detail (HH)
plt.subplot(2, 2, 4)
plt.imshow(HH, cmap='gray')
plt.title("Diagonal Detail (HH)")
plt.axis('off')

plt.tight_layout()
plt.show()
```

### RESULTS
Here is the sample output.
![image](https://github.com/user-attachments/assets/2ac39ef5-21eb-4633-9588-52b00ca5583b)






