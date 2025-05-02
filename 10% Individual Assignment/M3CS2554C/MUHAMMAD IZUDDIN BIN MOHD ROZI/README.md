# MUHAMMAD IZUDDIN BIN MOHD ROZI


# INTRODUCTION OF IMAGE PROCESSING

In the morden era, image processing take a lot of responsibility of making human task more efficient and easy. Image processing is the technique of analyzing, enhancing, and manipulating the images using algorithms, typically using for software and internet of things (IOT). In easy way too understand image processing taking an image as a input and doing something about it. For example improving its quality, detecting object, changing size or colors.

At its core, image processing is divided into two major type which is analog done on physical images using optical or electronic device and second major type if digital done on digital images using computers. In moderan system, digital image processing is far more widespread and accessible, enabling complex operation on images using programming languages and libraries. One of the key benefits of digital image processing is the ability to perform task with speed, accuracy and reproducibility. For example the vital in fields such as medical diagnostics (analyzing X-rays and MRIs), security system (facial recognition), industrial automation (quality inspection), satellite imaging (weather monitoring and land mapping) amd entertainment (filters and effects in apps and games).

As technology advances and visual data becomes increasingly central too communication and decision-making, image processing continues to evolve as a vital field in both research and industry, it acts as a foundation for more advanced topics like computer vision, machine learning, and artificial intelligence, allowing the computer to not just look up but also to understand and interpret the visual world.

# IMAGE PROCESSING TOOLS


<div align="center">
  
**<img src="https://github.com/user-attachments/assets/2e63b82f-2f1b-4c35-88b3-5562924329a7" alt="image"/>**

</div>




# What is Scikit-Image?

In simple terms, **Scikit-Image** is a Python library made specifically for image processing and is part of the SciPy ecosystem. It provides ready-to-use functionality for filtering, segmentation, feature detection, restoration, transformation, and more.

# Advantage Using Scikit-Image

- **Ease to use**: High-level functions and no need for deep computer vision knowledge.
- **Powerful tools**: Inside scikit-image, there are ready-made functions for almost all common processing needs like denoising, edge detection, segmentation, and transformations. Each tool uses algorithms that are trusted and proven in scientific communities.
- **Scientific accuracy**: It is designed for real researchers, for example in biology (cell counting), astronomy (star segmentation), and material science (analyzing textures). Functions are mathematically correct and follow peer-reviewed algorithms.

# Features that can be used in scikit-image 

