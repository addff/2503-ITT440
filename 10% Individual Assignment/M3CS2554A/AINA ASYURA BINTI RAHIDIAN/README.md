# 2503-ITT440
## NAME: AINA ASYURA BT RAHIDIAN (2023414614)
## TITLE: CVG & Image Processing with Python
### OBJECTIVE
- To write article about CVG & Image Processing using Python tools or library
- To demonstrate coding used related to the article

### Editor: Notepad ++
Notepad++ is a widely-used, free source code and text editor for Windows, developed by Don Ho and licensed under the GNU General Public License. It is known for its intuitive interface and broad support for various programming languages and file formats.
###### Significance Of Notepad++ :
- Free and Open Source: Notepad++ is available at no cost, and its open-source nature means the source code is accessible to the public, allowing users to inspect, modify, and contribute to its development.
- Lightweight: Notepad++ is a lightweight application that doesn’t use much system resource, enabling it to run smoothly even on older or lower-performance computers.
- Community and Support: Notepad++ benefits from a large, active community, providing users with access to tutorials, plugins, and help from fellow users to extend its capabilities.

### FRAMEWORK

#### Albumenatations

##### What is Albumenatations ?
Albumentations is a fast and flexible Python library used for image augmentation. It's specifically designed to perform various image transformation operations, making it a popular choice for data preprocessing in machine learning and computer vision projects. Albumentations provides a wide range of augmentations, from basic transformations like rotation and flipping to more advanced ones like elastic deformations and random brightness adjustments.

##### Albumenatations Features :
Here are some key features and characteristics of the Albumenatations framework:

1) High Performance: Albumentations is optimized for speed and efficiency, making it suitable for large-scale image processing tasks.
2) Rich Set of Transformations: It offers a wide variety of image augmentations, including flipping, rotating, cropping, brightness/contrast adjustments, blurring, noise addition, and more.
3) Support for Advanced Augmentations: Includes complex transformations like elastic deformation, grid distortion, optical distortion, and CLAHE (Contrast Limited Adaptive Histogram Equalization).
4) Mask and Keypoint Support: Allows simultaneous augmentation of images, segmentation masks, and keypoints, which is essential for tasks like semantic segmentation and pose estimation
5) Custom Transformations: Users can define their own custom transformations for specialized use cases.
6) Reproducibility: Augmentations can be made deterministic using random seeds, ensuring consistent results when needed.
   
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
