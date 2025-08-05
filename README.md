# Image Quality Reducer using PCA

A simple Flask web application that allows users to upload an image, reduce its quality using Principal Component Analysis (PCA), and download the compressed grayscale image.

This project demonstrates how dimensionality reduction techniques like PCA can be effectively applied to compress images by retaining specified percentage of information.



## Features

-  Upload `.jpg`, `.jpeg`, or `.png` images.
-  Choose quality level (1–100%) —> lower values = more compression.
-  PCA is applied to reduce image dimensionality.
-  Outputs grayscale compressed images.
-  Download the result instantly after compression.



## Tech Stack

- **Backend**: Python, Flask
- **Image Processing**: `matplotlib`, `numpy`, `scikit-learn (PCA)`
- **Frontend**: HTML5 + Bootstrap



## How It Works

1. The user uploads an image.
2. The red channel (or grayscale version) is extracted.
3. PCA reduces the number of components based on the selected quality level.
4. The inverse transform reconstructs the compressed version.
5. The output is saved and made available for download.


