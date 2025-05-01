## 2503 - ITT440
## NAME : NUR FARAH FAIZZAH BINTI RAHMAT
## STUDENT ID : 2023213584 
## TITTLE : CVG & IMAGE PROCESSING USING PYTHON
### OBJECTIVES : 
* To acquire proficiency in utilizing Python libraries, particularly imagehash, for the analysis and processing of digital images
* To implement hashing techniques for the purpose of evaluating visual similarities and differences between digital image
* To develop the ability to intepret and analyze image hash outputs to assess the degree of similarity between images
### IMAGE PROCESSING 
Image processing refers to the techniques of converting an image into its digital representation and applying various operations to extract meaningful information from it. Typically, an image processing system interprets images as two-dimensional signals and utilizes predefined signal processing methods to analyze and manipulate the image data
### IMAGEHASH
<img src="logo.png" alt="logo" width="250">

Image hashing is the computational process of applying an algorithm to genarate unique hash value that represents the content of an image. Identical copies of the image produce the same hash value, thereby enabling consistent identification. Consequently, image hashing is often referred to as a "digital fingerprint" due to its ability to uniquely characterized visual data.
### TYPE OF IMAGE HASHING ALGORITHMS
* Average Hash (aHash)
  Reduces an image to grayscale and computers a binary hash based on whether each pixel's intensity is above or below the mean
* Perceptual Hash (pHash)
  Uses the Discrete Cosine Transform (DCT) to analyze the image in the frequency domain, focusing on low-frequency components to capture overall structure.
* Difference Hash (dHash)
  Calculates the gradient of pixel insities by comparing adjacent pixels horizontally or vertically.
* Wavelet Hash (wHash)
  Applies a wavelet transform to extract low-frequency coefficients that represent perceptual features.
### ADVANTAGES OF USING IMAGEHASH
* The imagehash library enables rapid and computationally efficient image comparison by transforming images into compact hash representations, thus eliminating the need for exhaustive pixel-level analysis.
* Image hashing techniques employed within imagehash exhibit resilience to subtle changes such as resizing, cropping, compression or minor color adjustments, thereby ensuring reliable similarity detection under various image transfromations.
* By generating consistent hash values for identical or nearly images, imagehash simplifies the process of identifying duplicate or near-duplicate content across extensive image datasets.
* The library provides an accessible and user-friendly interface, facilitating the integration of image hashing functionalities into Python-based applications with minimal complexity.
* Imagehash supports a range of hashing algorithms including Average Hash (wHash) by providing adaptability to diverse application requirements.
* Owing to its lightweight nature, imagehash is well-suited for deployment in both small-scale and large-scale environments without significant computational burdens.
* Designed to operate alongside widely adopted libraries such as Pillow (PIL), imagehash benefits from broad compatibiity, enhancing its applicability whithin comprehensive computer vision and image processing workflows.
### A PRACTICAL EXAMPLE FOR IMAGE COMPARISON
#### Original Image
<img src="image3.jpg" alt="image3" width="250">

#### Resized Image
<img src="image3_resized.jpg" alt="image3_resized" width="250">

```python
from PIL import Image
import imagehash

# Load the image
image = Image.open("myimage.jpg")
pixels = image.load()  # Get access to the pixel data

# Resize the image to 300x300 pixels
resized_image = image.resize((300, 300))
resized_image.save("myimage_resized.jpg")

# Calculate hash after resizing
resized_hash = imagehash.average_hash(resized_image)
print("Resized Image Hash:", resized_hash)
```
#### Gray Image
<img src="image3_gray.jpg" alt="image3_gray" width="250">

```python
from PIL import Image
import imagehash

# Load the image
image = Image.open("myimage.jpg")
pixels = image.load()  # Get access to the pixel data

# Convert the image to grayscale
gray_image = image.convert("L")
gray_image.save("myimage_gray.jpg")

# Calculate hash after grayscale conversion
gray_hash = imagehash.average_hash(gray_image)
print("Grayscale Image Hash:", gray_hash)
```
#### Rotated Image
<img src="myimage_rotated.jpg" alt="myimage_rotated" width="250">

