# NUR SHAHIRAH BINTI BAHARUDDIN
## STUDENT ID: 2023698756
### ITT440 INDIVIDUAL ASSIGNMENT
# IMAGE PROCESSING WITH ALBUMENTATION
![image](https://github.com/user-attachments/assets/633600ff-ce45-41ab-96b2-ffdc53422e5a)


#### Image processing is a critical step in building robust computer vision models. It involves operations like resizing, cropping, rotating, adjusting brightness, adding noise and many other transformations to make the model more accurate and generalizable. Albumentations is a powerful, flexibale and fast open-source Python library for image augmentation. It was specifically designed to improve the performance of deep learning models for computer vision tasks such as classification, object detection and segementation.

## Advantages of Using Albumentations
* High Performance: Albumentations is optimized for speed, enabling it to process even complex augmentation pipelines efficiently.

* Versatile Transformations: It offers a broad selection of operations, including geometric changes, color modifications, noise addition, blur effects, and more.

* User-Friendly: With its clear and intuitive syntax, building augmentation pipelines becomes fast and straightforward.

* Feature-Rich: It provides specialized transformations designed for advanced tasks like semantic segmentation and object detection involving bounding boxes.

* Broad Compatibility: Albumentations integrates smoothly with leading deep learning frameworks such as PyTorch, TensorFlow, Keras, and tools like OpenCV.
  
### STEP BY STEP HOW TO IMPLEMENT.
Step 1 : Install the required libraries in the Command Prompt
 pip install albumentations opencv-python matplotlib
 
``` 
pip install albumentations opencv-python matplotlib
```
Step 2 : Prepare your image
* Download any cat photo (example)
* Save it as ```cat.jpg```
* Put in a folder (example: ```C:/Users/YourName/Desktop/cat_project/```)
  
Step 3 : Create a Python file ```cat_rotate.py```

Step 4 : Step-by-Step Code for Rotate Image

```
import cv2
import albumentations as A
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('cat.jpg')  # Replace with your image name
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Define rotation transformation
transform = A.Compose([
    A.Rotate(limit=90, p=1.0)  # Rotate between -90 and +90 degrees, always apply (p=1.0)
])

# Step 3: Apply rotation
augmented = transform(image=image)
rotated_image = augmented['image']

# Step 4: Show original and rotated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Cat')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Rotated Cat')
plt.imshow(rotated_image)
plt.axis('off')

plt.show()

# Step 5: Save the rotated image
rotated_bgr = cv2.cvtColor(rotated_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('rotated_cat.jpg', rotated_bgr)
```
#### RESULT :
![image](https://github.com/user-attachments/assets/84a93575-3573-45b4-a3aa-66849b98343b)  

### BLACK AND WHITE IMAGE
Step 1 : Create a new Python file ```cat_blackwhite.py``` 

Step 2 : Step-by-Step Code for Black and White Image
```
import cv2
import matplotlib.pyplot as plt

# Step 1: Load the color image
image = cv2.imread('cat.jpg')  # Make sure your image is in the same folder

# Step 2: Convert to grayscale (black and white)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Show original and grayscale images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Cat')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Black & White Cat')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.show()

# Step 4: Save the black and white image
cv2.imwrite('cat_blackwhite.jpg', gray_image)
```
#### RESULT :
![image](https://github.com/user-attachments/assets/14362ede-ac03-4d4d-b868-7a7765975e29)

### RESIZE IMAGE 
Step 1 : Create a new Python file ```cat_resize.py``` 
Step 2 : Step-by-Step Code for Resize Image
```
import cv2
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('cat.jpg')  # Make sure your cat.jpg is in the same folder

# Step 2: Resize the image
# New size: 200 pixels wide, 200 pixels tall
resized_image = cv2.resize(image, (200, 200))

# Step 3: Show original and resized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Cat')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Resized Cat (200x200)')
resized_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
plt.imshow(resized_rgb)
plt.axis('off')

plt.show()

# Step 4: Save the resized image
cv2.imwrite('cat_resized.jpg', resized_image)
print("✅ Resized image saved as 'cat_resized.jpg'!")
```
#### RESULT :
![image](https://github.com/user-attachments/assets/5627f906-ea0b-4c83-9655-42b566bb3907)

### COLOUR CHANGE IMAGE
Step 1 : Create a new Python file ```cat_colorchange.py``` 

Step 2 : Step-by-Step Code for Colour Change Image 
```
import cv2
import matplotlib.pyplot as plt

# Step 1: Load the original image
image = cv2.imread('cat.jpg')  # Make sure cat.jpg is in the same folder

# Step 2: Convert color — from BGR to RGB (normal color)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 3: Convert color — make it a different color map (example: apply COLORMAP_JET)
colored_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)

# Step 4: Show original and color-changed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Cat')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Color Changed Cat')
colored_rgb = cv2.cvtColor(colored_image, cv2.COLOR_BGR2RGB)
plt.imshow(colored_rgb)
plt.axis('off')

plt.show()

# Step 5: Save the color-changed image
cv2.imwrite('cat_colored.jpg', colored_image)
print("✅ Color-changed image saved as 'cat_colored.jpg'!")
```
#### RESULT :
![image](https://github.com/user-attachments/assets/9555bad9-2bb6-4663-912c-57c99f616baf)



