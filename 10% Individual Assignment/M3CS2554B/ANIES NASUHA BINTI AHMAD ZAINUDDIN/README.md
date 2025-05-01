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

🧠 Easy to learn and use
    
    Pygame has a simple and beginner friendly syntax, making it accessible even for students who are new to graphics programming or Python

⚙️ Minimal setup

    Installation is straightforward with a single pip install pygame command and also there are no complex configurations or external 
    dependencies needed 
