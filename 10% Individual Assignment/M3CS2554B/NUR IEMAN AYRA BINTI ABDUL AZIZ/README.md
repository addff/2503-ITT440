# NUR IEMAN AYRA BINTI ABDUL AZIZ
# ITT440-CDCS2554B

# Learn Image Processing with ImageAI in Python : ImageAI Analysis


![gambar imageai](https://github.com/user-attachments/assets/3e7fcb8b-444d-443c-bf19-7738b97b19cd)

     

# Introduction
For this project, I chose to use ImageAI, a powerful Python library designed to simplify the development of applications with deep learning and computer vision capabilities. ImageAI makes it easy for developers, researchers, and students to perform complex tasks such as object detection, image prediction, and custom model training with just a few lines of code. Image processing, a crucial aspect of computer vision, involves enhancing, analyzing, and transforming images to extract valuable information, and ImageAI provides an accessible way to implement these techniques efficiently.


# Concept ImageAI

1. Pre-trained Models:
ImageAI uses deep learning models like YOLOv3, ResNet, and others for tasks such as object detection and classification without needing to train from scratch.

2. Object Detection:
It can identify multiple objects in images or video streams, drawing bounding boxes and labels around detected items.

3. Image Classification:
Classifies images into categories using pre-trained models (e.g., identifying whether an image is of a cat, dog, or car).

# How is it work?

Setting Up ImageAI for Image Processing
Follow these steps :

1. Install Python
First, make sure you have Python 3.6, 3.7, 3.8, or 3.9 installed on your computer.
If you don't have Python yet, download and install it here: https://www.python.org/downloads/

2. Create a virtual Environment
```
python -m venv myenv
```

Then,activate it

Windows : 
```
myenv\Scripts\activate
```
Mac/Linux :
```
source myenv/bin/activate
```
3. Install Required Libraries
Now, install TensorFlow and ImageAI.
```
pip install tensorflow
pip install imageai 
```

4. Prepare Project Folder
```
/my-imageai-project
    /input
        (your images here)
    /output
        (processed images saved here)
    process.py (your main Python code)
    README.md
    yolo.h5 (optional, if you use object detection)
```

5. Coding
```
from imageai.Prediction import ImagePrediction
import os

# Get current folder path
execution_path = os.getcwd()

# Initialize ImagePrediction
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()

# Load a pre-trained model (you must have this file!)
prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
prediction.loadModel()

# Predict the image
predictions, probabilities = prediction.predictImage(
    os.path.join(execution_path, "input/myphoto.jpg"), 
    result_count=5
)

# Print results
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)

```

# Run The Project
```
python process.py
```
# Sample Image
![dog](https://github.com/user-attachments/assets/f6be07dc-7c8d-4b30-a420-c084585cb180)

# Output After Running Script
```
golden_retriever  :  92.54
Labrador_retriever  :  5.32
cocker_spaniel  :  1.12
vizsla  :  0.54
Irish_setter  :  0.48
```

AfterImageAI predicts 92.54% sure that this is a golden retriever. processing the image, the AI model predicted the object as a golden retriever with a 92% probability.Other possible predictions included labrador retriever (5.3%) and cocker spaniel (1.1%), but the model was highly confident that the dog is a golden retriever.The high probability score indicates that the AI correctly recognized the breed based on features like the dog's fur color, body shape, and posture.Therefore,ImageAI predicts 92.54% sure that this is a golden retriever.

# Typical Inference Models for AI-based Image Recognition

Detecting people, objects, and vehicles

![image](https://github.com/user-attachments/assets/908a1dad-df6b-4921-bb4b-f02c3b65d490)

This inference model detects people, objects, and vehicles in images. People detection checks for congestion on streets and in open spaces, and the behavior of people at work in construction sites. Vehicle detection is used to check for congestion on highways.

Detecting human skeletal structure and posture

![image](https://github.com/user-attachments/assets/0687bc26-cd17-42d2-ac6a-ece1ff75aec5)

This technology detects the skeletal structure and posture of the human body by recognizing information about the head, neck, hands, and other parts of the human body. Deep learning technology is used to detect not only parts of the human body, but also optimal connections between them. In the past, skeletal structure and posture detection required expensive cameras that could estimate depth, but advances in AI technology have made detection possible even with ordinary monocular cameras.

# Typical Applications of AI Image Recognition Technology

Monitoring road traffic conditions

![image](https://github.com/user-attachments/assets/76c965d4-806d-4748-a7c6-025a84861965)

This system uses AI cameras and other devices to detect vehicles and monitor road traffic conditions. Road conditions such as increased traffic can be indicated in real time by using road signs. AI image recognition is also used in technologies that measure road surface conditions and how poor visibility is in bad weather.

Access control for buildings

![image](https://github.com/user-attachments/assets/eea67416-b1f6-4ba0-8430-c6f91e26e403)

This system uses biometric authentication technology based on AI image recognition to control access to buildings. The access control system uses biometric authentication technologies such as facial recognition, iris recognition, and fingerprint recognition to identify individuals and allow them to enter and exit without touching the authentication device. Since each biometric authentication has its own strengths and weaknesses, some systems combine multiple biometrics for authentication.

# Conclusion
ImageAI makes it easy for anyone to work with AI-powered image processing, even without deep knowledge of computer vision or machine learning. With simple tools for object detection, image classification, and training custom models, it helps developers and enthusiasts quickly build smart, practical applications. Whether you're working on a hobby project or building something for a real-world need, ImageAI takes the complexity out of AI and puts powerful image tools at your fingertips.
