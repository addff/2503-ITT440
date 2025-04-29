# NAME: MUHAMAD IZZAT SYAZWAN BIN MOHD SUFIAN
## MATRIC NUMBER: 2023436266

---

# Image Processing Using Keras: A Beginner’s Guide

Image processing has become an essential tool in modern-day machine learning applications. From facial recognition to medical imaging, the need to analyze and understand images has never been greater. Fortunately, with libraries like **Keras**, working with image data has become simple and efficient.

In this article, we’ll explore how to perform image processing tasks using **Keras**, covering everything from loading and visualizing images to building a simple convolutional neural network (CNN) for image classification.

---

## Why Keras?

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow. It’s user-friendly, modular, and easy to extend, making it ideal for beginners and experienced developers alike.

---

## Getting Started

### 🔧 Prerequisites

To follow along, you’ll need to install the following:

```bash
pip install tensorflow matplotlib
```

---

## 1. Loading and Preprocessing Images

Keras provides utility functions to load and preprocess images easily.

```python
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt

# Load image
image = load_img('cat.jpg', target_size=(150, 150))
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Convert to array
image_array = img_to_array(image)
image_array = image_array / 255.0  # Normalize pixel values
```

---

## 2. Image Augmentation

Image augmentation helps improve model generalization by generating variations of the training data.

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Visualizing Augmented Images
image_array = image_array.reshape((1,) + image_array.shape)
i = 0
for batch in datagen.flow(image_array, batch_size=1):
    plt.imshow(batch[0])
    plt.axis("off")
    i += 1
    if i > 4:
        break
plt.show()
```

---

## 3. Building a Simple CNN Model

Let’s now build a simple convolutional neural network to classify images.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  # For binary classification
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

---

## 4. Training the Model with Images

Use `ImageDataGenerator` to load images directly from a folder structure.

```python
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary'
)

model.fit(train_generator, steps_per_epoch=100, epochs=10)
```

---

## 5. Making Predictions

```python
import numpy as np

test_image = load_img('test/cat_or_dog.jpg', target_size=(150, 150))
test_array = img_to_array(test_image) / 255.0
test_array = np.expand_dims(test_array, axis=0)

prediction = model.predict(test_array)
print("Predicted class:", "Dog" if prediction[0][0] > 0.5 else "Cat")
```

---

## Conclusion

Keras makes image processing and deep learning approachable, even for beginners. With just a few lines of code, you can build powerful image recognition models using CNNs, perform data augmentation, and make real-time predictions.

This is just the beginning—Keras supports more complex architectures, transfer learning, and integration with powerful tools like TensorFlow and OpenCV.

---


