**SITI NUR AMIRAH BINTI MAT PIAH**



# *Title:  Book Detection and Counting*


## Introduction

The study of computer vision aims to provide methods for computers to view and comprehend digital pictures, such as photos and videos. This involves developing techniques that aim that imitate human vision's capabilities. The automatic extraction of information from pictures, including object identification, camera position, and content search, is known as computer vision. Retrieving valuable information from pictures is the aim of computer vision.There are a lot of digital photos and videos available, so it's useful to focus on some of the basic computer vision problems that want to solve.

I focused on using object detection to help automatically count the number of books on a shelf whether there are hundreds or thousands. This makes the process faster, more accurate, and removes the need for manual counting.



## Overview
The primary highlight of this project is the ability to process a video frame by frame applying the YOLOv8 object detection structure. As the video plays, the system recognizes and counts the books on a shelf in real-time. Each detected book is identified by a visual bounding box, and a live counter is shown immediately on the video to indicate how many books are located in each frame. At the same time, the system saves the results, including the precise timestamp, frame number, and book count, to a CSV file. This enables both real-time visualization and thorough tracking or analysis later on, making it ideal for large-scale shelf monitoring where hundreds or thousands of books may be present.


## Key Features
- Real-time Book detection
- Live counter display
- CSV Logging with Timestamps
- Keyboard control to stop (q)

## Editor
**PyCharm -** An integrated development surroundings (IDE) used for programming in Python. Its provides code analysis, a graphical debugger an integration with version control systems.

***Programming languages:** Python, Java*

***Developer:** JetBrains*

![pycharm logo](https://github.com/user-attachments/assets/4ad4fc4a-84f3-4ee2-8c82-57934d85aab1)

## Tools
**1. YOLOv8 -** The model framework used for object detection

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

 ## Output Preview: Book Count Log

 ## *book_log.csv*
 
 <img width="391" alt="ss result pycharm" src="https://github.com/user-attachments/assets/0b91538c-33fe-413d-832f-de8304ba6fea" />

 ## Conclusion
In summary, this project shows how computer vision and deep learning, particularly YOLOv8, can automate the process of accurately and quickly counting books on shelves.  It processes the video frame by frame, producing a time-stamped record of the number of books for additional analysis in addition to providing real-time visual feedback.  This system can manage the volume of book inventories, huge book shops, and enormous books while lowering manual labour and increasing efficiency  any environment where counting and item detection are necessary.

The main challenge I faced in implementing this project was that it involved a lot of trial and error. I had to do a lot of trial-and-error, which included downloading and installing different Python libraries that were relevant and deleting any that weren't needed. I had to change the project structure since the code would occasionally not compile or execute properly, forcing me to start again in five separate directories.Even though it took a lot of effort and time, this approach  me a lot of chances to learn new things, gain a deeper grasp of computer vision, and develop my Python programming skills.  On the other side, this experience increased my technical skill development and given me the courage I need to manage technology-based projects in future.
 
## Demostration
**Sample video**

https://www.youtube.com/watch?v=vvKUuFk_uWI



**Demostration Book Detection and Counting**
https://youtu.be/S0RllfI3AGg



