# NAUFAL BIN MOHAMAD HAPISOL
# Import the imageio module
import imageio

# Reading an image
image = imageio.imread('example.jpg')  # Replace 'example.jpg' with your image file
print("Image shape:", image.shape)

# Writing an image
imageio.imwrite('output.jpg', image)  # This saves the image to 'output.jpg'

print("Image has been read and saved successfully.")
