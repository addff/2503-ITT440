# Image Processing Using MMDetection

**NAME:** Nurul Aisyah binti Ayob  
**MATRIC NUMBER:** 2023239322  
**GROUP:** M3CS2554B  

---

## 📚 **LIBRARY**  
### **MMDetection**  
#### **What is MMDetection?**  
MMDetection is an open-source object detection toolbox based on **PyTorch**, developed by the **OpenMMLab** team. It provides a wide range of pre-trained models for object detection, instance segmentation, and panoptic segmentation. MMDetection supports popular architectures like **Faster R-CNN, Mask R-CNN, YOLOv3, RetinaNet, and more**, making it a powerful tool for computer vision tasks.  

#### **Significance**  
- **State-of-the-art Models:** MMDetection includes high-performance models for object detection.  
- **Modular Design:** Easy to customize and extend for different use cases.  
- **High Efficiency:** Optimized for both training and inference.  
- **Multi-task Support:** Supports detection, segmentation, and even pose estimation.  
- **Large Community & Documentation:** Well-documented with active development.  

---

## ⚙️ **Installation and Setup**  

### **1. Install PyTorch**  
MMDetection requires PyTorch. Install it based on your system:  

#### **For CUDA (GPU) Support:**  
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
For CPU-only:
bash
pip install torch torchvision torchaudio
2. Install MMDetection
bash
pip install openmim
mim install mmengine
mim install mmcv-full
mim install mmdet
3. Verify Installation
python
import mmdet
print(mmdet.__version__)
If no errors, installation is successful.

▶️ Video Tutorial
Learn how to use MMDetection with this video tutorial:
Watch on YouTube (Replace with your video link)

🧪 Python Code (Object Detection)
Code Example: Object Detection with Pre-trained Model
python
from mmdet.apis import init_detector, inference_detector
import mmcv

# Config and checkpoint files
config_file = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

# Initialize the detector
model = init_detector(config_file, checkpoint_file, device='cuda:0')  # or 'cpu'

# Perform inference on an image
img = 'demo/demo.jpg'
result = inference_detector(model, img)

# Visualize the results
out_img = 'output.jpg'
model.show_result(img, result, out_file=out_img)
print(f"Detection results saved to {out_img}")
Explanation
init_detector → Loads a pre-trained model (Faster R-CNN in this case).

inference_detector → Runs object detection on an input image.

show_result → Draws bounding boxes and saves the output.

(Download the config and checkpoint from MMDetection Model Zoo)

✅ Output Description
output.jpg → Image with detected objects highlighted with bounding boxes.

Supported Classes: COCO dataset classes (e.g., person, car, dog, etc.).

GitHub Repository
Find the full code and documentation here:
GitHub Link (Replace with your repo link)

Conclusion
MMDetection is a powerful library for object detection tasks, offering flexibility and high performance. By leveraging pre-trained models, developers can quickly implement advanced computer vision applications.
