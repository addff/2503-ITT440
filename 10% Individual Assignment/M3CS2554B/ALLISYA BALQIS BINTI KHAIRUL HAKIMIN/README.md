# ALLISYA BALQIS BINTI KHAIRUL HAKIMIN
## 2023491708
## INDIVIDUAL ASSIGNMENT
## OBJECT DETECTION WITH CAFFE
![image](https://github.com/user-attachments/assets/aa9e59e4-2ae6-4783-bb1b-77f70dc9a1ba)


Caffe (Convolutional Architecture for Fast Feature Embedding) is an open-source deep learning library that has astrong reputation for speed, expressiveness and modularity. It was developed at the University of California, Berkeley, but has been widely utilized in academia, research, and industry particularly in computer vision tasks.

## Applications
Caffe has been widely used in various deep learning applications particularly in:
* Image Classification: Identifying objects within images
  
* Object Detection: Locating and classifying multiple objects in an image
  
* Image Segmentation: Dividing an image into meaningful regions.
  
* Feature Extraction: Using trained networks to extract useful features form images for other tasks.
  
* Multimedia Analysis: Processing video and other multimedia data.

## Core Features and Design Principles:
* Speed: It's using C++ and can be CPU and GPU-accelerated(via CUDA and CuDNN), which makes it extreamly efficient for both training ad inference, especially with convolutional neural networks (CNNs). It's designed to support high-performanve computing.

* Modularity: Caffe has a modular design where neural networks are created by connected layers. Every layer contains a particular computation, such as convolution, pooling, activation, or loss computation. Modularity benefits experimenting with different network architectures as well as debugging.

* Interfaces: Caffe provides interfaces for command-line usage, Python and MATLAB, offering flexibility for different user preferences and workflow.

# STEPS ON HOW TO IMPLEMENT

## 1. Install Requirement
First, you need to install Caffe and Python bindings built

## 2. Import Libraries
```
import numpy as np
import cv2
```

##  3. Set caffe to CPU or GPU mode
### CPU mode
``` caffe.set_mode_cpu ```

### GPU mode
```
caffe.set_mode_gpu()
caffe.set_device()
```

## 4. Load the Network
Download Petrained Model Files
* deploy.prototxt - model architecture
* mobilenet_iter_73000.caffemodel -the trained weight

```
model_def = 'deploy.protxt'
model_weight = 'mobilenet_iter_73000.caffemodel'

net = caffe.Net(model_def,model_weight, caffe.TEST)
```

## 5. Load the Preprocess Image
Load your input image
```
image = cv2.imread('test.jpg')
(h, w) = image.shape[:2]

# Resize and preprocess image for the network
resized_image = cv2.resize(image, (300, 300)).astype(np.float32)
resized_image = (resized_image - 127.5) * 0.007843  # Normalization

# Caffe expects (channels, height, width) format
resized_image = resized_image.transpose((2, 0, 1))  # (HWC) -> (CHW)

# Set the data into the net
net.blobs['data'].reshape(1, *resized_image.shape)  # Reshape if needed
net.blobs['data'].data[...] = resized_image
```

## 6. Forward Pass
Perform forward pass to get detections
```
output = net.forward()
detections = output[detection_out]
```

## 7.  Parse and Visualize Detections
List of class labels (for MobileNet SSD)
```
classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```
### Loop over detection
```
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.5:
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        label = f"{classes[idx]}: {confidence * 100:.2f}%"
        print(f"[INFO] Detected {label}")

        # Draw bounding box and label on image
        cv2.rectangle(image, (startX, startY), (endX, endY),
                      (0, 255, 0), 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show the final image
cv2.imshow("Caffe Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Full Code
```
import cv2
import numpy as np

model_def = 'deploy.prototxt'
model_weights = 'mobilenet_iter_73000.caffemodel'

# Load the model using OpenCV's dnn module
net = cv2.dnn.readNetFromCaffe(model_def, model_weights)

image = cv2.imread('test.jpg')
(h, w) = image.shape[:2]

# Preprocess the image
blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)

# Set input and forward pass
net.setInput(blob)
detections = net.forward()

classes = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.5:
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        label = f"{classes[idx]}: {confidence * 100:.2f}%"
        print(f"[INFO] Detected {label}")

        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("Caffe Detection (via OpenCV)", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
## Demonstration Video
[![Watch the video](https://img.youtube.com/vi/Q6lgimLBqfw/0.jpg)](https://www.youtube.com/watch?v=Q6lgimLBqfw)
