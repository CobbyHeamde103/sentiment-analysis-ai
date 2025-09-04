# 🧠 Sentiment Analysis AI (Transformers + Python)

An AI project that uses Hugging Face Transformers to perform **sentiment analysis** on text.  

---

## 🚀 Features
- Classifies text as **Positive / Negative / Neutral**
- Uses pre-trained Hugging Face model
- Lightweight and easy to run locally

---

## 🛠️ Installation

```bash
# Clone this repository
git clone https://github.com/CobbyHeamde103//sentiment-analysis-ai.git
cd sentiment-analysis-ai

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python sentiment_analysis.py
```

Example output:

```
Text: I love my new MacBook, it's blazing fast!
Prediction: POSITIVE (Confidence: 0.99)

Text: The weather is terrible today.
Prediction: NEGATIVE (Confidence: 0.98)

Text: I feel okay, not too bad, not too good.
Prediction: NEUTRAL (Confidence: 0.85)
```

---

## 📒 Jupyter Notebook
You can also run the example notebook:

```bash
jupyter notebook examples.ipynb
```

---

## 🤝 Contributing
Pull requests are welcome! Feel free to fork and add new features like:
- Web app (Streamlit/Flask)
- Dataset-based training
- Visualization of results

---

## 📜 License
MIT License
