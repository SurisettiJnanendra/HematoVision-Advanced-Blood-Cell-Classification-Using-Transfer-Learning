from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load your trained ResNet50-based model
model = tf.keras.models.load_model("bloodcell.h5")

# Class labels (adjust according to your training order if needed)
class_names = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']

# Preprocess image to match ResNet50 input
def preprocess_image(image):
    image = image.resize((224, 224))               # ResNet50 input size
    image = np.array(image) / 255.0                # Normalize pixel values
    image = np.expand_dims(image, axis=0)          # Shape: (1, 224, 224, 3)
    return image

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return render_template('result.html', class_label="No image uploaded", img_data="")

    file = request.files['image']
    image = Image.open(file.stream).convert("RGB")

    # Encode uploaded image for display in HTML
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_data = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Predict class
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    class_label = class_names[np.argmax(prediction)]

    return render_template('result.html', class_label=class_label, img_data=img_data)

if __name__ == "__main__":
    app.run(debug=True)
