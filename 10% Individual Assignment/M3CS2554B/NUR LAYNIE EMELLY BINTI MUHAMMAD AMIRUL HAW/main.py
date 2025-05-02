import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# ========== 1. Checkerboard Pattern ==========
def generate_checkerboard(size=8, block_size=50):
    pattern = np.zeros((size * block_size, size * block_size, 3), dtype=np.uint8)
    for i in range(size):
        for j in range(size):
            color = [255, 255, 0] if (i + j) % 2 == 0 else [0, 128, 255]
            pattern[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size] = color
    return pattern

checkerboard = generate_checkerboard()
plt.imshow(checkerboard)
plt.title("Checkerboard Pattern")
plt.axis("off")
plt.savefig("../outputs/checkerboard.png")
plt.show()
plt.close()

# ========== 2. Grayscale Image ==========
try:
    img = imageio.imread("sample.jpg")
except FileNotFoundError:
    print("⚠️ 'sample.jpg' not found. Please make sure it is inside the 'code' folder.")
    exit()

gray = np.mean(img, axis=2).astype(np.uint8)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.savefig("../outputs/grayscale.png")
plt.show()
plt.close()

# ========== 3. Blue Tint Filter ==========
blue_tinted = img.copy()
blue_tinted[:, :, 2] = np.clip(blue_tinted[:, :, 2] + 100, 0, 255)
plt.imshow(blue_tinted)
plt.title("Blue Tint Applied")
plt.axis("off")
plt.savefig("../outputs/blue_tint.png")
plt.show()
plt.close()

# ========== 4. Brightness Enhancement ==========
brighter = np.clip(img + 50, 0, 255).astype(np.uint8)
plt.imshow(brighter)
plt.title("Brightened Image")
plt.axis("off")
plt.savefig("../outputs/brightened.png")
plt.show()
plt.close()

# ========== 5. Black Area Detection ==========
img2 = imageio.imread("sample.jpg")  # Reload original image
r = img2[:, :, 0]
g = img2[:, :, 1]
b = img2[:, :, 2]

# Detect black: All color channels are low
mask = (r < 60) & (g < 60) & (b < 60)

# Highlight detected black areas in bright green
overlay = img2.copy()
overlay[mask] = [0, 255, 0]  

plt.imshow(overlay)
plt.title("Detected Black Areas in Image")
plt.axis("off")
plt.savefig("../outputs/black_detection.png")
plt.show()
plt.close()

