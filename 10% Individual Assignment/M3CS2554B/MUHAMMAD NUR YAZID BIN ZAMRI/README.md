# MUHAMMAD NUR YAZID BIN ZAMRI
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


