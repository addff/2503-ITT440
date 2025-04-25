# 2503-ITT440
## NAME: AINA ASYURA BT RAHIDIAN (2023414614)
## TITLE: CVG & Image Processing with Python
### OBJECTIVE
- To write article about CVG & Image Processing using Python tools or library
- To demonstrate coding used related to the article

### Image Processing
Image processing involves the manipulation and enhancement of digital images through computer algorithms. It is primarily used to extract valuable information, enhance image quality, and prepare images for further applications. This technology plays a vital role across various industries. For example, in security systems, where it is used for facial recognition. Its wide range of applications underscores the importance of image processing as a key tool in both today’s world and in the future.

### FRAMEWORK

#### Albumenatations
<img src="https://github.com/user-attachments/assets/c7f06c36-18cc-49d0-9eeb-4d1caf6e2010" width="300" />



##### What is Albumenatations ?
Albumentations is a fast and flexible Python library used for image augmentation. It's specifically designed to perform various image transformation operations, making it a popular choice for data preprocessing in machine learning and computer vision projects. Albumentations provides a wide range of augmentations, from basic transformations like rotation and flipping to more advanced ones like elastic deformations and random brightness adjustments.

### Core Features of Albumenatations
 1) Gaussian blur
 2) Median blur
 3) Image sharpening
 4) Edge detection (via emulation, since direct Sobel is not available)
 5) Brightness and contrast contro

##### Albumenatations Advantages :
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

### Basic Image Processing Functions
 1) A.GaussianBlur(blur_limit=(3, 3), p=1.0) – Smooths the image.
 2) A.MedianBlur(blur_limit=3, p=1.0) – Reduces noise.
 3) A.Sharpen(p=1.0) – Enhances edges and detail.
 4) A.RandomBrightnessContrast(p=1.0) – Adjusts brightness and contrast.
 5) A.Equalize(p=1.0) – Improves overall image histogram distribution.

   
###### Exact code used:
```py
import cv2
import albumentations as A
from albumentations.pytorch import ToTensorV2
import matplotlib.pyplot as plt

# Load the image using OpenCV
image = cv2.imread("example.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the Albumentations transformation pipeline
transform = A.Compose([
    A.Resize(256, 256),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=15, p=0.3),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
])

# Apply the transformation
augmented = transform(image=image)
augmented_image = augmented['image']

# Convert tensor to numpy format for visualization
augmented_image_np = augmented_image.permute(1, 2, 0).numpy()

# Display the augmented image
plt.imshow(augmented_image_np)
plt.title("Augmented Image")
plt.axis('off')
plt.show()
```
