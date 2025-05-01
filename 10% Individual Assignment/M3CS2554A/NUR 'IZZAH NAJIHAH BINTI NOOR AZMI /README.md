## 2503-ITT440
## 10% Individual Assignment
#### NAME: NUR 'IZZAH NAJIHAH BINTI NOOR AZMI  
#### MATRIC NUMBER: 2023298506
#### CLASS: M3CS2554A
---
## Image Processing using ImageAI 
---
## 1️⃣ FRAMEWORK
### TensorFlow & Keras (Used with ImageAI)
![image](https://github.com/user-attachments/assets/9359ab7f-c9f8-4093-8d60-58a8057983b1)

#### What is TensorFlow & Keras?
ImageAI is not a standalone framework. It works on top of **TensorFlow** and **Keras**, which are powerful deep learning frameworks. TensorFlow is an open-source platform developed by Google for machine learning, while Keras is a high-level neural networks API written in Python that runs on top of TensorFlow. These frameworks provide the foundation for the deep learning models that ImageAI uses. Together, TensorFlow and Keras enable ImageAI to leverage pre-trained deep learning models without requiring manual setup of neural networks.

---
---
## 2️⃣ LIBRARY
### ImageAI
![image](https://github.com/user-attachments/assets/6a7f2531-5914-4740-bb90-bd626c19b5c6)

## What is ImageAI?
ImageAI is a Python library that empowers developers to easily integrate state-of-the-art deep learning models for object detection, image classification, and even video analysis into their applications. The library abstracts the complexity of deep learning model deployment and provides a simple and intuitive API for working with pre-trained models like YOLOv3, RetinaNet, and others. ImageAI is suitable for various applications in fields such as security, autonomous vehicles, and healthcare.  

---
## Features and Functionality
#### • Object Detection
ImageAI allows users to detect and identify objects in images and videos using state-of-the-art-deep learning models such as RetinaNet, YOLOv3, and TinyYOLO.
#### • Image Prediction
It supports image classification using pre-trained models like ResNet, DenseNet, SqueezeNet, and InceptionV3.
#### • Video Object Detection
ImageAI can process video files or real-time webcam feeds to detect and track objects.
#### • Custom Model Training
Users can train custom image classifiers using ImageAI and datasets of their own, using Transfer learning.
#### • Simplicity
ImageAI provides a very beginner-friendly and Pythonic syntax that makes it accessible even to non-experts in AI.
#### • Real-Time Processing
It enables real-time object detection and alert systems when integrated with cameras.

---
## Uses of ImageAI
#### • Security systems
Detect intruders or monitor surveillance videos.
#### • Retail analytics
Track product movement or customer behavior.
#### • Autonomous vehicles
Identify objects on the road.
#### • Robotics
Empower robots with vision capabilities.
#### • Medical imaging
Assist in analyzing X-rays or MRI scans.
#### • Wildlife monitoring
Detecting animals in forests via cameras.
#### • Construction site monitoring
Detecting whether workers are wearing helmets or not.

---
## Impact on Image Processing and AI
#### Accessibility
ImageAI lowers the entry barrier for people new to deep learning, making powerful AI tools available to a broader audience.
#### Rapid Prototyping
Developers can test ideas quickly without worrying about low-level AI model implementation.
#### Education
Widely used in academic projects and courses to teach AI and computer vision principles.

---
## Future Scope of ImageAI
With ongoing improvements in AI and deep learning, ImageAI may expand to support newer models like YOLOv8 or integrate better with real-time IoT systems. It can also be used alongside cloud services like AWS or Azure for scalable deployments.

---
## Module / Subpackage
ImageAI is structured as a Python module that contains submodules for different computer vision tasks. When you use:
```
from imageai.Detection import ObjectDetection
import os

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")  # Make sure the model file is downloaded
detector.loadModel()

input_path = "image.jpg"
output_path = "image_detected.jpg"

detections = detector.detectObjectsFromImage(input_image=input_path,
                                              output_image_path=output_path)

for detection in detections:
    print(detection["name"], ":", detection["percentage_probability"])
```
You're accessing the Detection submodule under the main imageai package. This modular structure makes it easier to work with specific functionalities such as:

##### • Detection: For object detection

##### • Classification: For image classification

##### • Prediction: For video object prediction

##### • Detection.Custom: For custom training and inference

These submodules encapsulate different AI capabilities, allowing developers to use only what they need without dealing with the entire library.

---
## Conclusion
ImageAI is a powerful and easy-to-use library that democratizes access to artificial intelligence for image and video analysis. With its integration of TensorFlow, Keras, and pre-trained models, it supports a wide range of computer vision tasks. Whether used in education, prototyping, or real-world applications, ImageAI continues to make AI more accessible and practical.

---
---
## 3️⃣ EDITOR
### Visual Studio Code
![image](https://github.com/user-attachments/assets/1ce773b2-f368-4574-bdfb-faf20a671ec1)


## What is Visual Studio Code?
**Visual Studio Code (VS Code)** is a free, open-source, and lightweight code editor developed by Microsoft. It supports multiple programming languages, including Python, and offers robust features like IntelliSense, Git integration, debugging tools, and extensions.

---
## Features and Functionality
#### • IntelliSense
VS Code offers smart code completion, parameter hints, and syntax highlighting. It supports Python syntax and libraries, which makes it perfect for Python development, including working with ImageAI.
#### • Debugging Support
VS Code comes with integrated debugging tools. Developers can easily set breakpoints, step through code, and inspect variables, making it easier to troubleshoot and refine their projects.
#### • Version Control Integration
With built-in Git support, VS Code allows you to manage your project repositories without leaving the editor. You can commit changes, create branches, and synchronize with GitHub directly within VS Code.
#### • Extensibility
VS Code is highly extensible with plugins available for various languages, tools, and frameworks. For Python projects like ImageAI, extensions such as Python and Jupyter notebooks make development even more seamless.

---
## Conclusion
Visual Studio Code, with its rich features and extensibility, stands out as one of the top choices for Python development. Whether you're building a machine learning model, such as the ones used in ImageAI, or developing a simple script, VS Code provides a solid development environment.

---
## Demonstration


---
## 📚REFERENCES
#### • ImageAI Official GitHub
OlafenwaMoses. (n.d.-b). GitHub - OlafenwaMoses/ImageAI: A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities. GitHub. Retrieved April 25, 2025, from https://github.com/OlafenwaMoses/ImageAI
#### • ImageAI Documentation
Official English Documentation for ImageAI! — ImageAI 3.0.2 documentation. (n.d.-b). Retrieved April 25, 2025, from https://imageai.readthedocs.io/en/latest/
#### • TensorFlow Introduction
Introduction to TensorFlow. (n.d.). TensorFlow. Retrieved April 26, 2025, from https://www.tensorflow.org/learn
#### • Keras Overview
Team, K. (n.d.). Keras documentation: About Keras 3. Retrieved April 26, 2025, from https://keras.io/about/
#### • VS Code Official Website
Visual Studio Code - Code editing. Redefined. (2021, November 3). Retrieved April 26, 2025, from https://code.visualstudio.com/
