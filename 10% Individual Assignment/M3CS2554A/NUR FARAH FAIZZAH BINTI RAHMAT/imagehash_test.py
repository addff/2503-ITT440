from PIL import Image
import imagehash

# Load the image
image = Image.open("image1.jpg")
pixels = image.load()  # Get access to the pixel data

# Get the size of the image
width, height = image.size

# === Modify the image by changing pixel values ===
for i in range(width):
    for j in range(height):
        # Get the current pixel value (RGB tuple)
        r, g, b = pixels[i, j]
        
        # Apply a simple transformation: invert colors (just for demonstration)
        inverted_pixel = (255 - r, 255 - g, 255 - b)
        
        # Set the new pixel value
        pixels[i, j] = inverted_pixel

# Save the edited image
image.save("image1_inverted_pixels.jpg")

# === Generate Hash after Editing ===
image_hash = imagehash.average_hash(image)
print("Hash after pixel inversion:", image_hash)

# Original image hash
original_hash = imagehash.average_hash(image)

# Apply pixel-level changes
# Invert colors (from the previous example)

# Recalculate the hash after modification
modified_hash = imagehash.average_hash(image)

# Compare hashes
if original_hash != modified_hash:
    print("The image has been modified!")
else:
    print("The image is unchanged.")


