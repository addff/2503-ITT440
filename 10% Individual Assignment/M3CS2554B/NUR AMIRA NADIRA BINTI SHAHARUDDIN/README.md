# NUR AMIRA NADIRA BINTI SHAHARUDDIN (2023414868)

## Image Processing Using imageio in Python

![imageio](https://github.com/user-attachments/assets/a1c72c2e-0029-4b51-84da-8877780655ec)

## Introduction
This project demonstrates basic image processing operations using imageIO in Python. The operations include reading, resized and grayscale  an image. imageIO with help with other library can transform module makes it simple to manipulate images easily and efficiently and differently. Image processing is a technique used to perform operations on digital images to enhance, analyze, or extract useful information from them. It involves manipulating image data using algorithms to perform tasks such as resizing, filtering, rotating, converting to grayscale, and more. Image processing is widely used in fields like computer vision, medical imaging, photography, remote sensing, and artificial intelligence. By using programming languages like Python along with libraries such as ImageIO, Pillow, and OpenCV, image processing becomes an accessible and powerful tool for solving real-world problems involving visual data.

## Technologies Used
- Python 3.10.11
- imageio Library

  ## What imageio can do?
✅ Read images from files or URLs into NumPy arrays

✅ Write or save images to various formats like JPG, PNG, GIF, BMP, TIFF

✅ Read and write animated images for example animated GIF

✅ Read and write videos

✅ Support a wide range of file formats

✅ Integrate with other libraries like NumPy, Pillow, and OpenCV for advanced processing

✅ Perform image I/O for scientific computing, visualization, and machine learning

## Installation
To run this project, you need to install imageIO first and other libraries that you need:

pip install imageIO
## Code Overview

# Read an Image

```### Import the imageio library
import imageio.v2 as imageio  # Use v2 to avoid deprecation warnings

### Define the path to the input image
image_path = 'C:/Users/USER/Downloads/picture.jpg'  # Input image file path

### Read the image from the given path
img = imageio.imread(image_path)  # Read the image into a NumPy array

### Define the output path where the image will be saved
output_path = 'new_image.jpg'  # Output image file name

### Save the image to the new location
imageio.imwrite(output_path, img)  # Write the image to the new file

### Print confirmation message
print(f"Image successfully read from '{image_path}' and saved as '{output_path}'")
```
*Explanation:* This code read picture.jpg in other file saves it as new_image.jpg in diffython

# Resized an Image

``` python
from PIL import Image
import imageio.v2 as imageio

### Read the image using imageio
image = imageio.imread('C:/Users/USER/Downloads/picture.jpg')

### Convert the image to a PIL Image for resizing
pil_image = Image.fromarray(image)  # Make sure this is done before resizing

### Resize the image (you can adjust the dimensions as needed)
resized_image = pil_image.resize((13, 55))  # Set the new dimensions (13, 55)

### Save or display the resized image
resized_image.save('resized_picture.jpg')
resized_image.show()

### Print new dimensions
print(f"New dimensions: {resized_image.size[0]}x{resized_image.size[1]}")
```

*Explanation:* This code are use to resized by using picture.jpg and save as resized_image.jpg.

# Grayscale an Image
```import imageio.v2 as imageio
from PIL import Image

### Read the image in RGB (default behavior of imageio)
image = imageio.imread('C:/Users/USER/Downloads/picture.jpg')

### Convert the image to grayscale using the luminosity method
### This will convert the image to 2D (grayscale)
grayscale_image = image[:, :, :3].dot([0.2989, 0.5870, 0.1140])

### Convert the grayscale image to an 8-bit image (uint8)
grayscale_image = (grayscale_image * 255).astype('uint8')

### Convert the numpy array to a PIL Image object
pil_image = Image.fromarray(grayscale_image)

### Save the grayscale image with the same original size
pil_image.save('grayscale_picture.jpg')
pil_image.show()

### Print original dimensions
print(f"Original dimensions: {pil_image.size[0]}x{pil_image.size[1]}")
```

*Explanation:* This code are use to grayscale image by using picture.jpg. A grayscale image is an image that contains only shades of gray and have no color. Each pixel in the image represents intensity ranging from black (0) to white (255) in 8-bit images.

# Download an image using link 
```import requests
import imageio.v2 as imageio
from io import BytesIO

# Image URL
url = 'https://example.com/sample.jpg'  # 

### Send HTTP GET request to fetch the image
response = requests.get(url)

### Ensure the request was successful
if response.status_code == 200:
    ### Wrap the byte content in a BytesIO object
    image_bytes = BytesIO(response.content)

    ### Read the image using imageio
    img = imageio.imread(image_bytes)

    ### Save the image to a file
    imageio.imwrite('downloaded_image.jpg', img)

    print("Image successfully downloaded and saved as 'downloaded_image.jpg'")
else:
    print("Failed to download image. Status code:", response.status_code)
```
*Explanation:* This code are use to download an image from URL and downloaded it into folder. Access an image from the internet using its URL

### Sample Output

```read new_image.jpg```
![new_image](https://github.com/user-attachments/assets/cd5329e7-fecc-4bee-9b20-b08671758e7c) 

```grayscale_picture.jpg```
![grayscale_picture](https://github.com/user-attachments/assets/96b9fbf0-4ba8-46af-b9e5-b79f6c80e440)

```resized_picture.jpg```
![resized_picture](https://github.com/user-attachments/assets/5f0400a5-f73b-4bf5-a56e-746d7e3e7a44)

```downloaded_picture.jpg(URL)```
![downloaded_image](https://github.com/user-attachments/assets/a78320e5-cd7e-430b-bb48-7ab860c4d3e2)

### Conclusion
In conclusion by using imageio library, I was able to efficiently perform image processing in Python by reading an image to access its pixel data, converting it to grayscale to simplify visual information, resizing it to adjust dimensions, and downloading an image from a URL to use external resources—all with simple and effective code.

### youtube link video:
https://youtu.be/5-1sVW0yAwQ?feature=shared
