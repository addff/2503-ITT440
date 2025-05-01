**Name: Nur Asha Irdina binti Md Heryzal**

**Student ID: 2024977815**

---

🔍 **Easy Object Detection with Keras: A Hands-On Student Project**

---

🎓 **Introduction**

In this project, I explored the basics of computer vision and deep learning by building a real-time object detection system. The main goal was to train a simple model using Keras to detect the position of objects, and to test how well it can perform on live images.


---

🧠 What is CVG (Computer Vision and Graphics)?

Computer Vision and Graphics (CVG) is a field in computer science focused on enabling machines to interpret and process visual information from the world, similar to human vision. It combines image processing, machine learning, and graphics to solve real-world visual problems such as object detection, recognition, tracking, and image generation.

---

🧠 What is Keras?

Keras is a high-level open-source deep learning API written in Python. It runs on top of backend engines like TensorFlow and simplifies the process of building and training neural networks. Keras is widely used for its clean and user-friendly syntax that allows rapid prototyping and experimentation.

---



🔗 Advantages of Using Keras

User-friendly: Intuitive syntax for beginners and researchers.

Modular: Allows easy combination of neural network components.

Supports multiple backends: Primarily TensorFlow but also Theano and CNTK.

Community Support: Large user base and comprehensive documentation.

Integration: Seamlessly integrates with TensorFlow tools and ecosystem.

--- 

🛠️ Tools Used
Keras: For building and training the neural network model.

NumPy: For numerical operations and handling image data.

OpenCV: Used minimally for image creation and visualization purposes.

Python: The programming language used for the entire project

---

📁 **Project Files and Explanation**

### 1. `create_model.py`

![image](https://github.com/user-attachments/assets/5a67038e-d712-4450-ba54-ca059c783453)

**Explanation:**
- We define a **Sequential model** with Flatten and Dense layers.
- The model learns to predict **four bounding box values**.
- Using `adam` as optimizer and `mean_squared_error` since this is a regression problem.

---

### 2. `generate_images.py`

![image](https://github.com/user-attachments/assets/0eb7942b-6661-4fa6-9232-ffc46bcad0ad)


---

### 3. `train_model.py`

![image](https://github.com/user-attachments/assets/d0f58b8d-366e-4a3f-83aa-2a806c022565)

**Explanation:**
- Trains the Keras model on the generated rectangle images.
- Saves the trained model to `models/object_detection_model.h5`.

---

### 4. `predict.py`
```python
import cv2
import numpy as np
from keras.models import load_model

def predict_and_display(image_path):
    model = load_model('models/object_detection_model.h5')
    img = cv2.imread(image_path)
    resized_img = cv2.resize(img, (64, 64)) / 255.0
    input_img = np.expand_dims(resized_img, axis=0)

    bbox = model.predict(input_img)[0].astype(int)
    cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
    cv2.imshow('Prediction', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/783ef5c2-0ec7-45c4-b139-c1950ac4571d)

**Explanation:**
- Loads the trained Keras model.
- Reads and resizes the input image to 64x64.
- Predicts the bounding box using the model and draws it.
- Displays the result using OpenCV.

---

### 5. `object_detection.py`
```python
from train_model import train_model
from predict import predict_and_display

# Train the model
train_model()

# Predict on test image
predict_and_display('images/test_image.jpg')
```
**Explanation:**
- This is the main script to **train and test** the model.
- First trains the model.
- Then uses it to predict on a sample image.

---

🔧 **Tools Used**

- **Keras**: Main framework to build and train the model.
- **NumPy**: For array manipulations.
- **OpenCV**: Used only to draw rectangles and display images, not for detection.
- **Thonny IDE**: My personal IDE for running Python scripts.

---

🔹 **Conclusion**

Through this project, I got hands-on experience with how **Keras models** can be used for simple object detection tasks. By removing complex datasets and using synthetic images, I could focus purely on the model’s ability to learn bounding box coordinates.

This project helped me understand the following:
- How Keras models handle regression tasks.
- How to generate and normalize custom image data.
- How training works for object localization.

Overall, this project provided a foundational understanding of object detection using Keras, emphasizing the process of building and training a model from scratch without relying on pre-trained models or extensive image enhancement techniques.​



