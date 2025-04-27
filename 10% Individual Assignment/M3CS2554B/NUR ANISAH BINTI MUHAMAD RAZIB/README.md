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
Save the script in all files type and give the file name like analyzeface.py

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
Open python and open the script file. Run the file to get the output.  

Sample image for img1:

![Image alt](https://github.com/anisahrazib/smile/blob/3a44db51bd54d42bcf19adba5be6f6c98f4b48ab/smile.jpg)


The output:

![Image alt](https://github.com/anisahrazib/smile/blob/8c1110d6b1f29cca748380549b8e1558aa23ffa4/output.jpg)

-**Predicted Age** - The estimated biological age to predict how old the person in the photo looks. It's not the exact age but the model thinks the person in the photo to be around 29 years old.

-**Predicted Gender** - There is a 99.98% chance the person is a woman and only a tiny chance that the person is a man. It is almost 100% confident that the face belongs to a woman.

-**Dominant Emotion** - DeepFace analyzes the expression on the face to checks for emotions like happy, sad,angry and neutral. Here, happy is the dominant emotion.

-**Dominant Race** - DeepFace also estimates race or ethnicity based on facial features. It checks categories like white, black, asian, latino, indian and more. The dominant race of the person is asian.





