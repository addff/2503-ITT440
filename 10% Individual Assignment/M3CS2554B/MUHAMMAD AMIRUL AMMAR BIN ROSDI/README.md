##### Published By : MUHAMMAD AMIRUL AMMAR BIN ROSDI
##### Published Date : 25 APRIL 2025
# **Image Processing using MoviePy**
## *1. What is Image Processing*
Image processing is the process of transforming an image into a digital form and performing certain operations to get some useful information from it. The image processing system usually treats all images as 2D signals when applying certain predetermined signal processing methods.
## *1.1 Types of Image Processing*
There are 5 types of image processing :
- **Visualization** - Find objects that are not visible in the image
- **Recognition** - Distinguish or detect objects in the image
- **Sharpening and Restoration** - Create an enhanced image from the original image
- **Pattern Recognition** - Measure the various patterns around the objects in the image
- **Retrieval** - Browse and search images from a large database of digital images that are similar to the original image
## *2. What is MoviePy*
![logo](https://github.com/user-attachments/assets/79eb1580-78a2-4fa9-9e58-8f0107a537ef)

MoviePy is a powerful Python library used for video editing, compositing, and processing. It's often used for video manipulation but also supports frame-by-frame image processing, allowing you to apply effects, filters and transformations using Python.
## *2.1 Why choose MoviePy for Image Processing*
MoviePy stands out as a developer-friendly, Pythonic solution for processing and editing video with image processing techniques. Its ability to apply custom Python functions to each frame, along with built-in support for audio, overlays, transitions and text, makes it an all-in-one toolkit for creating high quality video content programmatically.
## *3. How to install MoviePy*
## *Step 1 : Install Python*
1. Go to the official Python website: https://www.python.org/downloads/windows/
2. Download the latest Python
3. Run the installer.

To verify installation, open Command Prompt (Win + R, then type cmd) and run :
```bash
python --version
```
## *Step 2 : Install pip*
1. After installing Python, pip should already be available.
```bash
pip --version
```
## *Step 3 : Install MoviePy*
1. Open Command Prompt (press Win + S, type "cmd", and open it).
2. Run this command.
```bash
pip install moviepy
```
3. It will automatically download and install MoviePy and its dependencies.
## *Step 4 : Testing if it works*
1. In Command Prompt, type this.
```bash
import moviepy.editor as mp
print("MoviePy installed successfully!")
```
2. If success, it will prints that line without errors.
## *4. Tutorial to rotate video using MoviePy*
```Python
# Import everything needed to edit video clips 
from moviepy.editor import *
  
# loading video intro  
clip = VideoFileClip("dsa_geek.webm") 
  
# clipping of the video  
# getting video for only starting 10 seconds 
clip = clip.subclip(0, 10) 
  
# rotating video by 180 degree 
clip = clip.rotate(180) 
  
# Reduce the audio volume (volume x 0.5) 
clip = clip.volumex(0.5) 
  
# showing clip 
clip.ipython_display(width = 280)
```
This the result of the tutorial
## Demo Projek

🎥 [Klik untuk tonton video demo](https://media.geeksforgeeks.org/wp-content/uploads/20200721003455/19.mp4)

