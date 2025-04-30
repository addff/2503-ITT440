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

# ========== 2. Diagonal Line Pattern ==========
lines = np.zeros((300, 300), dtype=np.uint8)
for i in range(300):
    lines[i, i] = 255
    lines[i, 299 - i] = 255
plt.imshow(lines, cmap='gray')
plt.title("Diagonal Line Pattern")
plt.axis("off")
plt.savefig("../outputs/diagonal_lines.png")
plt.show()
plt.close()

# ========== 3. Grayscale Conversion ==========
try:
    img = imageio.imread("sample.jpg")
except FileNotFoundError:
    print("⚠️ 'sample.jpg' not found. Put it in the same folder as main.py.")
    exit()

gray = np.mean(img, axis=2).astype(np.uint8)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.savefig("../outputs/grayscale.png")
plt.show()
plt.close()

# ========== 4. Blue Tint Filter ==========
blue_tinted = img.copy()
blue_tinted[:, :, 2] = np.clip(blue_tinted[:, :, 2] + 100, 0, 255)
plt.imshow(blue_tinted)
plt.title("Blue Tint Applied")
plt.axis("off")
plt.savefig("../outputs/blue_tint.png")
plt.show()
plt.close()

# ========== 5. Brightness Enhancement ==========
brighter = np.clip(img + 50, 0, 255).astype(np.uint8)
plt.imshow(brighter)
plt.title("Brightened Image")
plt.axis("off")
plt.savefig("../outputs/brightened.png")
plt.show()
plt.close()
