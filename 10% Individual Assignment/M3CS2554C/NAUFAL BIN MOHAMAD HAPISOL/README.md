# NAME : NAUFAL BIN MOHAMAD HAPISOL
# STUDENT ID : 2024665804

---

# Image Processing with Imageio

# 1. What is Image Processing?
Image processing is the technique of manipulating and analyzing digital images to enhance their quality, extract useful information, or automate visual tasks. It involves applying mathematical operations and algorithms to images for:

- *Enhancement* (brightness, contrast, sharpening)
- *Restoration* (noise removal, deblurring)
- *Segmentation* (object detection, edge detection)
- *Compression* (reducing file size)
- *Feature extraction* (pattern recognition)
  
#### Image processing is widely used in fields like medicine, robotics, surveillance, and computer vision.

---

# 2. Image Processing with Imageio

<div align="center">
<img align="center" width="200" height="200" src="https://github.com/Naufalhapisol/ITT440/blob/bb28775928d558c23c5118b29c8fcb25e1c8d3be/imageio.png">
   
</div>

ImageIO is a Python library designed for reading and writing various image formats. It provides a simple, efficient way to handle images in scientific and research applications. Unlike OpenCV or PIL, ImageIO supports animated images, medical formats (DICOM), and volumetric data.

---

# 3. How to Install Imageio

You can install Imageio using pip:

   ``` python
   pip install imageio
   ```
For additional plugins (e.g., for medical imaging):
   ``` python
   pip install imageio[ffmpeg]  # For video support
   pip install imageio[dicom]   # For medical images
   ```
---

# 4. How to Use Imageio

a. Reading an Image

   ``` python
   import imageio.v3 as iio

   # Read an image into a NumPy array
   image = iio.imread("image.jpg")  
   print(image.shape)  # (height, width, channels)
   ```
b. Writing / Saving an Image

   ``` python
  import numpy as np

  # Create a random image (NumPy array)
  random_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

  # Save the image
  iio.imwrite("random.png", random_image)
   ```
c. Reading Frames from a Video/Gif
   ``` python
  # Read all frames from a GIF
  frames = iio.imread("animation.gif")  

  # Iterate through frames
  for frame in frames:
  print(frame.shape)  # Each frame is a NumPy array
   ```
d. Converting Image Formats
   ``` python
  # Read a PNG and save as JPEG
  image = iio.imread("input.png")  
  iio.imwrite("output.jpg", image)
   ```
---

# 5. Example: Converting Video (MP4) to (GIF)

Step 1: Install Required Libraries
   ``` python
!pip install imageio[pyav] --quiet
from google.colab import files
uploaded = files.upload()  # Upload your MP4
   ```
Step 2: Code Implementation
   ``` python
# 2. MAIN CONVERSION CODE
import imageio.v3 as iio
from IPython.display import display, Image
import os

# 3. USER SETTINGS (edit these)
input_video = "IMG_5738.mp4"  # ← Your MP4 file
output_gif = "output.gif"
duration_seconds = 4  # Max clip length
output_fps = 10       # GIF frames per second
quality = 8           # 1-10 (higher=better quality)

# 4. SMART FRAME PROCESSING
try:
    # Verify file exists
    if not os.path.exists(input_video):
        raise FileNotFoundError(f"❌ File '{input_video}' not found. Please upload it!")
    
    print("⏳ Processing your MP4...")
    
    # Calculate optimal frame count
    total_frames = duration_seconds * output_fps
    
    # Read and select frames efficiently
    frames = []
    for i, frame in enumerate(iio.imiter(input_video, plugin="pyav")):
        if i >= total_frames * 2:  # Process 2x needed frames for selection
            break
        if i % 2 == 0:  # Skip every other frame for smoother playback
            frames.append(frame)
            if len(frames) >= total_frames:
                break
    
    # Create optimized GIF
    iio.imwrite(
        output_gif,
        frames[:total_frames],  # Ensure exact frame count
        duration=1000/output_fps,
        loop=0,
        quality=quality
    )
    
    # Show results
    print(f"🎉 Success! Created {output_gif}")
    print(f"📊 Stats: {len(frames)} frames | {os.path.getsize(output_gif)/1024:.1f} KB")
    display(Image(filename=output_gif))
    
except Exception as e:
    print(f"🔥 Error: {str(e)}")
    print("\n💡 TROUBLESHOOTING:")
    print("1. Confirm filename is EXACT (including .mp4)")
    print("2. Try shorter duration_seconds")
    print("3. Click 'Restart Kernel' if memory errors occur")
   ```
Output:
- the video (MP4) turn to (GIF)
  
Converting videos to GIFs using Python and ImageIO is a powerful yet straightforward process, ideal for automating animations, creating social media content, or enhancing presentations.  

Click the link below for tutorial that i have made:

https://youtu.be/SG7ew9Jek-Q?si=VMl-cG48qUZnCM-O

---

# 6. Conclusion
- *ImageIO is a powerful yet simple library for reading, writing, and converting images in Python.*
- *Useful for medical imaging, video processing, and batch image operations.*

