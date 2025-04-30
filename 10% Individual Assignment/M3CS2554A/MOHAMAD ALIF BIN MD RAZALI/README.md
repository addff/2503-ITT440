# M3CS2554A-ITT440

## NAME: MOHAMAD ALIF BIN MD RAZALI

## TITLE: CVG & Image Processing Using SimpleITK in Python

---

### 🎯 OBJECTIVE:
- To learn and utilize SimpleITK for image processing tasks using Python.
- To demonstrate basic image operations and visualization using SimpleITK.

---

### 🧠 Image Processing
Image processing involves the manipulation and enhancement of digital images through computational algorithms. It is crucial for a wide range of applications such as medical imaging, satellite imagery, document scanning, and more. SimpleITK is a simplified layer built on top of the Insight Segmentation and Registration Toolkit (ITK), designed to make image analysis easier using Python and other high-level languages.

---

### 🧰 FRAMEWORK

**SimpleITK**

![Image](https://github.com/user-attachments/assets/9d02e4fb-cff8-482c-bcf4-fe416bc8414a)


---

### 📌 What is SimpleITK?

SimpleITK is a simplified layer built on top of the Insight Segmentation and Registration Toolkit (ITK). It provides a user-friendly interface to ITK, making it easier to use for rapid prototyping, education, and research. SimpleITK supports 2D and 3D image processing and is particularly powerful for medical image analysis and registration.

---

### 🔍 Core Functions of SimpleITK

- Image reading/writing  
- Image filtering  
- Image segmentation  
- Registration (aligning images)  
- Transformations and resampling  

---

### ✅ Advantages of Using SimpleITK

- Cross-platform compatibility: Python, R, Java, and more
- Multi-dimensional image support: 2D, 3D, 4D
- Interactive exploration in Jupyter Notebooks
- Built-in visualization tools
- Specialized in medical imaging tasks (DICOM, NIfTI, etc.)

---

### 🧾 Related Libraries

SimpleITK handles:

- Image I/O (JPEG, PNG, DICOM, NIfTI)
- Image transformations (resize, rotate, shift)
- Filtering (Gaussian, Median, etc.)
- Segmentation & registration tools

---

### 💻 Integrated Development Environments (IDEs)

- Jupyter Notebook
- Visual Studio Code
- PyCharm

---

### 🧪 Basic Image Processing Functions

1. `ReadImage()` – Load the image  
2. `Show()` – Display image  
3. `GetArrayFromImage()` – Convert image to NumPy array  
4. `RescaleIntensity()` – Adjust brightness and contrast  
5. `Cast()` – Convert image pixel types  
6. `Histogram()` – Analyze intensity distribution  

---

### 🔬 Code Example (SimpleITK)

```python
import SimpleITK as sitk
import matplotlib.pyplot as plt

# Read an image
image = sitk.ReadImage("sample.jpg", sitk.sitkFloat32)

# Display image using matplotlib
array = sitk.GetArrayFromImage(image)
plt.imshow(array, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# Apply smoothing filter
smoothed = sitk.SmoothingRecursiveGaussian(image, sigma=2.0)

# Display smoothed image
smoothed_array = sitk.GetArrayFromImage(smoothed)
plt.imshow(smoothed_array, cmap='gray')
plt.title("Smoothed Image")
plt.axis('off')
plt.show()
