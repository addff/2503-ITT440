
NAME        : ROSE SYAIRAH BINTI ZAINOL 

STUDENT ID  : 2023443846  

COURSE CODE : ITT 440  

CLASS       : CDCS2554A  

## OBJECTIVES 
- To write article related to image processing and computer vision tools using Pyhton
- To demonstrate application of the chosen tools

## APPLICATION OF YOLO IN PYTHON FOR COMPUTER VISION AND GRAPHICS  
### 🧠 WHAT IS COMPUTER VISION & GRAPHICS (CVG) ?
The growth of Computer vision and graphics has led to substantial impact on the world. Computer vision is a part of Artificial Intelligence (AI) that allows computers to derive valuable data from visual inputs like photos and videos. The AI utilizes machine learning and neural networks to train computers and systems to extract the information from digital images and videos. To put it another way , it mimics human vision - where we perform visual tasks and retrieve the information.  Applications of computer vision include recognition, autonomous vehicles, security systems and medical imaging. Computer vision plays an important role in making systems more efficient, innovative and intelligent. 

### 📌 INTRODUCTION TO YOLO
<img src="https://github.com/user-attachments/assets/4f6dfc78-f6bb-43be-b9fd-2fffd40f1326" alt="Image" width="500"/>

**You Only Look Once (YOLO)** is an algorithm that is capable of **detecting real-time objects**. This is accomplished by technology called convolutional neural networks (CNN) that can predict various bounding boxes and class probabilities directly from the complete image in one evaluation. The YOLO model can process images in real-time at 45 frames per second which make it incredibly fast and efficient. It is used across multiple industry fields such as the medical sector for x-rays, MRIs or scans. YOLO’s ability to detect objects in real time is ideal for autonomous vehicles, allowing them to recognize and react to objects like other vehicles or traffic signals. Its strong capabilities made it gain popularity and led to rapid growth over the years. 


### 🚀 ADVANTAGES OF YOLO IN COMPUTER VISION
- **Speed**  
      YOLO is **extremely fast** since it does not deal with complex pipelines and deal with single-pass architecture. This means it can process images at high frame rate - within
      milliseconds.
   
- **Accuracy**  
    Not only is it fast, but YOLO also has a **high accuracy rate**. It can achieve state-of-the-art performance on various benchmarks meaning it can do real-time object detection with less error rate.

- **Efficiency**  
  YOLO is **incredibly efficient**. It does not require too much computational power. YOLO is still able to achieve comparable results despite having  fewer resources.
  
- **Open-Source**  
  YOLO is an **open-source project**, allowing developers to freely use, alter and improve it. This results in constant community improvement and advancement. 


### 🛠️ MODULES USED   
- _ultralytics.YOLO_ : main class
- _ultralytics.models_ : internal models
- _ultralytics.cfg_ : configs for training, validation and testing
- _ultralytics.utils_ : helper functions for logging, plotting and file handling

### ⚙️ METHODS APPLIED  
- _Yolo(“yolo8vn.pt”)_  // load the model
- _model(image.jpg)_  // perform prediction on images or videos
- _model.predict()_  // runs object detection and return results
- _results.show()_  // display the detection result in a window
- _results.save()_  // save images’ result with bounding boxes drawn

### 🖥️ INTEGRATED DEVELOPMENT ENVIROMENT (IDE) USED FOR YOLO  
<img src="https://github.com/user-attachments/assets/e88bd664-d8fd-4e95-82e9-3f07acd65561" alt="image" width = "450"/>

Integrated Development Environment or called IDE, is a software application that offers extensive features for developers. It serves to streamline the development process and boost productivity by providing a centralized hub for all the tools a developer requires.
Visual Studio Code, often known as VS Code, is one of IDE that provides an excellent source code editor. It merges strong tools with the simplicity of a source code making it perfect for both beginners and experienced users. VS Code works extremely well with Python as it features autocomplete and IntelliSense, debugging, unit testing and built in terminal access. Additionally, VS Code includes many programming languages such as C, C++, Java and Node.js. It operates smoothly with extensions like Pylance and Jupyter which allow debugging, data visualization and dependency management all in one place. Compared to other editors, VS Code is more organized, simple, potent, and efficient to work with. 

### 🐍 PYTHON CODE SAMPLE
  - **Object Detection: Image**
  ```python
  from ultralytics import YOLO
  import numpy

  # Load pre-trained YOLOv8 model
  model = YOLO("yolov8n.pt")

  # Predict on the image
  detection_output = model.predict(source="images/cooking.jpeg", conf=0.25, save=True)

  # Display tensor array
  print(detection_output)

  # Display numpy array
  print(detection_output[0].numpy())

```
- **Object Detection: Video**
 ```python
  from ultralytics import YOLO
  import cv2

  # Load model
  model = YOLO("yolov8n.pt")

  # Load the video
  cap = cv2.VideoCapture("images/trafficvid.mp4")

  # Get the frame size
  frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  # Save as mp4
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter("output_detected.mp4", fourcc, 30, (frame_width, frame_height))

  while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
          break

      # Run detection
      results = model(frame)
      annotated = results[0].plot()

      # Write frame to output
      out.write(annotated)

      # Show live
      cv2.imshow("Detection", annotated)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
  ```
  
 ### 🎬 YOLOV8 OBJECT DETECTION DEMONSTRATION VIDEO  
 In this video, I provide a quick demonstartion showing YOLO's effectivness and accuracy by performing for real-time object detection on both images and videos.  

<img src="https://github.com/user-attachments/assets/5bf350a4-31f2-4f02-b285-51339a17f673" alts="ss" width="300"/>

👉🏻 [ Demonstration Video ](url)
 
