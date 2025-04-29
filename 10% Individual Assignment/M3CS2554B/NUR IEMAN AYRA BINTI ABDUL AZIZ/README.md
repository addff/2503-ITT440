# NUR IEMAN AYRA BINTI ABDUL AZIZ
# ITT440-CDCS2554B

# Smart Image Processing with ImageAI in Python


# Introduction
For this project, I chose to use ImageAI, a powerful Python library designed to simplify the development of applications with deep learning and computer vision capabilities. ImageAI makes it easy for developers, researchers, and students to perform complex tasks such as object detection, image prediction, and custom model training with just a few lines of code. Image processing, a crucial aspect of computer vision, involves enhancing, analyzing, and transforming images to extract valuable information, and ImageAI provides an accessible way to implement these techniques efficiently.

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


