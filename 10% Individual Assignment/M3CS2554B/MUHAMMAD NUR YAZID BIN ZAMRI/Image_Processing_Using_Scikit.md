# MUHAMMAD NUR YAZID BIN ZAMRI (2023261328)
# Image Processing with Scikit-learn

## Introduction
Image processing is the science of analyzing and manipulating digital images to extract meaningful information or improve their quality. It's a foundational aspect of fields like computer vision, medical imaging, and satellite analysis. Whether it's detecting patterns in medical scans or enhancing photos for social media, image processing plays a pivotal role in bridging the gap between raw visual data and actionable insights.

---

## Core Concepts
- **Preprocessing**: Preparing raw image data by resizing, normalizing, or denoising it.
- **Feature Extraction**: Identifying unique patterns or structures within an image, such as edges, shapes, and textures.
- **Segmentation**: Dividing an image into regions or objects for further analysis.
- **Classification**: Using machine learning to categorize images based on extracted features.

---

## Tools for Image Processing

![skimage_logo](https://github.com/user-attachments/assets/ed901153-6e46-428e-bb90-8a158e62ca33) ![OIP](https://github.com/user-attachments/assets/16367e7e-91f0-4f6f-b6d8-de14bdb1c051)

- **Scikit-learn**: A versatile library for machine learning, often used for tasks like image classification, clustering, and regression.
- **Scikit-image**: A companion library to Scikit-learn, specifically designed for image processing tasks such as edge detection, segmentation, and transformations.

---

## Example: Image Classification with Scikit-learn
This example demonstrates how to combine **Scikit-learn** and **Scikit-image** to build a simple image classification pipeline.

### Step 1: Install Dependencies
Run the following command to install the required libraries:
```bash
pip install scikit-learn scikit-image matplotlib
```
### Step 2: Import Required Modules
```
import numpy as np
from skimage import io, color, feature
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
```
### Step 3: Load and Preprocess Images 
Load images and extract features for classification:
```
# Load image dataset (example: grayscale images)
image1 = color.rgb2gray(io.imread("image1.jpg"))
image2 = color.rgb2gray(io.imread("image2.jpg"))

# Extract edge features using Canny
edges1 = feature.canny(image1)
edges2 = feature.canny(image2)

# Flatten features into 1D arrays
features = [edges1.ravel(), edges2.ravel()]
labels = [0, 1]  # Example labels for classification

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
```
### Step 4: Train a Classifier
Use Scikit-learn’s machine learning model for classification:
```
# Use Random Forest for image classification
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
```
Step 5: Evaluate the Model
Test the classifier and calculate accuracy:
```
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
```
Applications
- Medical Imaging: Detecting tumors or abnormalities in scans.
- Face Recognition: Identifying individuals in photos or videos.
- Object Detection: Detecting and classifying objects in real-time.
- Self-Driving Cars: Analyzing road signs and obstacles.


Conclusion
Image processing, when combined with machine learning, opens up a world of possibilities for analyzing visual data. By leveraging libraries like Scikit-learn for machine learning and Scikit-image for feature extraction, you can build powerful systems that understand and act on images.




