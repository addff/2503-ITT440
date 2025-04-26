# NUR ANISAH BINTI MUHAMAD RAZIB
# 2023449312
# ITT440 (INDIVIDUAL ASSIGNMENT)
# BASIC FACE ANALYSIS USING DEEPFACE

![DEEPFACE LOGO](https://raw.githubusercontent.com/serengil/deepface/master/icon/deepface-icon-labeled.png)
#### Overview
This project uses the DeepFace library in python to perform face analysis on a given image. It predicts four attributes of the person in the image.
- **Age**
-  **Gender**
-  **Emotion**: such as happy,sad,angry
-   **Race/Ethnicity**: like white,black,asian
#### Why use DeepFace?
DeepFace is a powerful and beginner-friendly python library that makes face recognition and analysis easy to use. Only a few lines of python code needed to analyze the image. We also can switch models easily based on our project needs.
#### Tools and Libraries Used
- **Phyton 3** - Main programming language used to write and run the script.
- **DeepFace** - Library for face analysis (age,gender,emotion,race).
- **TensorFlow** - Deep learning framework used by DeepFace for AI model predictions.
- **OpenCV** - Used for image handling and face detection tasks.
#### How to Use DeepFace for Face Analysis 
#### Step 1: Install DeepFace
```bash
pip install deepface
pip install tensorflow
pip install opencv-python
```
#### Step 2: Write python script using notepad
```python
from deepface import DeepFace
try:
    result = DeepFace.analyze(
        img_path="img1.jpg",                     
        actions=['age', 'gender', 'race', 'emotion'], 
        enforce_detection=False                 
    )
    print("Full Analysis Result:")
    print(result)

    print("\nSummary:")
    print(f"Predicted Age: {result[0]['age']}")
    print(f"Predicted Gender: {result[0]['gender']}")
    print(f"Dominant Emotion: {result[0]['dominant_emotion']}")
    print(f"Dominant Race: {result[0]['dominant_race']}")

except Exception as e:
    print(f"Error: {e}")
```
#### Step 3: Prepare your folder
 - **1** - create a folder
 - **2** - save your python script inside the folder
 - **3** - save the image you want to analyze in the same folder
#### Step 4: Run the script using python 
