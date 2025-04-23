# MUHAMMAD AIMAN HAZIQ BIN ABDUL RAHIM

ITT440 - INDIVIDUAL ASSIGNMENT

Object detection is a fundamental task in computer vision that involves identifying and localizing objects within an image or video. Unlike image classification, which predicts a single label per image, object detection provides both the class labels and bounding boxes for multiple objects in a scene.

This project leverages PyTorch, a powerful deep learning framework, to build and train an object detection model. Using state-of-the-art architectures like Faster R-CNN, YOLOv5, or SSD, the model is capable of detecting and classifying objects in real time or on static images with high accuracy.

![image](https://github.com/user-attachments/assets/2728f0ed-ff45-4c03-a5a2-3bce0d56373e)

Pytorch is widely used for deep learning framework for building and training models.

Here are the step to setup the environment using Pytorch:

Step 1: Choose Python Environment Tool
Pick one:

Option A: Conda (recommended)
Easiest to manage Python versions + packages

Works on Windows, Mac, Linux

Option B: venv + pip
Comes with Python by default

Lightweight and fast

If you're not sure, go with Conda.


Step 2: Install Python (if not already)
Install Python 3.8–3.11. Check:
python --version

Step 3: Create a Virtual Environment

Conda :
conda create -n pytorch-env python=3.10
conda activate pytorch-env

venv :
python -m venv pytorch-env
source pytorch-env/bin/activate  # Mac/Linux
pytorch-env\Scripts\activate     # Windows

Step 4: Install PyTorch
Check your system:
Go to https://pytorch.org/get-started/locally/ and copy the install command that matches:

OS: Windows, Linux, macOS

Package manager: pip or conda

Compute: CPU or CUDA (GPU)

CPU only (safe default):
# pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# conda
conda install pytorch torchvision torchaudio cpuonly -c pytorch

With CUDA (NVIDIA GPU support):
# For CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# conda
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

Step 5: Test PyTorch
In Python:
import torch
print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
✅ You should see your version and True for CUDA if GPU is available.

Now here are the steps on Object Detection using Pytorch :

We will use a PRETRAINED MODEL that can detect objects and create boxes around them. 
This has many applications in real life such as self driving cars.

First: Import both of this tools
![image](https://github.com/user-attachments/assets/cbabee2d-8647-4c1b-ac4b-f65458c46fab)

Next : Use this command to download the pretrained model
![image](https://github.com/user-attachments/assets/fd2ac6d2-43c7-412b-8a26-363ee0f8b745)

Then : You need to put it into evaluation mode
![image](https://github.com/user-attachments/assets/f47ae1d0-48b4-4ebb-8ad2-198be324a2a5)

After that : We get the list of names :
![image](https://github.com/user-attachments/assets/b5e47e12-ec55-4e29-af5e-402862fba837)

Next : import these things for images and other functions
![image](https://github.com/user-attachments/assets/a31a31d6-fb4f-4929-a239-f2acdd3ea421)

After that : code the get_prediction method 
![image](https://github.com/user-attachments/assets/db0758df-b31f-400d-8e9a-58730b630dce)

Next : make this function and import random 

![image](https://github.com/user-attachments/assets/312149a3-7bd1-4d88-97d4-558e184cd39e)

Lastly : make an object detection method 
![image](https://github.com/user-attachments/assets/f9dbd06e-3ce4-49f8-bcdb-c4522d4acf06)

RESULTS

Here are the sample for an image with multiple cars for this model to detect.

![image](https://github.com/user-attachments/assets/910e089c-2eb4-4655-9b64-ce319a4cc753)

![image](https://github.com/user-attachments/assets/97402eb4-12ae-4ee3-939b-3e7821943aef)

as you can see, it is able to detect it all as a car and create boxes around them.

That's all from me, Thank You





