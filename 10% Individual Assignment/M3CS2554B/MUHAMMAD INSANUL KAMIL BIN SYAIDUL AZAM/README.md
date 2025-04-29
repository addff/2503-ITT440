# MUHAMMAD INSANUL KAMIL BIN SYAIDUL AZAM (2023699244)
### ITT440 - Individual Assignment

Object Detection is a task of computer vision that helps to detect the objects in the image or video frame. It helps to recognize objects count the occurrences of them to keep records, etc. The objective of object detection is to identify and annotate each of the objects present in the media.

YOLO(You Only Look Once) is a state-of-the-art model to detect objects in an image or a video very precisely and accurately with very high accuracy. In this tutorial, we will learn to run Object Detection with YOLO and plot the frames using OpenCV on both a recorded video and a camera.
![YOLO LOGO](https://raw.githubusercontent.com/goktug97/PyYOLO/master/pyyologo.png "YOLO Logo")

#### Steps to Detect Object with YOLO and OpenCV

##### Step 1: Setup the Environment
We will be using Ultralytics and OpenCV that can be installed using the following command:

``` python
pip install opencv-python
pip install ultralytics
```
![Screenshot](https://media.geeksforgeeks.org/wp-content/uploads/20240424215608/Screenshot-2024-04-24-215121.png "Screenshot")

After installation, create the file main.py, and download the video from the given reference or use any other video.

#### Step 2: Importing Necessary Libraries
```
import cv2
from ultralytics import YOLO
```
- cv2: It is the OpenCV python library.
- We import the YOLO from ultralytics to load the model and work upon it.

#### Step 3: Define Function to Get Class Colors
To generate random colours for different classes label and frame for object detection, we use the following method:

- The method takes the RGB extreme values as a tuple array
- Next we store the index in colour_index and choose the appropriate of R, G or B.
- Then we add some increments to the base colours to add variation.
- Finally we add modulus for keeping it in range
- Then we return the colour as tuple.

```
# Function to get class colors
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * 
    (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)
```

#### Step 4: Load YOLO Model
We will initializes the YOLO object detector with the specified model file (yolov8s.pt), which contains the pre-trained weights and configuration for the YOLOv8s model.
```
yolo = YOLO('yolov8s.pt')
```

#### Step 5: Open Video Capture

We are going to use the small model, since with better accuracy, it comes at the cost of speed. Now we are going to load the given model, and it will be downloaded in the project directory. Next, we will capture the video using VideoCapture(0) method.

```
videoCap = cv2.VideoCapture(0)
```

#### Step 6: Process Video Frames
This part of the code continuously captures frames from the video feed (videoCap.read()), processes each frame using YOLO (yolo.track()), and visualizes the detected objects in the frame.

```
while True:
    ret, frame = videoCap.read()
    if not ret:
        continue
    results = yolo.track(frame, stream=True)
    # Object detection and visualization code
```
#### Step 7: Main Loop for Real-time Object Detection
Continuously read frames from the video capture, perform object detection using YOLOv8s, and visualize the results.
```
    while True:
    ret, frame = videoCap.read()
    if not ret:
        continue
    results = yolo.track(frame, stream=True)


    for result in results:
        # get the classes names
        classes_names = result.names
```
Now we will iterate over the loop and then fetch each of the result. Each result contains the following attributes.

- orig_img: This is the original image as an numpy array.
- orig_shape: This tuple contains the frame shape.
- boxes: This is a array of Box objectsof Ultralytics containing bounding box. Each box has following parameters:
- xyxy: It contains the coordinates according to frame and we are going to use this for this tutorial.
- conf: It is the confidence value of the bounding box or the detected object.
- cls: It is the class of object. There are total 80 classes.
- id: It is the ID of the box.
- xywh: Returns the bounding box in xywh format.
- xyxy: It returns the bounding box in xyxy format but in normalized form that is from 0 to 1.
- xywhn: It returns the bounding box in xywh format but in normalized form that is from 0 to 1.
- masks: It is the collection of Mask objects for detection mask.
- probs: It contains the probability of each classification.
- keypoints: It is the collection of Keypoints which stores the collection of each keypoint.
- obb: It contains OBB object containing oriented bounding boxes.
- speed: It returns the speed of prediction. Faster computer with GPU gives better speed.
- names: It is the dictionary of classes with names and it is irrespective of prediction. The cls that we get in box can be used here to get the respective name.
- path: It is the path to image file.

Now for this tutorial, we will be needing only the boxes for drawing the bounding box.

Now each Box has the conf value, so we check if the confidence is greater than 40% or 0.4 or not. If yes, we draw the bounding box. According to that, we also label the Bounding box.

#### Step 8: Display Image and Break Loop
Show the annotated frame and break the loop if the 'q' key is pressed.
```
cv2.imshow('frame', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```

#### Step 9: Release Resources
Release video capture resources and close all windows.

```
videoCap.release()
cv2.destroyAllWindows()
```

FINAL CODE : 

```
import cv2
from ultralytics import YOLO

# Load the model
yolo = YOLO('yolov8s.pt')

# Load the video capture
videoCap = cv2.VideoCapture(0)

# Function to get class colors
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * 
    (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)


while True:
    ret, frame = videoCap.read()
    if not ret:
        continue
    results = yolo.track(frame, stream=True)


    for result in results:
        # get the classes names
        classes_names = result.names

        # iterate over each box
        for box in result.boxes:
            # check if confidence is greater than 40 percent
            if box.conf[0] > 0.4:
                # get coordinates
                [x1, y1, x2, y2] = box.xyxy[0]
                # convert to int
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # get the class
                cls = int(box.cls[0])

                # get the class name
                class_name = classes_names[cls]

                # get the respective colour
                colour = getColours(cls)

                # draw the rectangle
                cv2.rectangle(frame, (x1, y1), (x2, y2), colour, 2)

                # put the class name and confidence on the image
                cv2.putText(frame, f'{classes_names[int(box.cls[0])]} {box.conf[0]:.2f}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, colour, 2)
                
    # show the image
    cv2.imshow('frame', frame)

    # break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture and destroy all windows
videoCap.release()
cv2.destroyAllWindows()
```
