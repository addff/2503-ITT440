# LUKMAN HAFIZI BIN MOHD ZAILAN

# SimpleCV

![image](https://github.com/user-attachments/assets/a2b1a218-5b7b-4e86-aeee-238bea65e7fe)


SimpleCV is an open-source Python framework designed to simplify Computer Vision (CV) tasks. Built on top of libraries like OpenCV, PIL, and NumPy, it provides a user-friendly interface for beginners and rapid prototyping.

- **Goal**: Make computer vision accessible to non-experts by abstracting complex code.

- **Key Features:**

  - Easy-to-use API for image loading, filtering, and analysis.

  - Built-in tools for feature detection, object tracking, and camera integration.

  - Works with webcams, IP cameras, and image files.

  - Cross-platform (Windows, macOS, Linux).

 # Applications of SimpleCV
- **Education**: Teach basic CV concepts without complex code.

- **Prototyping**: Quickly test ideas (e.g., object tracking, filters).

- **Raspberry Pi Projects**: Lightweight enough for IoT/embedded systems.

- **Augmented Reality (AR)**: Overlay graphics on live camera feeds.

# Installation

```bash
pip install simplecv  # For Python 2.7 (original version)
# Note: For Python 3, use the community fork "SimpleCV2":
pip install git+https://github.com/sightmachine/SimpleCV.git
```

# Basic Usage Examples
**1. Load and Display an Image**

```python
from SimpleCV import Image

# Load an image
img = Image("path/to/image.jpg")

# Display the image
img.show()
```

**2. Basic Image Manipulation**

```python
# Convert to grayscale
gray_img = img.toGray()

# Resize
small_img = img.resize(200, 200)

# Rotate
rotated_img = img.rotate(45)  # 45 degrees
```

**3. Edge Detection**

```python
edges = img.edges()  # Uses Canny edge detector
edges.show()
```

**4. Face Detection**

```python
# Load a face detection Haar cascade
faces = img.findHaarFeatures("haarcascade_frontalface_default.xml")

if faces:
    for face in faces:
        face.draw()  # Draw rectangles around faces
    img.show()
```

**5. Webcam Capture**

```python
from SimpleCV import Camera

cam = Camera()
img = cam.getImage()
img.save("webcam_snapshot.jpg")
```

# Complete Example: Face Detection Script

```python
from SimpleCV import Image, Camera

# Initialize camera
cam = Camera()

# Capture image
img = cam.getImage()

# Detect faces
faces = img.findHaarFeatures("haarcascade_frontalface_default.xml")

if faces:
    print(f"Found {len(faces)} faces!")
    for face in faces:
        face.draw()  # Draw a box around each face
    img.show()
else:
    print("No faces detected.")
```

# Example

![image](https://github.com/user-attachments/assets/e06196c0-8db5-4d0e-8b10-9745152f1d7a)
![image](https://github.com/user-attachments/assets/9d1d4a56-8680-4a43-8678-69fecac00a3c)
![image](https://github.com/user-attachments/assets/4a24f04e-5194-4cc0-aae4-1840785f6365)


