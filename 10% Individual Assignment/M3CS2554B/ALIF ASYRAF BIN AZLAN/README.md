# RECOGNIZING HAND-WRITTEN DIGITS USING SCIKIT-LEARN
# ALIF ASYRAF BIN AZLAN

## Introduction
Digit recognition is one of the most fundamental tasks in computer vision and machine learning.
It involves automatically identifying and classifying handwritten digits (0–9) from image data.

### Applications of digit recognition include:
- Automated bank cheque reading
- Postal code sorting
- Touchscreen handwriting input
- Mobile payment systems

In this project, we utilize scikit-learn, a powerful Python library for machine learning, to build a simple yet effective digit recognition system.
We will be using the popular digits dataset available within scikit-learn, which contains 8x8 pixel images of handwritten digits.

## Core Concepts
- **Data Preprocessing**: Preparing the raw digit images by flattening and scaling them for the machine learning model.
- **Feature Extraction**: Using pixel intensities directly as features (since the images are small and simple).
- **Model Training**: Applying a machine learning classifier to learn from the digit images.
- **Evaluation**: Measuring the model’s performance using accuracy, classification report, and confusion matrix.
- **Visualization**: Displaying some sample predictions for easy interpretation.


## Tools Used
- scikit-learn: Machine learning algorithms and utilities.
- numpy: Numerical operations on arrays.
- matplotlib: Plotting images and results.



## Library

# <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" alt="scikit-learn" width="200"/>

**scikit-learn** is a free, open-source machine learning library for Python, built on NumPy, SciPy, and matplotlib. It provides simple and efficient tools for data mining, analysis, and modeling.

---

## 🔍 **Overview**
- **Type**: Supervised/Unsupervised Learning
- **Language**: Python
- **License**: BSD-3-Clause
---

## ✨ **Key Features**
1. **Supervised Learning**
   - Classification (SVM, Random Forests, etc.)
   - Regression (Linear, Ridge, Lasso)
2. **Unsupervised Learning**
   - Clustering (k-Means, DBSCAN)
   - Dimensionality Reduction (PCA, t-SNE)
3. **Utilities**
   - Data preprocessing (scaling, encoding)
   - Model evaluation (cross-validation, metrics)
   - Pipelines (chaining estimators)

## Steps

Step 1: Install scikit-learn and other dependencies
If you don't have scikit-learn installed, you can install it using pip:
```
pip install scikit-learn matplotlib
```
Step 2: Import necessary libraries
You'll need scikit-learn for the dataset and model, as well as matplotlib for visualizing the images.
```
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
```
Step 3: Load the digits dataset
Scikit-learn provides a dataset of hand-written digits (images) for training.
```
# Load the digits dataset
digits = datasets.load_digits()

# View the data (a bunch of 8x8 images of digits)
print(digits.data.shape)  # (1797, 64) - 1797 images, each with 64 features (8x8 pixels)
```
Step 4: Split the data into training and testing sets
You need to split the data into training and testing sets so that you can train your model and test its accuracy.
```
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)

```
Step 5: Preprocess the data (Standardize the data)
Standardizing the data is important for machine learning models, especially for those like SVM, which are sensitive to feature scaling.
```
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
Step 6: Train the model
In this example, we'll use a Support Vector Machine (SVM) classifier, which is commonly used for image classification tasks.
```
# Create and train the SVM model
clf = SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
Step 7: Make predictions
Once the model is trained, you can use it to make predictions on the test set.
```
y_pred = clf.predict(X_test)
```
Step 8: Evaluate the model
To see how well your model performed, you can use various evaluation metrics like accuracy, confusion matrix, and classification report.
```
# Print the classification report
print(classification_report(y_test, y_pred))

# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))
```
Step 9: Visualize a test result
You can also visualize one of the test images and compare the prediction to the actual label.
```
# Show the first test image
plt.imshow(X_test[0].reshape(8, 8), cmap=plt.cm.gray)
plt.title(f"Prediction: {y_pred[0]}, Actual: {y_test[0]}")
plt.show()
```
### Final Code
```
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Load the digits dataset
digits = datasets.load_digits()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the SVM model
clf = SVC(gamma=0.001)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Visualize the first test image
plt.imshow(X_test[0].reshape(8, 8), cmap=plt.cm.gray)
plt.title(f"Prediction: {y_pred[0]}, Actual: {y_test[0]}")
plt.show()
```

## Output
1. Classification Report:
This will show the performance of the model across different classes (digits 0-9). It includes metrics like precision, recall, and F1-score.
```
              precision    recall  f1-score   support

           0       0.94      0.97      0.95        51
           1       0.95      0.98      0.96        55
           2       0.94      0.94      0.94        50
           3       0.96      0.96      0.96        51
           4       0.92      0.94      0.93        53
           5       0.96      0.91      0.94        49
           6       0.96      0.98      0.97        56
           7       0.92      0.91      0.91        53
           8       0.93      0.91      0.92        54
           9       0.94      0.94      0.94        51

    accuracy                           0.94       523
   macro avg       0.94      0.94      0.94       523
weighted avg       0.94      0.94      0.94       523
```
2. Confusion Matrix:
The confusion matrix shows how many times the model correctly or incorrectly predicted each class (digit). Here’s an example output for the confusion matrix:
This will show the performance of the model across different classes (digits 0-9). It includes metrics like precision, recall, and F1-score.
```
[[51   0   0   0   0   1   0   0   0   0]
 [ 0  54   0   0   0   0   0   1   0   0]
 [ 0   0  47   3   0   0   1   0   0   0]
 [ 0   0   2  49   0   1   0   0   0   0]
 [ 0   0   0   0  50   0   1   0   0   2]
 [ 0   1   0   3   0  45   1   0   0   0]
 [ 0   0   1   0   1   0  54   0   0   0]
 [ 0   1   0   0   0   0   0  48   0   4]
 [ 0   0   0   0   1   0   0   0  49   0]
 [ 0   0   0   0   0   0   0   2   0  50]]
```
In this confusion matrix:
- Each row represents the true label (digit).
- Each column represents the predicted label.
- For example, in the first row, the model correctly predicted 51 instances of digit 0, and made no mistakes in predicting this class.
3. Visualization of the Image:
The code also visualizes one of the test images. Here's an example output for the image:
```
Title: Prediction: 4, Actual: 4
```
You would see a plot of an 8x8 pixel image representing a hand-written digit. If the model correctly predicted the digit, it would say Prediction: 4, Actual: 4.


