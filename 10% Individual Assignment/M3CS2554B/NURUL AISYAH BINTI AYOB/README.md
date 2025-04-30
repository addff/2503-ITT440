# Object Detection using MMDetection: A Python Approach

## Introduction

Computer Vision, Graphics, and Image Processing (CVG & IP) are essential fields in AI. One of the most powerful applications is **Object Detection**, which allows a system to identify and locate objects in images or video streams.

In this project, we explore **MMDetection**, an open-source toolbox based on PyTorch, developed by OpenMMLab for object detection and instance segmentation.

---

## What is MMDetection?

MMDetection is a part of the OpenMMLab project and supports a wide range of detection algorithms like Faster R-CNN, RetinaNet, YOLO, and more.

**Features:**
- Modular and flexible design
- Supports multiple backbones (ResNet, Swin, etc.)
- Pretrained models on COCO and other datasets

---

## Why MMDetection?

- Easy-to-use APIs for inference
- Highly configurable
- Well-documented and active community

---

## Installation & Setup

### 1. Clone MMDetection
```bash
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
```

### 2. Install dependencies
```bash
pip install -r requirements/build.txt
pip install -v -e .  # or "python setup.py develop"
```

> 💡 Tip: Use a virtual environment (e.g., conda or venv) for clean setup.

---

## Running Object Detection

We use a pretrained **Faster R-CNN** model on the COCO dataset to detect objects in an image.

### 1. Download a test image
Place your image in the `assets/` folder and rename it `input.jpg`.

### 2. Run the detection script
```bash
python detect_image.py
```

This will create `assets/output.jpg` with bounding boxes.

---

## Output Example

### Input:
![Input](assets/input.jpg)

### Output:
![Output](assets/output.jpg)

---

## Video Demonstration

A full demo video of running MMDetection and explaining the code is available on YouTube:

🔗 [Watch the demo video here](https://youtube.com/your-demo-link)

---

## Conclusion

This assignment demonstrates how MMDetection can be used with Python to perform state-of-the-art object detection. With just a few lines of code and access to pretrained models, anyone can experiment with real-world image processing tasks.

---

## References

- [MMDetection GitHub](https://github.com/open-mmlab/mmdetection)
- [OpenMMLab Docs](https://openmmlab.com/)

