# **ASSIGNMENT ITT440**  

**NAME** : Irfan Nazmi bin Mohd Salikhin  

**CLASS** : CDCS2554A

## 1. Introduction to MediaPipe

MediaPipe is an open-source framework developed by Google to build machine learning pipelines for processing multimodal data (video, audio, sensor data). It simplifies many advanced computer vision and machine learning tasks and provides pre-built solutions for tasks like face detection, hand tracking, pose estimation, and more.

Reference:

MediaPipe Official Documentation

___

## 2. Setting Up MediaPipe in Python

### Installation

To get started with MediaPipe, first install the required packages:

    pip install mediapipe opencv-python numpy matplotlib

Reference:

Installing MediaPipe in Python

### Basic Face Detection Example

A basic face detection implementation using MediaPipe:

    import cv2
    import mediapipe as mp
    
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    
    # Open webcam
    cap = cv2.VideoCapture(0)
    
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                continue
            
            # Convert BGR to RGB & process
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image_rgb)
            
            # Draw face detections
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
            
            cv2.imshow('Face Detection', image)
            if cv2.waitKey(5) & 0xFF == 27:  # Press ESC to exit
                break
    
    cap.release()
    cv2.destroyAllWindows()

Reference:

MediaPipe Face Detection Guide

___

## 3. Key MediaPipe Use Cases for Your Assignment

### A. Hand Tracking (Gesture Recognition)

Detects 21 landmarks per hand, useful for applications like sign language recognition or virtual controllers.

    import cv2
    import mediapipe as mp
    
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    
    cap = cv2.VideoCapture(0)
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue
        
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

Reference:

Hand Tracking with MediaPipe

### B. Pose Estimation (Fitness Apps, Motion Analysis)

Detects 33 body landmarks used in applications like yoga apps, sports analysis, and animation.

    import mediapipe as mp
    
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    
    # (Similar loop as above, replace with `results.pose_landmarks`)

Reference:

Pose Estimation with MediaPipe

### C. Face Mesh (AR Filters, Virtual Makeup)

Detects 468 3D landmarks for facial features, such as lips, eyes, and jawline, used in AR applications like Snapchat filters.

    import mediapipe as mp
    
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()
    
    # (Similar loop as above, replace with `results.multi_face_landmarks`)

Reference:

Face Mesh with MediaPipe

___



  
