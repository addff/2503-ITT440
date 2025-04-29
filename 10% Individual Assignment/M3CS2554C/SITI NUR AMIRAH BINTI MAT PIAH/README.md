**SITI NUR AMIRAH BINTI MAT PIAH**

**LECTURE'S: SHAHADAN BIN SAAD**



# *Title:  Book Detection and Counting*



## Introduction

Computer Vision is



## Overview
The script processes a video which applies a YOLOv8 model frame by frame to detect books in the shelf, annotstes the frames visually, displays the count in real time and saves the timestamped results in a CSV file.


## Key Features
- Real-time Book detection
- Live counter display
- CSV Logging with Timestamps
- Keyboard control to stop (q)

## Editor
PyCharm - An integrated development surroundings (IDE) used for programming in Python. Its provides code analysis, a graphical debugger an integration with version control systems.

*Programming languages: Python, Java*

*Developer: JetBrains*
![pycharm logo](https://github.com/user-attachments/assets/4ad4fc4a-84f3-4ee2-8c82-57934d85aab1)

## Tools
**1. YOLOv8 -** The model framework used for bbject detection

**2. OpenCV -** A toolset for image and video processing

**3. Pandas + CSV -** Managing and saving structured data


## Library
**1. ultralytics -** loading and using YOLOv8 object detection

**2. cv2 -** video capture, image annotation and frame display

**3. pandas -** logging detection results into a CSV file

**4. datetime -** generating timestamps

**5. os -** file system operations

## The Code


## *book_count.py*

	from ultralytics import YOLO
	import cv2
	import pandas as pd
	from datetime import datetime
	import os

**YOLOv8 model**

	model = YOLO("yolov8n.pt")  # Replace with your custom model if trained on books

**Video file**

	video_path = "bokshelfvid.mp4"
 
	cap = cv2.VideoCapture(video_path)
 
**CSV log file**

	csv_file = "book_log.csv"
 
	if not os.path.exists(csv_file):
 
		pd.DataFrame(columns=["Timestamp", "Frame", "Book Count"]).to_csv(csv_file, index=False)

	frame_count = 0

	while cap.isOpened():
 
		ret, frame = cap.read()
  
		if not ret:
  
			break

**Run detection**

	results = model(frame, conf=0.1, verbose=False)

**Count books**

    boxes = results[0].boxes
    book_count = len(boxes)

**Log into CSV**

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = pd.DataFrame([[timestamp, frame_count, book_count]], columns=["Timestamp", "Frame", "Book Count"])
    log_entry.to_csv(csv_file, mode='a', header=False, index=False)
    
  
**Annotate frame**

    annotated_frame = frame.copy()
    for idx, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(annotated_frame, f"Book {idx+1}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
		    
**Display book counter**

    cv2.putText(annotated_frame, f"Book Counter: {book_count}",
                (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)

    cv2.imshow("Book Detection", annotated_frame)

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
	
   **System exit**
   
	cap.release()
 
	cv2.destroyAllWindows()

 ## System output: Book Count Log

 ## *book_log.csv*
 
 <img width="391" alt="ss result pycharm" src="https://github.com/user-attachments/assets/0b91538c-33fe-413d-832f-de8304ba6fea" />
 
## Demostration
**Video File**

![bokshelfvid_mp4-0000](https://github.com/user-attachments/assets/16a373f7-bec4-42d7-ba25-4d58487dd476)


**Video Demostartion**

## Conclusion
