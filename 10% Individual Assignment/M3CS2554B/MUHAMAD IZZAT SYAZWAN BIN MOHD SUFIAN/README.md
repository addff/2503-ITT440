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

## 📌 Loading and Preprocessing Images

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

Great! Let’s now explore **`pad_sequences`**, **`skipgrams`**, and how they are used in text preprocessing for deep learning using **Keras**.

These are especially useful in **Natural Language Processing (NLP)** tasks like sentiment analysis, language modeling, and word embedding training.

---

# 🧠 Preprocessing with `pad_sequences` and `skipgrams` in Keras

---

##  1. `pad_sequences`

`pad_sequences` is used to make all input sequences the **same length**, which is necessary for batching inputs into neural networks.

### ✅ Why use it?
Neural networks require input tensors to have the same shape. If your input sentences (tokenized as lists of integers) are of different lengths, you must **pad** them.

### ✅ Example:

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    [1, 5, 7],
    [2, 3],
    [9, 8, 6, 4]
]

# Pad all sequences to same length
padded = pad_sequences(sentences, padding='post')  # or 'pre'
print(padded)
```

🔹 Output:
```
[[1 5 7 0]
 [2 3 0 0]
 [9 8 6 4]]
```

### Options:
- `maxlen=5`: Force max length
- `padding='pre'` or `'post'`: Where to add zeros
- `truncating='pre'` or `'post'`: Cut from the beginning or end

---

## 📌 2. `skipgrams`

`skipgrams` generates training samples for **word embeddings** like Word2Vec. It forms **(target, context)** pairs from a sentence, useful for context-based learning.

### ✅ Why use it?
It helps you build word embeddings by predicting surrounding words of a target word in a sentence.

### ✅ Example:

```python
from tensorflow.keras.preprocessing.sequence import skipgrams
import numpy as np

# A tokenized sentence
sentence = [2, 3, 4, 5, 6]
vocab_size = 10

pairs, labels = skipgrams(sentence, vocabulary_size=vocab_size, window_size=2)

for i in range(5):
    print(f"Target: {pairs[i][0]}, Context: {pairs[i][1]}, Label: {labels[i]}")
```

### 🔹 Output (example):
```
Target: 3, Context: 2, Label: 1
Target: 5, Context: 6, Label: 1
Target: 4, Context: 7, Label: 0   # Negative sample
...
```

- `Label = 1` means real pair (word + nearby context)
- `Label = 0` means negative pair (random word)

### Options:
- `window_size`: Context range
- `negative_samples`: Proportion of random (non-related) pairs

---

---

## Conclusion

Keras makes image processing and deep learning approachable, even for beginners. With just a few lines of code, you can build powerful image recognition models using CNNs, perform data augmentation, and make real-time predictions.

This is just the beginning—Keras supports more complex architectures, transfer learning, and integration with powerful tools like TensorFlow and OpenCV.

---


