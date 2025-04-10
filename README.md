# cotton_disease_prediction

# 🌿 AI Cotton Plant Disease Detector

The AI Cotton Plant Disease Detector is a terminal-based deep learning application that helps farmers and agricultural experts detect diseases in cotton plants just by analyzing images. It uses advanced language-vision models like Mistral and LLaMA to recognize disease patterns and suggest cures and preventive actions

---

## 🧠 How It Works
 - Image Input: The user provides the path to an image of a cotton plant (infected or healthy).
 - Processing: The image is preprocessed using tools like OpenCV or PIL.
 - Model Prediction: A trained AI model (using VGG-16) analyzes the image and predicts:
 - The type of disease (e.g., bacterial blight, leaf curl, etc.)
 - Suggested treatment or cure
 - Preventive measures to avoid recurrence
 - Output: The results are shown in the terminal for quick and easy interpretation.

## 🔍 Features
- 📷 Upload images of cotton plants to diagnose diseases
- 🧠 Disease detection using Mistral or LLaMA
- 💊 Suggests cures and preventive measures
- 🌐 Web-based UI built using Flask and HTML/CSS

---

## 🛠️ Tech Stack
- **Language Models**: Mistral, LLaMA
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Others**: OpenCV, PIL, NumPy, PyTorch or TensorFlow

---

## 📦 Setup Instructions

### 1. Clone the Repository
bash
git clone https://github.com/saiteja-lab/cotton_disease_prediction.git
cd cotton_disease_prediction

# Windows
python -m venv .venv
venv\Scripts\activate

# Linux / Macos
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


cotton_disease_prediction/
├── app.py
├── cottonModel/
│   └── Modelfile(You can create a custom model accordingly)

python app.py

Then open your browser and go to:
🌐 http://127.0.0.1:5000
