## NUR IEMAN AYRA BINTI ABDUL AZIZ
### ITT440-CDCS2554B

## Learn Image Processing with ImageAI in Python : ImageAI Analysis


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

# How is it work?

Setting Up ImageAI for Image Processing
Follow these steps :

1. Install Python
First, make sure you have Python 3.7 installed on your computer.
If you don't have Python yet, download and install it here : (https://www.python.org/downloads/release/python-3717/)


2. Install Required Libraries
Now, install TensorFlow and ImageAI.
```
pip install tensorflow
pip install imageai 
```

3. Prepare Project Folder
- Create folder into your desktop

4. Coding Detector Image
- For input image, load the model, do the object detection and also display the output
```
from imageai.Detection import ObjectDetection

class detectorImage:
    def init(self):
        self.detector = ObjectDetection()

    def setModelTypeAsTinyYOLOv3(self):
        self.detector.setModelTypeAsTinyYOLOv3()

    def setModelPath(self, path):
        self.detector.setModelPath(path)

    def loadModel(self):
        self.detector.loadModel()

    def detectObjectsFromImage(self, input_image, output_image_path):
        return self.detector.detectObjectsFromImage(
            input_image=input_image,
            output_image_path=output_image_path
        )

```
5. Main Script
- Running the code for run_detector to perform object detection

```
import sys
sys.path.append(r'C:\Users\hp\Desktop\imagedetection')  # Add the path to the imagedetection folder

from imagedetection import detectorImage
import os

# Initialize the detector
detector = detectorImage.detectorImage()  # Access the class from the module

# Define paths
model_path = "C:/Users/hp/Desktop/imagedetection/Models/yolo-tiny.h5"
input_path = "C:/Users/hp/Desktop/imagedetection/Input/CAR.jpg"
output_path = "C:/Users/hp/Desktop/imagedetection/Output/CAR_detected.jpg"

# Check if paths exist
print(f"Model Path Exists: {os.path.exists(model_path)}")
print(f"Input Image Path Exists: {os.path.exists(input_path)}")
print(f"Output Path Exists: {os.path.exists(output_path)}")

# Load the model
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

# Perform detection
detections = detector.detectObjectsFromImage(
    input_image=input_path,
    output_image_path=output_path
)

# Print the results
for item in detections:
    print(f"{item['name']} : {item['percentage_probability']}")
```


# Conclusion
ImageAI makes it easy for anyone to work with AI-powered image processing, even without deep knowledge of computer vision or machine learning. With simple tools for object detection, image classification, and training custom models, it helps developers and enthusiasts quickly build smart, practical applications. Whether you're working on a hobby project or building something for a real-world need, ImageAI takes the complexity out of AI and puts powerful image tools at your fingertips.

# Refer to this link 
[Learn How To Use](https://youtu.be/PdpUn861ZtU?si=6yQLiysURxtwyBPn)
