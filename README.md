# 📩 SMS Spam Detection

A machine learning-based web application that classifies SMS messages as **Spam** or **Ham (Not Spam)**. The project uses the **Multinomial Naive Bayes** algorithm with **TF-IDF Vectorization** and is built using **Python** and **Flask**.

---

## 📌 Features

- Detects Spam and Ham SMS messages
- User-friendly web interface
- Machine Learning model using Multinomial Naive Bayes
- TF-IDF text vectorization
- Displays prediction results with confidence score
- Stores recent prediction history

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
SMS-Spam-Detection/
│
├── app.py
├── train_model.py
├── requirements.txt
├── dataset/
│   └── SMSSpamCollection
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/amans92842-eng/SMS-Spam-Detection.git
```

### Go to project directory

```bash
cd SMS-Spam-Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

1. Load SMS dataset
2. Clean and preprocess text
3. Convert text into TF-IDF vectors
4. Train Multinomial Naive Bayes model
5. Save trained model using Joblib
6. Predict whether a message is Spam or Ham

---

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset** containing SMS messages labeled as:

- Spam
- Ham (Not Spam)

---

## 📷 Project Preview

You can add screenshots here after uploading them.

Example:

```
Home Page Screenshot

Prediction Result Screenshot
```

---

## 📈 Future Improvements

- Email Spam Detection
- Deep Learning (LSTM/BERT)
- User Authentication
- Database Integration
- REST API Support
- Real-time Message Classification

---

## 👨‍💻 Author

**Aman Singh**

B.Tech - Computer Science & Engineering

GitHub:
https://github.com/amans92842-eng

---

## 📄 License

This project is developed for educational purposes.
