# **ASSIGNMENT ITT440**  

**NAME** : Irfan Nazmi bin Mohd Salikhin  

**CLASS** : CDCS2554A

## 1. Introduction to MediaPipe

MediaPipe is an open-source framework developed by Google to build machine learning pipelines for processing multimodal data (video, audio, sensor data). It provides pre-built solutions for:

✅ Face Detection & Mesh (468 3D landmarks)

✅ Hand Tracking (21 landmarks per hand)

✅ Pose Estimation (33 body landmarks)

✅ Object Detection & Tracking

✅ Augmented Reality (AR) Effects

✅ Real-time processing (optimized for mobile & edge devices)

Why MediaPipe?

✅ Easy to use (few lines of code)

✅ Cross-platform (Python, Android, iOS, JavaScript)

✅ Pre-trained models (no need for deep learning expertise)

✅ GPU acceleration (supports OpenGL and Vulkan)

Reference:

MediaPipe Official Documentation

___

## 2. Setting Up MediaPipe in Python (VS Code)

### Installation

https://www.python.org/downloads/release/python-3109/ (Python 3.10.9)
https://code.visualstudio.com/download (VS Code)

To get started with MediaPipe, first install the required packages:

    pip install mediapipe opencv-python

### Basic Face Detection Example

A. Basic Face Detection

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

https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/face_detection.md

B. Hand Tracking (Gesture Recognition)

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

https://gautamaditee.medium.com/hand-recognition-using-opencv-a7b109941c88

___



  