```python
from PIL import Image
import imagehash

# Load the image
image = Image.open("myimage.jpg")
pixels = image.load()  # Get access to the pixel data

# Rotate the image by 90 degrees
rotated_image = image.rotate(90)  # Rotate 90 degrees clockwise
rotated_image.save("myimage_rotated.jpg")

# Calculate hash after rotation
rotated_hash = imagehash.average_hash(rotated_image)
print("Rotated Image Hash:", rotated_hash)
```

#### Vertical Image
<img src="myimage_flipped_vertically.jpg" alt="myimage_flipped_vertically" width="250">

```python
from PIL import Image
import imagehash

# Load the image
image = Image.open("myimage.jpg")
pixels = image.load()  # Get access to the pixel data

# Flip the image vertically (top to bottom)
flipped_image_v = image.transpose(Image.FLIP_TOP_BOTTOM)
flipped_image_v.save("myimage_flipped_vertically.jpg")

# Calculate hash after vertical flip
flipped_hash_v = imagehash.average_hash(flipped_image_v)
print("Flipped Vertically Hash:", flipped_hash_v)
```

#### Horizontal Image
<img src="myimage_flipped_horizontally.jpg" alt="myimage_flipped_horizontally" width="250">

```python
from PIL import Image
import imagehash

# Load the image
image = Image.open("myimage.jpg")
pixels = image.load()  # Get access to the pixel data

# Flip the image horizontally (left to right)
flipped_image_h = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image_h.save("myimage_flipped_horizontally.jpg")

# Calculate hash after horizontal flip
flipped_hash_h = imagehash.average_hash(flipped_image_h)
print("Flipped Horizontally Hash:", flipped_hash_h)
```

#### Color Modified Image
<img src="myimage_color_modified.jpg" alt="myimage_color_modified" width="250">

```python
from PIL import Image
import imagehash

# Load the image
image = Image.open("myimage.jpg")
pixels = image.load()  # Access pixel data

# Get image size
width, height = image.size

# Modify colors (increase red, decrease green)
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        
        # Increase red by 50 and decrease green by 50
        new_r = min(r + 50, 255)  # Ensure values stay within 0-255
        new_g = max(g - 50, 0)    # Ensure values stay within 0-255
        new_b = b  # Keep blue unchanged
        
        # Apply the new pixel value
        pixels[i, j] = (new_r, new_g, new_b)

# Save the modified image
image.save("myimage_color_modified.jpg")

# Generate hash of the modified image
modified_hash = imagehash.average_hash(image)
print("Hash of modified image:", modified_hash)
```

#### COMPARING ORIGINAL AND CHANGED IMAGES USING IMAGE HASHING 
Code Example for Comparison : 
```python
from PIL import Image
import imagehash

# Load the original image
original_image = Image.open("myimage.jpg")

# Load the changed image (after applying some modifications)
changed_image = Image.open("myimage_color_modified.jpg")

# Generate the hash for both images using the average hash method
original_hash = imagehash.average_hash(original_image)
changed_hash = imagehash.average_hash(changed_image)

# Compare the hashes (calculate the Hamming distance)
hamming_distance = original_hash - changed_hash

# Display the Hamming distance
print(f"Hamming distance between the images: {hamming_distance}")

# If the Hamming distance is 0, the images are identical
if hamming_distance == 0:
    print("The images are identical.")
else:
    print("The images are different.")
```
Image hashing is a method that generates a compact digital signature based on an image’s visual content. Perceptual hashing, such as that provided by the imagehash library, allows for the comparison of images by detecting visual similarities rather than exact binary matches. When an image is modified through color adjustments, rotation or filtering, the resulting hash usually changes.

By comparing the hashes of the original and altered images, one can measure their similarity using techniques like Hamming distance. A smaller distance indicates higher similarity. This approach is widely used in areas such as digital forensics, duplicate detection and content verification due to its efficiency and sensitivity to changes.




