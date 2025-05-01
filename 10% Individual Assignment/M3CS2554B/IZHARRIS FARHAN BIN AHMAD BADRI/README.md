Name: IZHARRIS FARHAN BIN AHMAD BADRI

Student ID: 2023674644

Group: CS2554B

# Image Processing using Pywavelets

PyWavelets (also known as PyWavelets or the pywt module) is a Python library for wavelet transforms, which are tools used for analyzing and processing signals and images. Wavelet transforms are useful in many areas including signal denoising, image compression, feature extraction, and time-frequency analysis. PyWavelets is widely used in fields like data compression, medical imaging, and digital signal processing. 

## 🔍 Key Features of PyWavelets:
Discrete Wavelet Transform (DWT): For 1D, 2D, and even n-dimensional data.
- `pywt.dw()t`, `pywt.dwt2()`, `pywt.dwtn()`

Inverse Discrete Wavelet Transform (IDWT): Reconstructs original data from wavelet coefficients.
- `pywt.idwt()`, `pywt.idwt2()`, `pywt.idwtn()`

Stationary Wavelet Transform (SWT): A non-decimated version of DWT.
- `pywt.swt()`, `pywt.swt2()`

Multilevel decompositions: Decompose a signal or image into multiple levels of detail.
- `pywt.wavedec()`, `pywt.wavedec2()`

Wavelet families: Supports a wide variety of wavelets, like Haar, Daubechies, Symlets, Coiflets, etc.
- `pywt.Wavelet()`, `pywt.wavelist()`, `pywt.build_wavelet()`

Image processing: Commonly used for image denoising and compression.
- `pywt.threshold()`


## 🛠️ Installation & Setup
### Install PyWavelets matplotlib numpy





## 🔧 Step-by-Step: Image Processing Using PyWavelets

### Basic Workflow Image Processing Denoising with Daubechies Wavelet
```
import pywt
from skimage import data, color, util
import matplotlib.pyplot as plt
```

### Load and noise image
```
image = color.rgb2gray(data.astronaut())
noisy = util.random_noise(image, mode='gaussian')
```

### Wavelet decomposition
```
wavelet = 'db2'
coeffs = pywt.wavedec2(noisy, wavelet, level=2)
```

### Thresholding
```
threshold = 0.08
coeffs_thresh = [(pywt.threshold(c, threshold, mode='soft') if isinstance(c, np.ndarray) else 
                  tuple(pywt.threshold(i, threshold, mode='soft') for i in c)) for c in coeffs]
```

### Reconstruction
```
denoised = pywt.waverec2(coeffs_thresh, wavelet)
```

### Display
```
plt.subplot(1, 2, 1)
plt.imshow(noisy, cmap='gray')
plt.title("Noisy")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(denoised, cmap='gray')
plt.title("Denoised")
plt.axis('off')
plt.tight_layout()
plt.show()
```


## 📚 References
Exploring Technologies. (2022, March 3). Wavelet Transform Analysis of Images using Python [Video]. YouTube. https://www.youtube.com/watch?v=JdVq8Tn1ds0
