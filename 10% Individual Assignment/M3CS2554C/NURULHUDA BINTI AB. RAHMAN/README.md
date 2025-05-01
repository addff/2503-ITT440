## NURULHUDA BINTI AB. RAHMAN
## STUDENT ID : 2023365581
## CLASS : M3CS2554C


<ins>**Identifying Colors with OpenCV and Pandas**</ins>

#### Introduction to OpenCV and Pandas

OpenCV (Open Source Computer Vision Library) is a powerful library used for image processing and computer vision tasks. It provides tools for manipulating images and videos, detecting objects, applying filters, and even performing machine learning-based image analysis. OpenCV is widely used in applications such as facial recognition, augmented reality, and automated image classification.

Pandas is a data manipulation and analysis library designed for handling structured data efficiently. It provides tools for loading, filtering, and transforming datasets using intuitive data structures like DataFrames. In these scripts, Pandas is used to read a CSV file containing color names and RGB values, allowing easy comparison and matching of colors.

In this project, I use computer vision and image processing to identify the color at a specific pixel location from an image or a webcam feed. It employs the OpenCV library for real-time image capture and processing, alongside pandas for handling color data. The color detection system uses a CSV file containing RGB values and corresponding color names to map a selected color to its closest known name. By combining OpenCV for image processing and Pandas for data handling, these scripts efficiently identify and display color names from images and webcam feeds.

### Objective
- To develop an interactive system that detects and displays the name of a color based on a pixel selected in an image or video feed.
- To enable users to analyze colors from images or live webcam footage for educational, design, or development purposes.

### Tools

| Tool/Library | Description |
|--------------|-------------|
| **OpenCV (cv2)** | Handles image loading, video streaming, pixel manipulation, and GUI windows. |
| **Pandas** | Reads the CSV file containing RGB values and color names, enabling efficient lookup. |
| **NumPy** | (Implicitly used via OpenCV) Handles array and image data internally. |
| **Tkinter** | Provides a GUI file dialog to select images from the filesystem. |
| **colors.csv** | A CSV file storing color names and their corresponding RGB values. |


### How it Works
Part 1: Image Color Detection
   - Opens a file dialog to select one or more image files (.jpg, .png).
   - Resizes and displays each image in a window.
   - On left mouse click, it retrieves the RGB color of the clicked pixel.
   - It compares this RGB with all rows in colors.csv and finds the closest match.
   - Displays a colored rectangle with the name and RGB value of the detected color.
   - Press ESC to move to the next image.

   <img src="https://github.com/user-attachments/assets/818da0b7-f50b-456f-87ad-e7929f6c7b4d" width="600" height="500" />


Part 2: Webcam Color Detection
   - Captures video from the webcam in real-time.
   - Tracks the mouse movement across the window.
   - Continuously reads the pixel color under the cursor.
   - Matches it to the closest name from colors.csv.
   - Draws a colored rectangle and overlays the detected color name with RGB values.
   - Press ESC to exit.

      <img src ="https://github.com/user-attachments/assets/a720466e-4911-41cb-b5eb-62604c98e3c3" width="600" height="500" />)


### Conclusion
This project demonstrates a practical application of computer vision, allowing users to easily identify and label colors from any visual source. It combines image processing with user interaction to deliver a simple but effective color detection system. Such a tool can be useful in design, digital art, education, and accessibility.

### Demo
Click this link for Demo session : https://youtu.be/WKey80JH_d8

To run this program:
1. Ensure colors.csv is correctly formatted and present in the same directory.
<img src="https://github.com/user-attachments/assets/e96aa977-eb27-44a1-8427-7a9283771dcd" width="200" height="500" />

3. Install necessary dependencies using:
   **pip install opencv-python pandas numpy**

4. Run the script and select an image or use the webcam.

**Image color detection**

![image](https://github.com/user-attachments/assets/52816e99-be09-49ee-9c10-b6217d737696)

#### Webcam Color Detection
![image](https://github.com/user-attachments/assets/fe24c555-3adb-4dd0-868f-260f5deb0014)

5. Click on pixels in the image or move the cursor in the webcam feed to see color detection in action.









