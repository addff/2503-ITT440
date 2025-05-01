Name : MUHAMMAD IMAN AFIQ BIN ROZIHAN

Student ID : 2023436724

Group : CDCS2554B

# Image Processing using Mahotas




🧪 What is Mahotas?



Mahotas is a high-performance Python library specifically designed for scientific image processing and analysis, especially in domains like biology, microscopy, and pattern recognition.

It’s best for processing grayscale images, analyzing textures, and applying morphological operations efficiently.

🛠️ Built With:
Python + NumPy: Easy to use with Python's scientific stack.

C++ Backend: Fast processing, ideal for large datasets or real-time applications.









### ⚙️ Key Features of Mahotas

1. Speed:

Written in C++, with Python bindings — making it much faster than pure Python libraries.

2. Numpy Integration:

Works seamlessly with NumPy arrays, so it fits well in the scientific Python ecosystem.

3.0 Rich Functionality:

Morphological operations: dilation, erosion, opening, closing, etc.

Filtering: Gaussian filtering, Sobel edges, thresholding.

Connected components and labeling.

Feature extraction: Haralick textures, Zernike moments, SURF (Speeded-Up Robust Features).

4.0 No GUI dependencies:

Unlike OpenCV, Mahotas doesn’t include I/O or GUI functions. It focuses purely on image processing.











🧰 Core Capabilities of Mahotas
Here’s what Mahotas can do:

🧹 1. Filtering & Smoothing

```
mahotas.gaussian_filter()   #Blurs images using a Gaussian kernel.
mahotas.median_filter()     #Reduces salt-and-pepper noise.
```


 
🌗 2. Thresholding

```
mahotas.thresholding.otsu()  #Automatically selects a threshold.
mahotas.thresholding.rc()    #Ridler-Calvard method for iterative thresholding
```




🔳 3. Morphological Operations
Used for shape and structure analysis:

```
mahotas.dilate() and erode()  #Grow or shrink shapes.
mahotas.open() and close()    #Remove noise or small holes.
```





🧬 4. Segmentation


```
mahotas.label()      #Label connected components (e.g., counting cells).
mahotas.cwatershed() #Watershed algorithm for separating touching objects.
mahotas.distance()   #Computes distance from the nearest zero pixel (useful for segmentation).
```





🔍 5. Feature Extraction
Mahotas can extract descriptive features from images:

```
mahotas.features.haralick()   #Texture analysis (used in cancer detection, cell classification).
mahotas.features.zernike_moments()  #Shape descriptors.
mahotas.features.lbp()   #Local Binary Patterns for texture classification.
```








🧪 6. Other Tools

```
mahotas.imresize()   #Resize images.
mahotas.colors.rgb2gray()  #Convert to grayscale.
mahotas.stretch()     #Contrast stretching (normalization).
```









### 🔧 Step-by-Step: Image Processing Using Mahotas




###  ✅ 1. Install Mahotas

```
pip install mahotas

```



###  🖼️ 2. Load an Image

Mahotas can load images directly, or you can use Pillow or OpenCV to handle various formats:

```
import mahotas
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load an image and convert to grayscale (if not already)
img = Image.open('your_image.jpg').convert('L')
image = np.array(img)

plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.show()
```



###  🧹 3. Preprocessing (Smoothing / Denoising)

```
smoothed = mahotas.gaussian_filter(image, sigma=2)

plt.imshow(smoothed, cmap='gray')
plt.title('Smoothed Image')
plt.axis('off')
plt.show()
```



###  🌗 4. Thresholding (Otsu Method)

```
T = mahotas.thresholding.otsu(smoothed)
binary = smoothed > T

plt.imshow(binary, cmap='gray')
plt.title("Binary Image (Otsu's Threshold)")
plt.axis('off')
plt.show()
```



###   🧱 5. Labeling Connected Components (Cells, Objects)

```
labeled, num_objects = mahotas.label(binary)

print(f"Number of objects detected: {num_objects}")
plt.imshow(labeled, cmap='nipy_spectral')
plt.title('Labeled Image')
plt.axis('off')
plt.show()
```




###  📏 6. Extract Features (Area, Perimeter, Eccentricity)

```
from mahotas import labeled

areas = labeled.area(labeled)
perimeters = labeled.perimeter(labeled)
eccentricities = labeled.eccentricity(labeled)

# Display results for first 5 objects
for i in range(1, min(6, len(areas))):
    print(f"Object {i} - Area: {areas[i]}, Perimeter: {perimeters[i]:.2f}, Eccentricity: {eccentricities[i]:.2f}")
```



###  🧼 7. Filter Small Objects (e.g., Noise)

```
min_area = 100
filtered = np.zeros_like(labeled)

for i in range(1, labeled.max()+1):
    if areas[i] > min_area:
        filtered[labeled == i] = i

plt.imshow(filtered, cmap='nipy_spectral')
plt.title('Filtered by Area')
plt.axis('off')
plt.show()
```




###   📄 Mahotas Image Processing Full Code

```
import mahotas
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# --- STEP 1: Load and Convert Image ---
img = Image.open('your_image.jpg').convert('L')  # Convert to grayscale
image = np.array(img)

# --- STEP 2: Preprocess Image (Gaussian Smoothing) ---
smoothed = mahotas.gaussian_filter(image, sigma=2)

# --- STEP 3: Thresholding (Otsu) ---
T = mahotas.thresholding.otsu(smoothed)
binary = smoothed > T

# --- STEP 4: Label Connected Components ---
labeled, num_objects = mahotas.label(binary)
print(f"Detected {num_objects} objects")

# --- STEP 5: Extract Features ---
from mahotas import labeled as mlabel

areas = mlabel.area(labeled)
perimeters = mlabel.perimeter(labeled)
eccentricities = mlabel.eccentricity(labeled)

# --- STEP 6: Filter Small Objects (Optional) ---
min_area = 100
filtered = np.zeros_like(labeled)

for i in range(1, labeled.max() + 1):
    if areas[i] > min_area:
        filtered[labeled == i] = i

# --- STEP 7: Display Results ---
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(image, cmap='gray')
axs[0].set_title("Original")
axs[0].axis('off')

axs[1].imshow(binary, cmap='gray')
axs[1].set_title("Binary (Otsu)")
axs[1].axis('off')

axs[2].imshow(filtered, cmap='nipy_spectral')
axs[2].set_title(f"Filtered & Labeled ({np.max(filtered)} objects)")
axs[2].axis('off')

plt.tight_layout()
plt.show()

# --- STEP 8: Print Feature Summary ---
print("\nFeature Summary (First 5 objects):")
for i in range(1, min(6, len(areas))):
    if areas[i] > min_area:
        print(f"Object {i} | Area: {areas[i]} | Perimeter: {perimeters[i]:.2f} | Eccentricity: {eccentricities[i]:.2f}")
```



###  🧾 Output:

Visual display of:

- Original image

- Binary thresholded image

- Labeled/filtered objects

Console printout of:

- Object count

- Shape features (area, perimeter, eccentricity)


                      
