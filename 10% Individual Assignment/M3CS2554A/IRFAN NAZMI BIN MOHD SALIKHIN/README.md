# **ASSIGNMENT ITT440**  

**NAME**          : IRFAN NAZMI BIN MOHD SALIKHIN

**STUDENT ID**    : 2023414534

**CLASS**         : CDCS2554A

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

What is Computer Vision Graphic (CVG)?

✅ CV refines useful information from images on the computer.

✅ CG uses mathematical models and computer algorithms to generate images.

Reference:

[What is MediaPipe?](https://viso.ai/computer-vision/mediapipe/#:~:text=MediaPipe%20is%20an%20open%2Dsource,a%20graph%20of%20modular%20components.)

[Understand the Difference between Computer Vision (CV) and Computer Graphics (CG)](https://www.alibabacloud.com/blog/understand-the-difference-between-computer-vision-cv-and-computer-graphics-cg_599039#:~:text=CV%20and%20CG%20are%20two,or%20extracted%20in%20some%20features.)

___

## 2. Setting Up MediaPipe in Python (VS Code)

### Installation

https://www.python.org/downloads/release/python-3109/ (Python 3.10.9)

https://code.visualstudio.com/download (VS Code)

To get started with MediaPipe, first install the required packages:

    pip install mediapipe opencv-python

___

## 3. Code Demonstration: Real-Time Computer Vision with MediaPipe

### A. Basic Face Detection

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

### B. Hand Tracking (Gesture Recognition)

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

## 4. Video Tutorial

https://youtu.be/P5r4eA8Gp_0
