# 2503-ITT440
## NAME: AINA ASYURA BT RAHIDIAN (2023414614)
## TITLE: CVG & Image Processing Using Albumenatations In Python
### OBJECTIVE
- To write article about CVG & Image Processing using Python tools or library
- To demonstrate coding used related to the article

### Image Processing
Image processing involves the manipulation and enhancement of digital images through computer algorithms. It is primarily used to extract valuable information, enhance image quality, and prepare images for further applications. This technology plays a vital role across various industries. For example, in security systems, where it is used for facial recognition. Its wide range of applications underscores the importance of image processing as a key tool in both today’s world and in the future.

### FRAMEWORK

#### Albumenatations
<img src="https://github.com/user-attachments/assets/c7f06c36-18cc-49d0-9eeb-4d1caf6e2010" width="300" />



## What is Albumenatations ?
Albumentations is a fast and flexible Python library used for image augmentation. It's specifically designed to perform various image transformation operations, making it a popular choice for data preprocessing in machine learning and computer vision projects. Albumentations provides a wide range of augmentations, from basic transformations like rotation and flipping to more advanced ones like elastic deformations and random brightness adjustments.

## Core Features of Albumentations
 1) Gaussian blur
 2) Median blur
 3) Image sharpening
 4) Edge detection (via emulation, since direct Sobel is not available)
 5) Brightness and contrast contro


## Key Features of Albumentations
- Rich transformation library: Includes flip, rotate, crop, blur, noise, brightness, contrast, and more
- Composable pipelines: Combine multiple augmentations easily.
- GPU-friendly: Can work with DALI or other tools for high-speed data loading.
- Deterministic behavior: Supports reproducibility with random seeds.
- -Bounding box and mask support: Ideal for object detection and segmentation tasks.
- -Flexible format support: Works with images, masks, keypoints, bounding boxes, and more.

## Albumenatations Advantages :
Here are some advantages of the Albumenatations framework:

1) High Performance: Albumentations is optimized for speed and efficiency, making it suitable for large-scale image processing tasks.
2) Rich Set of Transformations: It offers a wide variety of image augmentations, including flipping, rotating, cropping, brightness/contrast adjustments, blurring, noise addition, and more.
3) Support for Advanced Augmentations: Includes complex transformations like elastic deformation, grid distortion, optical distortion, and CLAHE (Contrast Limited Adaptive Histogram Equalization).
4) Mask and Keypoint Support: Allows simultaneous augmentation of images, segmentation masks, and keypoints, which is essential for tasks like semantic segmentation and pose estimation
5) Custom Transformations: Users can define their own custom transformations for specialized use cases.
6) Reproducibility: Augmentations can be made deterministic using random seeds, ensuring consistent results when needed.

### Library Related to Albumentations
Albumentations is a fast and flexible image processing library designed primarily for machine learning and computer vision tasks. It supports a wide range of image augmentation techniques such as blurring, sharpening, cropping, and color adjustments. Unlike SciPy, which is more general-purpose, Albumentations is optimized for preparing image datasets, especially for training deep learning models.

### Integrated Development Environment (IDE)
Albumentations can be used in various popular IDEs such as Jupyter Notebook, VS Code, and PyCharm. These platforms allow for seamless integration with image visualization tools like Matplotlib or OpenCV, making it easy to view and test augmentations in real time.

## Basic Image Processing Functions
 1) A.GaussianBlur(blur_limit=(3, 3), p=1.0) – Smooths the image.
 2) A.MedianBlur(blur_limit=3, p=1.0) – Reduces noise.
 3) A.Sharpen(p=1.0) – Enhances edges and detail.
 4) A.RandomBrightnessContrast(p=1.0) – Adjusts brightness and contrast.
 5) A.Equalize(p=1.0) – Improves overall image histogram distribution.

## How Albumentations Works

**Step 1: Build Your AUgmentations**  
You choose what changes you want to make — like flipping, rotating, or changing brightness.

**Step 2: Combine Them into a Pipeline**  
Put those changes together using A.Compose() like a recipe that tells how and when to apply each one.

**Step 2: Apply To Your Image**  
Feed in your image, and Albumentations instantly gives you a new, changed version.
It works with images, masks, boxes, and keypoints — great for training AI models

## How to Install Albumentations (Windows)

1. **Install Albumentations via pip**
   - Pip install albumentations
2. **Install additional dependencies (Optional)**
   - Pip install opencv-python (for image operations like reading / saving images)
3. **Verify Installation**
   - python -c "import albumentations as A; print(A.__version__)"

   
###### Exact code used:
```py
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # Elak OpenMP crash

import cv2
import albumentations as A
from albumentations.pytorch import ToTensorV2
import matplotlib.pyplot as plt
import torch

image_path = r"C:\Users\Admin\Documents\project\gambar.jpg"

image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Gambar tidak dijumpai: {image_path}")
    
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

transform = A.Compose([
    A.ToGray(p=1.0),  # Tukar ke grayscale 100%
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=15, p=0.5),
    A.Resize(224, 224),
    ToTensorV2()
])

augmented = transform(image=image)
augmented_image = augmented['image']


mean = torch.tensor([0.485]).view(1, 1, 1)
std = torch.tensor([0.229]).view(1, 1, 1)
unnormalized = augmented_image * std + mean
unnormalized_np = unnormalized.permute(1, 2, 0).numpy()
unnormalized_np = (unnormalized_np * 255).astype('uint8').squeeze()


output_path = r"C:\Users\Admin\Documents\project\pic_augmented.jpg"
cv2.imwrite(output_path, unnormalized_np)

plt.imshow(unnormalized_np, cmap='gray')
plt.title("Gambar Augmented (Hitam Putih)")
plt.axis('off')
plt.show()

```
## Conclusion
Albumentations is a highly efficient and versatile Python library tailored for image preprocessing and data augmentation. Its ease of use, extensive transformation support, and compatibility with various deep learning workflows make it an essential tool for computer vision practitioners.

## References

1. Buslaev, A., Parinov, A., Khvedchenya, E., Iglovikov, V. I., & Kalinin, A. A. (2020). *Albumentations: Fast and Flexible Image Augmentations*. Information, 11(2), 125. [https://www.mdpi.com/2078-2489/11/2/125](https://www.mdpi.com/2078-2489/11/2/125)
2. Albumentations GitHub Repository. [https://github.com/albumentations-team/albumentations](https://github.com/albumentations-team/albumentations)
3. Albumentations Official Documentation. [https://albumentations.ai/docs/](https://albumentations.ai/docs/)



# Video Tutorial
Learn how to use the Albumentations with this video tutorial: 
[![Watch the video](https://img.youtube.com/vi/2YgV5oIVxuE/maxresdefault.jpg)](https://youtu.be/2YgV5oIVxuE)

### SAMPLE OUTPUT
![Image](https://github.com/user-attachments/assets/31a475b7-a85c-45b3-989d-ebd990aa61ba)
