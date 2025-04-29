## Face Detection Attendance System

## Introduction  
Face Detection is a task in computer vision used to identify and locate human faces in images or video streams. It plays an important role in security systems, user authentication, and smart automation such as attendance tracking.  
The goal of face detection is to detect the presence of a face and determine its location within the frame.  

In this project, I implemented a **Face Detection Attendance System** using **MediaPipe** and **OpenCV** in Python. MediaPipe is used for real-time, high-accuracy face detection, while OpenCV handles video capture and display.  
This system detects faces from a webcam feed and records attendance by saving the date and time into a CSV file. It provides a simple, contactless solution for automating attendance in various settings such as classrooms or offices.  

I chose the tools **MediaPipe** and **OpenCV** under the category of **Computer Vision & Graphics (CVG)**, as the main focus of my project is face detection and real-time graphics processing.



## Objectives
- Develop a Face Detection Attendance System using Python, MediaPipe, and OpenCV.
- Apply computer vision techniques for detecting and tracking human faces in real-time.
- Automate the attendance-taking process by recording date and time into a CSV file when a face is detected.
- Explore the use of MediaPipe for accurate facial landmark detection and OpenCV for video processing.
- Gain hands-on experience in implementing a real-time CVG (Computer Vision & Graphics) application.



## 🧰 Tools & Libraries Used

| Tool/Library       | Description                                                                 | Logo |
|--------------------|-----------------------------------------------------------------------------|:----:|
| **Python**         | The core language that ties together all parts of the system.               | <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="60"/> |
| **OpenCV (cv2)**   | Captures webcam frames, handles drawing operations, and displays live feed. | <img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" width="60"/> |
| **MediaPipe**      | Provides FaceMesh solution for real-time face detection.                    | <img src="https://github.com/user-attachments/assets/ea39c8fa-2421-48a0-a2c0-cf8129bf2f05" width="60"/> |
| **NumPy**          | Used for efficient numerical operations, such as finding minimum distances. | <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width="60"/> |
| **playsound**      | Plays a sound clip when a face is successfully recorded.                    | 🎵 |
| **datetime module**| Fetches current date and time for attendance timestamps.                    | 🕒 |




## ⚙️ How It Works

### 1.Video Capture
The system begins by capturing video from the **webcam** using OpenCV.

<img src="https://github.com/user-attachments/assets/be0cc9b9-1f33-45eb-ba5c-221c4cf3685d" width="500"/>


### 2.Face Detection
Each video frame is passed to **MediaPipe**, which performs real-time face detection.

<img src="https://github.com/user-attachments/assets/314efa1d-1cc8-4007-aadc-78710bb510a2" width="500"/>


### 3.Attendance Tracking
Once a face is detected, the system records the **date and time** into a CSV file.

<img src="https://github.com/user-attachments/assets/482b5514-a6a7-4dca-bf16-e23107b837ac" width="250"/>


### 4.Face Validation
The bounding box helps validate that a real face is within the frame.

<img src="https://github.com/user-attachments/assets/690db802-c27e-4873-b838-36dd7cbb5f88" width="250"/>


### 5.Continuous Monitoring
The system monitors continuously. New faces are automatically recorded.

<img src="https://github.com/user-attachments/assets/be0cc9b9-1f33-45eb-ba5c-221c4cf3685d" width="500"/>


### 6.Output
The final output is a **CSV file** containing the timestamps.

<img src="https://github.com/user-attachments/assets/09e125d1-3416-4728-925f-41d74f423d1b" width="300"/>


## Conclusion  
The Face Detection Attendance System developed in this project demonstrates how computer vision technologies like **MediaPipe** and **OpenCV** can be used to build real-time, contactless solutions for everyday tasks such as attendance tracking.  

By leveraging Python and its powerful libraries, this system detects faces through a webcam, automatically marks attendance, and saves records without manual input.  

This project strengthened practical skills in image processing and real-time video analysis, and highlighted the importance of automation in modern environments such as schools, offices, and events.  
It serves as a foundation that can be expanded further—for example:
- Adding face recognition for personalized attendance
- Integrating cloud storage for centralized access

Overall, this assignment provided valuable hands-on experience in implementing a real-time CVG solution using Python.


## 📺 Demo Video

Watch the full demo of the **Face Detection Attendance System** on YouTube:

[![Watch the video](https://img.youtube.com/vi/quoSsjWPYMw/hqdefault.jpg)](https://youtu.be/quoSsjWPYMw?si=H7KTewwRyzUnZkro)

> Click the image or [watch on YouTube](https://youtu.be/quoSsjWPYMw?si=H7KTewwRyzUnZkro)