I.  Filtering : blur, sharpen, edge detection
  
   - Blur :

  <div align="center">
    
  ![image](https://github.com/user-attachments/assets/ddafd572-ca52-44d9-90df-7561766af5ba)


  
</div>

  - Sharpen :

<div align="center">

  
   
![image](https://github.com/user-attachments/assets/ef485252-3e0c-46bb-ba11-810f8bf1701c)

</div>


- Edge detection :
  
<div align="center">
  
  ![image](https://github.com/user-attachments/assets/dbbca33a-c3a7-41f0-afa8-ce352a9d2a55)
  </div>

II. Segmentation : split an image into parts


III. Feature detection : corners, blobs, lines

- Corners :

<div align="center">
  
 ![image](https://github.com/user-attachments/assets/cc63c366-8bd3-4af9-9941-947457a2cc16)

  </div>

- Blobs detection :


<div align="center">
  
![image](https://github.com/user-attachments/assets/2c25aa1a-65f2-49eb-a840-3290315ab761)

  </div>


IV. Image transformation : rotate, resize, warp

- Resize :

<div align="center">
  
![image](https://github.com/user-attachments/assets/d474ffb5-6359-4c67-92f1-5b4cb46e0541)


  </div>


V. Morphological operation : erosion, diltation

- Erosion :

 <div align="center"> 
   
  ![image](https://github.com/user-attachments/assets/7c764b8a-49f7-4c8d-bd21-ca5f3c3f9771)
</div>


- Diltation :

<div align="center">
  
![image](https://github.com/user-attachments/assets/1a322f25-e74c-498f-95c3-3a5be16bf3bd)
</div>


VI. Color manipulations : convert RGB to grayscale to binary

- RGB to grayscale : 

<div align="center">

![image](https://github.com/user-attachments/assets/bfb1e781-a6b8-4f71-aca3-d34288771ed0)

</div>

VII. Restoration : remove noise, deblur image


# Real worlds Example using scikit-image 
- Biology :- Count number of bacteria in microscope image
- Medical imaging :- Segment tumors in MRI or CT scans
- Astronomy :- Detect start and galaxies form telescope images
- Remote sensing :- analyze land cover types form satellite images
- Industrial inspection :- find cracks of defects in products surfaces
- Document processing :- clean and extract text from old scanned books
- Machince learning :- preprocess images to train AI models



# Scikit-image installation


- Step 1 : Install Python In the Computer/laptop
  - link : https://www.python.org/
    
    <div align="center">
      
    ![image](https://github.com/user-attachments/assets/f6bc7406-d31f-48c8-9c65-368b7e2d2480)

    </div>

- Step 2 : Install scikit-image using commmad Prompt 
  - Enter command :
    
   ```python
    pip install scikit-image
    
  ```
  
  <br>

  <div align="center">
    
  ![image](https://github.com/user-attachments/assets/342676a5-5705-49d7-b9a5-b880304dbebf)

  </div>


- Step 3 : Run scikit-image and try fetures Image Color filtering using Python in Commad Promt
  
  - Enter commmad :
 
```python
    >>> from skimage import data,io
    >>> original = data.hubble_deep_field()
    >>> io.imshow(original)
    >>> io.show()

```
<div align="center">
  
  ![image](https://github.com/user-attachments/assets/3c9ff0f1-8a6f-458d-bb23-eeef036e47ae)

   </div>

   <br>
   
  ```python 
>>> i = data.hubble_deep_field()
>>> i[:, :, 0]=0
>>> io.imshow(i)
>>> io.show()
  ```
<div align="center">

   ![image](https://github.com/user-attachments/assets/5bbb2bd4-fbb4-4bf3-80eb-e8b8c987376b)

  </div>




# EXAMPLE CODE FOR IMAGE PROCESSING USING SCIKIT-IMAGE IN PHYTON 


```python

from skimage import io, color, filters
import matplotlib.pyplot as plt

# Step 1: Load image
image = io.imread(r'C:\Users\MUHAMMAD IZUDDIN\Downloads\GitHub.jpg') 

# Step 2: Convert to grayscale
gray_image = color.rgb2gray(image)

# Step 3: Apply threshold to segment
threshold = filters.threshold_otsu(gray_image)
segmented = gray_image > threshold

# Step 4: Display results
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(gray_image, cmap='gray')
ax[0].set_title('Grayscale Image')
ax[0].axis('off')

ax[1].imshow(segmented, cmap='gray')
ax[1].set_title('Segmented Image')
ax[1].axis('off')

plt.show()

```
<div align="center">
  
![image](https://github.com/user-attachments/assets/bb544e28-c966-4de1-972f-b226f6bead90)


 </div>

<br>
<br>

```python


from skimage import io, color, filters
import matplotlib.pyplot as plt

# Load the image
image_path = r'C:\Users\MUHAMMAD IZUDDIN\Downloads\izuddin.jpg'
image = io.imread(image_path)

# Convert to grayscale
gray_image = color.rgb2gray(image)

# Apply Gaussian Blur
blurred_image = filters.gaussian(gray_image, sigma=1)

# Apply Sobel edge detection
sobel_edges = filters.sobel(blurred_image)

# Display original, blurred, and edge-detected images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
ax = axes.ravel()

ax[0].imshow(gray_image, cmap='gray')
ax[0].set_title("Grayscale Image")
ax[0].axis('off')

ax[1].imshow(blurred_image, cmap='gray')
ax[1].set_title("Gaussian Blurred")
ax[1].axis('off')

ax[2].imshow(sobel_edges, cmap='gray')
ax[2].set_title("Sobel Edges")
ax[2].axis('off')

plt.tight_layout()
plt.show()

```

<div align="center">
  
![image](https://github.com/user-attachments/assets/52bb0dd6-f414-4ba7-aede-f2cf06733eb6)



 </div>

 # CLONCLUSION

 Scikit-image is a powerful, easy-to-use Python library that provides efficient and scalable tools for a wide range of image processing tasks. Whether you're working with image filtering, feature extraction, segmentation, or transformations, scikit-image simplifies complex operations, making it accessible to both beginners and advanced users. Its integration with the scientific Python ecosystem (like NumPy and SciPy) ensures that it is suitable for a variety of applications, from scientific research to industrial projects. With its clear documentation and extensive functionality, scikit-image remains an essential tool for anyone working with digital image analysis.



