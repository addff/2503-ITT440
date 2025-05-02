NAME: NURIN ADRIANA BINTI YUSRIL A'MALI

CLASS: CDCS2554A

STUDENT ID: 2023226274

2503-ITT440 (INDIVIDUAL ASSIGNMENT)


# TITLE: CVG AND IMAGE PROCESSING USING PYTHON

# OBJECTIVE
- To write article about CVG and Image Processing using Python tools or library.
- To demonstrate coding used related to the article

# What is image processing

Image processing is a field of computer science that focuses on analyzing and manipulating digital images to enhance their quality or extract useful information. It allows computers to 
interpret and work with images in ways that mimic human vision. Common tasks in image processing include filtering to remove noise, adjusting brightness or contrast, detecting edges, and 
segmenting regions of interest within an image. It also involves transforming images through operations like resizing, cropping, rotating, or applying effects such as blurring or sharpening.
More advanced applications include object detection, where the system identifies and locates objects in an image, and classification, where it determines the category an image belongs to,
such as identifying whether an image contains a dog or a cat. Tools like OpenCV, PIL, and PyTorch provide powerful capabilities for image processing in programming languages such as Python.
This technology plays a vital role in many real-world applications, from facial recognition and photo editing to medical image analysis and autonomous vehicles.

# What is Pytorch?

![pytorch logo](https://github.com/user-attachments/assets/95ad54bb-8dac-4920-8a18-ea61aedd6c13)


PyTorch is an open-source machine learning framework developed by Facebook’s AI Research lab (FAIR).It is based on the Python programming language and the Torch library. It is widely used 
for building and training deep learning models, especially in areas like computer vision, image recognition and natural language processing. Written in Python, it’s relatively easy for
most machine learning developers to learn and use. PyTorch provides a powerful and flexible tensor computation library, similar to NumPy, but with strong support for GPU acceleration.
One of its key features is autograd which automatically computes gradients, making it easier to train neural networks through backpropagation. PyTorch also supports dynamic computation 
graphs, allowing developers to modify the model's structure during runtime, making it intuitive and easy to debug. Additionally, the torchvision package simplifies image loading, 
transformation, and the use of pretrained models like ResNet and YOLO. Thanks to its ease of use, scalability, and strong community support, PyTorch has become a popular choice among 
researchers, students, and industry professionals for developing AI applications.

# Key features of Pytorch

- It’s written in Python and integrated with popular Python libraries like NumPy for scientific computing, SciPy, and Cython for compiling Python to C for better performance. Because its 
syntax and usage are similar to Python’s, PyTorch is relatively easy for Python developers to learn.
- It’s well supported by major cloud platforms.
- The scripting language, called TorchScript, is easy to use and flexible when in eager mode. 
- It supports CPU, GPU, and parallel processing, as well as distributed training. This meana that computational work can be distributed among multiple CPU and GPU cores, and training can 
be done on multiple GPUs on multiple machines.
- The PyTorch Hub is a repository of pre-trained models that can be invoked, in some cases with just a single line of code.
- It has a large collection of tools and libraries in areas ranging from computer vision to reinforcement learning.
- Similar to NumPy array, an open source library of Python that adds support for large, multidimensional arrays, tensors are generic n-dimensional arrays used for arbitrary numeric 
computation and are accelerated by graphics processing units. These multidimensional structures can be operated on and manipulated with application program interfaces (APIs).

# Advantages of Pytorch 

- Offers developers an easy-to-learn, simple to code structure that's based on Python.
- Enables easy debugging with popular Python tools.
- Offers scalability and is well-supported on major cloud platforms.
- Provides a small community focused on open source.
- Exports learning models to the Open Neural Network Exchange (ONNX) standard format.
- Offers a user-friendly interface.
- Provides a C++ front-end interface option.
- Includes a rich set of powerful APIs that extend the PyTorch library.
- Ideal for Deep Learning Research since its dynamic computational graph allows flexibility, perfect for experimenting with new models.
- High Performance with GPU Acceleration by running operations on GPUs for faster training and inference.
- Automatic Gradient Calculation. It wil simplifies backpropagation with its built in autograd engine.
- Rich Ecosystem and Librariessince it comes with tools like torchvision (for vision tasks), torchaudio, torchtext, and PyTorch Lightning.
- Strong Community Support. It is backed by Facebook AI and widely adopted by industry and academia, ensuring lots of tutorials, examples, and help.


# Basic image processing

1. Resizing – Adjusting the dimensions of an image to a specific width and height (e.g., 224×224 for models like ResNet).
2. Color Jittering – Randomly changing the color properties (hue, saturation) for data augmentation.
3. Grayscale Conversion – Converting colored images into black-and-white to reduce complexity or match model requirements.
4. Blurring (e.g: Gaussian Blur)– Softening an image to reduce noise or simulate out-of-focus effects.
5. Normalization – Scaling pixel values to a specific range or distribution (e.g., mean=0.485, std=0.229 for ResNet input).
6.Image Tensor Conversion – Converting PIL or OpenCV images to tensors for use in PyTorch models.

These basic operations help clean, enhance, and prepare images for more complex tasks like classification or detection.

# Apps used for Pytorch

VS Code 

![vscode logo](https://github.com/user-attachments/assets/a3e52b09-91ca-414f-8c50-bfcb42c0d517)


PyTorch works well with VS Code, a powerful and lightweight code editor. VS Code is one of the most popular and widely used code editors for developing with PyTorch. VS Code supports 
Python and offers features like syntax highlighting, smart suggestions, debugging, and an 
integrated terminal. We can easily run PyTorch code, manage virtual environments, and use extensions for productivity. It's one of the best tools for PyTorch development.

# Written code

import torch

from torchvision import transforms

from PIL import Image

import os

#Load image

image = Image.open("rabbit.jpg").convert("RGB")  # Replace with your actual image path

#Create a folder to save outputs

os.makedirs("output_steps", exist_ok=True)

#Resize

resized = transforms.Resize((666, 666))(image)
resized.save("output_steps/resized.jpg")

#Color Jitter

color_jitter = transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1)
jittered = color_jitter(image)
jittered.save("output_steps/color jitter.jpg")

#Gaussian Blur

blurred = transforms.GaussianBlur(kernel_size=11, sigma=(4.0, 6.0))(image)
blurred.save("output_steps/blur.jpg")

#Random Grayscale (force apply for visualization)

grayscaled = transforms.RandomGrayscale(p=1.0)(image)
grayscaled.save("output_steps/grayscale.jpg")

#ToTensor and Normalize (not visually savable, but show applied)

final_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
input_tensor = final_transform(grayscaled).unsqueeze(0)


print("✅ Saved step-by-step processed images in 'output_steps/' folder.")


# Output

![rabbit original](https://github.com/user-attachments/assets/e0908f8a-42bc-42bc-abef-88f515c99975)

original picture

![grayscale](https://github.com/user-attachments/assets/e8d45593-0873-4730-9086-ecfd594cbc4c)

grayscale

![color jitter](https://github.com/user-attachments/assets/a191507d-ea69-43ad-8505-6377861fea27)

colour jitter

![blur](https://github.com/user-attachments/assets/e1cdb263-5d24-4e6d-b409-ab09a8c6ccd1)

blur

![resized](https://github.com/user-attachments/assets/0899502d-b9c0-4acc-9010-f1abdaae4ca2)

resized


# Demostration of Pytorch

https://youtu.be/XKg40A5t97A
