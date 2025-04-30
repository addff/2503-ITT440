Name : MUHAMMAD IMAN AFIQ BIN ROZIHAN

Student ID : 2023436724

Group : CDCS2554B

# Image Processing using Mahatos


🧪 What is Mahotas?
Mahotas is a high-performance Python library specifically designed for scientific image processing and analysis, especially in domains like biology, microscopy, and pattern recognition.

It’s best for processing grayscale images, analyzing textures, and applying morphological operations efficiently.

🛠️ Built With:
Python + NumPy: Easy to use with Python's scientific stack.

C++ Backend: Fast processing, ideal for large datasets or real-time applications.

🧰 Core Capabilities of Mahotas
Here’s what Mahotas can do:

🧹 1. Filtering & Smoothing
mahotas.gaussian_filter() — Blurs images using a Gaussian kernel.

mahotas.median_filter() — Reduces salt-and-pepper noise.

🌗 2. Thresholding
mahotas.thresholding.otsu() — Automatically selects a threshold.

mahotas.thresholding.rc() — Ridler-Calvard method for iterative thresholding.

🔳 3. Morphological Operations
Used for shape and structure analysis:

mahotas.dilate() and erode() — Grow or shrink shapes.

mahotas.open() and close() — Remove noise or small holes.

🧬 4. Segmentation
mahotas.label() — Label connected components (e.g., counting cells).

mahotas.cwatershed() — Watershed algorithm for separating touching objects.

mahotas.distance() — Computes distance from the nearest zero pixel (useful for segmentation).

🔍 5. Feature Extraction
Mahotas can extract descriptive features from images:

mahotas.features.haralick() — Texture analysis (used in cancer detection, cell classification).

mahotas.features.zernike_moments() — Shape descriptors.

mahotas.features.lbp() — Local Binary Patterns for texture classification.

🧪 6. Other Tools
mahotas.imresize() — Resize images.

mahotas.colors.rgb2gray() — Convert to grayscale.

mahotas.stretch() — Contrast stretching (normalization).
