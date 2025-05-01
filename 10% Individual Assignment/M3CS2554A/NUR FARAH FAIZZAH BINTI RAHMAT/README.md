## 2503 - ITT440
## NAME : NUR FARAH FAIZZAH BINTI RAHMAT
## STUDENT ID : 2023213584 
## TITTLE : CVG & IMAGE PROCESSING USING PYTHON
### OBJECTIVES : 
* To acquire proficiency in utilizing Python libraries, particularly imagehash, for the analysis and processing of digital images
* To implement hashing techniques for the purpose of evaluating visual similarities and differences between digital image
* To develop the ability to intepret and analyze image hash outputs to assess the degree of similarity between images
### IMAGE PROCESSING 
Image processing refers to the techniques of converting an image into its digital representation and applying various operations tp extract meaningful information from it. Typically, an image processing system interprets iamges as two-dimensional signals and utilizes predefined signal processing methods to analyze and manipulate the image data
### IMAGEHASH
<img src="logo.png" alt="logo" width="300">

Image hashing is the computational process of applying an algorithm to genarate unique hash value that represents the content of an image. Identical copies of the image produce the same hash value, thereby enabling consistent identification. Consequently, image hashing is often referred to as a "digital fingerprint" due to its ability to uniquely characterized visual data.
### TYPE OF IMAGE HASHING ALGORITHMS
* Average Hash (aHash)
  Reduces an image to grayscale and computers a binary hash based on whether each pixel's intensity is above or below the mean
* Perceptual Hash (pHash)
  Uses the Discrete Cosine Transform (DCT) to analyze the image in the frequency domain, focusing on low-frequency components to capture overall structure.
* Difference Hash (dHash)
  Calculates the gradient of pixel insities by comparing adjacent pixels horizontally or vertically.
* Wavelet Hash (wHash)
  Applies a wavelet transform to extract low-frequency coefficients that represent perceptual features.
### ADVANTAGES OF USING IMAGEHASH
* The imagehash library enables rapid and computationally efficient image comparison by transforming images into compact hash representations, thus eliminating the need for exhaustive pixel-level analysis.
* Image hashing techniques employed within imagehash exhibit resilience to subtle changes such as resizing, cropping, compression or minor color adjustments, thereby ensuring reliable similarity detection under various image transfromations.
* By generating consistent hash values for identical or nearly images, imagehash simplifies the process of identifying duplicate or near-duplicate content across extensive image datasets.
* The library provides an accessible and user-friendly interface, facilitating the integration of image hashing functionalities into Python-based applications with minimal complexity.
* Imagehash supports a range of hashing algorithms including Average Hash (wHash) by providing adaptability to diverse application requirements.
* Owing to its lightweight nature, imagehash is well-suited for deployment in both small-scale and large-scale environments without significant computational burdens.
* Designed to operate alongside widely adopted libraries such as Pillow (PIL), imagehash benefits from broad compatibiity, enhancing its applicability whithin comprehensive computer vision and image processing workflows.
### A Practical Example for Image Comparison
![My Image](https://github.com/addff/2503-ITT440/blob/main/10%25%20Individual%20Assignment/M3CS2554A/NUR%20FARAH%20FAIZZAH%20BINTI%20RAHMAT%EF%80%8D/image3.jpg)
