NAME : MUHAMMAD FARIDZ BIN ROSLI

STUDENT ID : 2023276918

CLASS : CDCS2554A

### TITLE : INTRODUCTION TO IMAGE PROCESSING USING CUDA IN PYTHON TOOLS

## What is Image Processing ?

The process of modifying and evaluating digital images to improve their quality, extract useful information, or get them ready for additional analysis is known as image processing in Python tools.  To carry out a variety of tasks like filtering, edge detection, segmentation, noise reduction, and feature extraction, this field integrates methods from computer science, mathematics, and engineering.  To manipulate images at the pixel level or in larger structures, developers and researchers can easily apply complex algorithms with the help of robust Python libraries like OpenCV, scikit-image, Pillow, and SciPy.  With the use of techniques like thresholding, blurring, and morphological operations, these tools enable the conversion, resizing, enhancement, or transformation of images. Image processing is a crucial ability in contemporary data-driven applications since it is used extensively in fields like computer vision, robotics, machine learning, security, and medical imaging.  Both novices and experts can now process images more easily and effectively thanks to Python's ease of use and the abundance of open-source libraries.

## What is CUDA ?

[![CUDA Logo](https://upload.wikimedia.org/wikipedia/commons/b/b9/Nvidia_CUDA_Logo.jpg)](https://en.wikipedia.org/wiki/CUDA)

CUDA is a tools in Python language.

NVIDIA created the parallel computing platform and programming model known as CUDA (Compute Unified Device Architecture), which enables programmers to use the enormous processing power of NVIDIA GPUs (Graphics Processing Units) for general-purpose computing tasks other than graphics rendering.  CUDA significantly accelerates compute-intensive applications like medical imaging, scientific simulations, image and video processing, artificial intelligence, and financial modeling by allowing thousands of lightweight threads to operate concurrently.  GPUs optimized with CUDA can execute operations in massive parallel, which makes them perfect for tasks involving large datasets and real-time performance, in contrast to CPUs, which process tasks sequentially with a limited number of cores. With the aid of tools like Numba or PyCUDA, developers can create CUDA programs in C, C++, Fortran, or Python that use sophisticated memory control and customized GPU kernels to carry out high-performance calculations.  Consequently, CUDA has emerged as a key instrument for speeding up workloads related to next-generation computing, real-time analytics, and data-driven research.

## The main features of CUDA are:

- Custom CUDA kernels for GPU-accelerated image processing, such as morphological operations, Gaussian blur, and Sobel edge detection.

- High-performance image operations using parallel 1D, 2D, and multi-dimensional calculations

- Effective memory management with shared, constant, and global memory

- Capacity to execute massive parallelization, which allows large image datasets to be processed more quickly

- Both float32 and float64 precision are natively supported.

- Real-time image transformation and filtering support

- Through numba.cuda.to_device(), it functions flawlessly with GPU memory and NumPy arrays (on the host).

## Library related to CUDA ?
While CUDA Python (via Numba) is powerful on it's own, it is often used alongside:

- NumPy – Array manipulation on the host side prior to and following GPU computation.
- scikit-image – Preprocessing, grayscale conversion, and image loading.
- Matplotlib – Display of both processed and original images
- OpenCV (cv2) –  Sophisticated image pre/post processing, filtering, and input/output.

From loading and prepping images to GPU-accelerated computation and visual output, these tools offer a comprehensive image processing workflow.

## Module / Subpackage in CUDA

- @cuda.jit – To compile a Python function as a CUDA GPU kernel, it must be decorated.
- cuda.grid() / cuda.threadIdx – Used to determine thread-by-thread parallel execution positions.
- cuda.to_device() – NumPy arrays are transferred to the GPU.
- cuda.device_array() – Memory allocation on the GPU.
- Custom GPU kernels	 – Used to apply filters (such as Gaussian, Dilation, Sobel, etc.)

With the help of these tools, one can create custom GPU-based image processing logic that runs in parallel and offers notable performance benefits over CPU-only processing.
