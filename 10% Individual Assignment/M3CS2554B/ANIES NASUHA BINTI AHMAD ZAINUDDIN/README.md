# ANIES NASUHA BINTI AHMAD ZAINUDDIN
# 2023268475
# ITT 440 Individual Assignment 

# Computer Vision Graphics (CVG) using Pygame

📸 Computer Vision Graphics (CVG) is a field that focuses on the visualization and presentation of image and video data using graphical elements. Unlike image processing, which manipulates pixel-level data for analysis, CVG emphasizes how visual data is represented and interacted with in a graphical interface.

I made a decision to choose pygame because it is one of the popular tools that can be used in Python for CVG-related projects. Pygame is a cross-platform set of Python modules designed for creating video games, but it also supports multimedia applications, including CVG tasks.

Pygame is an open-source library that is based on SDL (Simple Direct Media Layer), It also supports 2D graphics, sounds, and event handling, making it ideal for visual and interactive applications. Eventhough Pygame is commonly utilized for developing games and multimedia applications. Nonetheless, it also highly useful for Computer Vision Graphics (CVG) projects involving real-time visuals and graphical data presentation.

 ## Why use Pygame for CVG ?

✔️ Overlay graphics or text on video/image 

✔️ Allows rendering of dynamic image frames or video-based graphics easily.

✔️ Supports real-time interaction through keyboard, mouse, or frame updates.

✔️ Simplifies development for students or beginners new to computer vision or graphical rendering.

✔️ Can be used to simulate image-based animations, visual tracking output, or frame-based displays.

## Programming languange

- Pygame is written in python

- Works weel with python 3.7 - 3.13

## Tools needed for Pygame

💠Python - main language Pygame

💠Pygame library - rendering and visuals

💠Visual studio code - writing and running code

💠Images or videos

## Pygame Installation 
1. Make sure Python is installed (python 3.13)

2. Open command prompt

3. Run the following command
   
<pre> pip install pygame </pre>

4. To verify installation

<pre> python -m pygame.examples.aliens </pre>
   
 ## Steps To Implement Pygme in a CVG Project

1. Install Python & Pygame

2. Prepare the image or video

3. Import Pygame and initialize 

<pre>
import pygame
</pre>

4. Create a display surface
   
<pre>screen = pygame.display.set_mode((640, 480))
</pre>

5. Load and display the image

<pre>img = pygame.image.load("your_image.jpg")
screen.blit(img, (0, 0))
pygame.display.update()
</pre>

6. Create a game loop

<pre>
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
</pre>

## Advantages of using Pygame

🧠 **Easy to learn and use**
    
Pygame has a simple and beginner friendly syntax, making it accessible even for students who are new to graphics programming or Python

⚙️ **Minimal setup**

Installation is straightforward with a single pip install pygame command and also there are no complex configurations or external 
dependencies needed. 

🎥 **Great for frame by frame rendering**

The whole aspect of Pygame is in handling 2D graphics and creating static or dynamic image sequences. This is very useful for CVG tasks such as video frame display, animated images, or simulation.

🎮 **Support real time interaction**

With its embedded event handling, Pygame allows the program to interact with keyboard, mouse, or user input events, a special feature in interactive CVG applications, such as sliders, buttons, or live frame control.

🍂 **Lightweight and efficient**

Pygame is specialized for speed and performance in 2D graphics. The library can be especially handy for systems with limited hardware or when projects need smooth performance without performance lag.

🛠️ **Flexible and customizable**

Can easily overlay or overlay text, shapes, or other graphics on top of images and video frames, this produces an interesting and informative CVG output. It is also suitable for both basic visual output, such as image displays, and advanced GUIs or animated simulations.

# 1. OBJECT TRACKING USING PYGAME
- This project demonstrates a basic form of interactive object tracking using a single static image.

- When the image is displayed using Pygame, user can click anywhere on the image. The program captures the position of the mouse click and interprets it as a point of interest like simulating an object detection. Once the click is detected, the program automatically draws a green diamond shape around the clicked region. This visually indicates the area of interest or the “detected object.”

FULL CODE

<pre>
import pygame
import sys

# Initialize PyGame
pygame.init()

# Load image
image_path = r'C:\NASUHA\keta merah.jpg'  # Ganti dengan path gambar sebenar
original_image = pygame.image.load(image_path)
original_image = pygame.transform.scale(original_image, (800, 600))  # Resize kalau perlu

# Set window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple Object Tracker - CVG Project')

# Store all diamond positions
diamonds = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            diamonds.append(pos)  # Save position

    # Draw the image
    screen.blit(original_image, (0, 0))

    # Draw diamonds
    for pos in diamonds:
        x, y = pos
        diamond_points = [
            (x, y - 30),     # Top
            (x + 30, y),     # Right
            (x, y + 30),     # Bottom
            (x - 30, y)      # Left
        ]
        pygame.draw.polygon(screen, (0, 255, 0), diamond_points, 2)

    # Update the display
    pygame.display.update()

# Exit
pygame.quit()
sys.exit()
</pre>

The output

original    

<img src="https://github.com/user-attachments/assets/58b909c4-b307-4ebd-9582-b65f984b4ce2" width="400"/>  

result 

<img src="https://github.com/user-attachments/assets/1e09644d-93e8-482e-b9ff-0652d30deff8" width="400"/>


# 2. MOTION DETECTION

- This project is a simplified simulation of motion detection using a moving shape instead of real camera input.
  
- Although it is not detecting real-world motion, it simulates how motion can be tracked and visualized by updating the position of an object in each frame.

FULL CODE

<pre>
import pygame
import sys
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Motion Detection with Moving Image")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Load moving object image
image_path = r'C:\NASUHA\keta merah.jpg'  # Gantikan dengan path sebenar
object_img = pygame.image.load(image_path)
object_img = pygame.transform.scale(object_img, (100, 100))  # Resize jika perlu

# Starting position & speed
x = random.randint(0, WIDTH - 100)
y = random.randint(0, HEIGHT - 100)
speed_x = random.choice([-5, -4, -3, 3, 4, 5])
speed_y = random.choice([-5, -4, -3, 3, 4, 5])

# Previous position for motion detection
previous_pos = (x, y)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position
    x += speed_x
    y += speed_y

    # Bounce off edges
    if x <= 0 or x >= WIDTH - 100:
        speed_x *= -1
    if y <= 0 or y >= HEIGHT - 100:
        speed_y *= -1

    # Background
    screen.fill(WHITE)

    # Draw the image (moving object)
    screen.blit(object_img, (x, y))

    # Motion detection check
    if abs(x - previous_pos[0]) > 1 or abs(y - previous_pos[1]) > 1:
        text = font.render("Motion Detected!", True, BLUE)
        screen.blit(text, (20, 20))

    previous_pos = (x, y)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
 </pre>

The Output

![Screenshot 2025-05-01 175914](https://github.com/user-attachments/assets/d65b7695-eeb9-43af-b9bc-5b98c49dbaf7)


