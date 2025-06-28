# HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning

### Author: surisetti jnanendra

---

## 🧬 Overview

Hematovision is a deep learning-based web application that performs automated blood cell classification using transfer learning. It uses the dataset2-master dataset to classify blood cells into four categories:

- Neutrophil  
- Eosinophil  
- Monocyte  
- Lymphocyte  

This application allows users to upload microscopic blood smear images and returns the predicted blood cell type with high accuracy.

---

## 📁 Dataset: DATASET2-MASTER

The dataset2-master Dataset is a labeled dataset for blood cell classification, organized in Pascal VOC format. It is suitable for object detection and classification tasks.

- License: MIT

---

## 🧠 Model & Approach

- Utilizes transfer learning with pre-trained CNN models such as ResNet50, MobileNet, or EfficientNet.
- Trained on a labeled dataset of 12,500 microscopic blood cell images.
- Techniques used:  
  - Data augmentation  
  - Fine-tuning of pretrained layers  
  - Batch normalization and dropout  
- Produces fast and reliable predictions for real-world blood smear images.

---

## 🌐 Web App Workflow

The application is built using Flask, a lightweight Python web framework.

### 🔁 Workflow

1. User uploads a blood cell image.
2. The backend processes the image and passes it to the trained model.
3. The model returns the predicted class.
4. The result is displayed on the web interface.

---

## 🚀 Features

- Easy-to-use web interface
- Accurate classification of blood cell types
- Fast, real-time prediction
- Works with .jpg, .jpeg, .png images

---

## 🛠️ Tech Stack

- Language: Python  
- Framework: Flask  
- Deep Learning: TensorFlow / Keras or PyTorch  
- Frontend: HTML5, Bootstrap (optional)  
- Deployment: Localhost or Cloud Platforms (Render, Heroku, etc.)

---

## 📂 Folder Structure

hematovision/
├── dataset2-master
├── Static/
│ └── test/ # Stores uploaded images
├── templates/
│ └── home.html # Frontend HTML file
│ └── result.html
├── app.py # Flask application
├── bloodcell.h5 # Trained model file
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Demo video link

testing video: https://drive.google.com/file/d/15n4VIHr3H5CSVbHgNmd9nQUF2MovoRvf/view?usp=drive_link
jupyter notebook demo: https://drive.google.com/file/d/1h7wOH1rTygqQRkIihQ8vr9vH01kPUVMc/view?usp=drive_link
