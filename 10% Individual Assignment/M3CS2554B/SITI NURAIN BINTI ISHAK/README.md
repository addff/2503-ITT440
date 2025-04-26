# SITI NURAIN BINTI ISHAK (2023436072)

## Image Processing Using Pygame in Python
## Introduction
This project demonstrates basic image processing operations using Pygame in Python. The operations include rotating, flipping, and resizing an image. Pygame's transform module makes it simple to manipulate images easily and efficiently.

## Technologies Used
- Python 3.10.11
- Pygame Library

## Installation
To run this project, you need to install Pygame first:
```
pip install pygame
```

## Code Overview
### Rotate an Image
```python
import pygame

# Initialize pygame
pygame.init()

# Load the image
image = pygame.image.load("example.jpg")  # Replace with your image filename

# Rotate the image (angle in degrees)
rotated_image = pygame.transform.rotate(image, 45)  # Rotate 45 degrees

# Save the rotated image
pygame.image.save(rotated_image, "rotated_image.jpg")

# Quit pygame
pygame.quit()

print("Image rotated and saved as 'rotated_image.jpg'")
```
**Explanation:** This code loads `cat.jpg`, rotates it by 45 degrees, and saves it as `rotated_image.jpg`.

### Flip an Image Horizontally
```python
import pygame
pygame.init()

image = pygame.image.load("cat.jpg")
flipped_image = pygame.transform.flip(image, True, False)
pygame.image.save(flipped_image, "flipped_image.jpg")

pygame.quit()
print("Image flipped and saved as 'flipped_image.jpg'")
```
**Explanation:** This code loads `cat.jpg`, flips it horizontally, and saves it as `flipped_image.jpg`.


### Resize an Image
```python
import pygame
pygame.init()

image = pygame.image.load("cat.jpg")
new_size = (300, 100)
resized_image = pygame.transform.scale(image, new_size)

pygame.image.save(resized_image, "resized_image.jpg")

pygame.quit()
```
**Explanation:** This code loads `cat.jpg`, resizes it to 300x100 pixels, and saves it as `resized_image.jpg`.

### Sample Output

![cat](https://github.com/user-attachments/assets/19335ebc-675d-4cf5-b298-c54b556a0c33)

`cat.jpg`

![rotated_image](https://github.com/user-attachments/assets/8b04b4bc-c213-4875-9bdb-7c800b6dda58)
`rotated_image.jpg`

![flipped_image](https://github.com/user-attachments/assets/b4016288-7ebb-40a3-ae01-4f7fda7ccb74)
`flipped_image.jpg`

![resized_image](https://github.com/user-attachments/assets/8ca96363-e39e-415d-a1b2-7a51cdb32049)
`resized_image.jpg`



### Conclusion
Using Pygame, basic image processing tasks like rotating, flipping, and resizing can be implemented easily with just a few lines of Python code. These operations provide a good foundation for more advanced image manipulation projects.


