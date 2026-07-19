import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================
# Load Dataset
# ==========================

dataset_path = "dataset/SMSSpamCollection"

data = pd.read_csv(
    dataset_path,
    sep="\t",
    names=["label", "message"]
)

# ==========================
# Convert Labels
# ham = 0
# spam = 1
# ==========================

data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

# ==========================
# Features & Labels
# ==========================

X = data["message"]
y = data["label"]

# ==========================
# TF-IDF
# ==========================

vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(X)

# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Multinomial Naive Bayes
# ==========================

model = MultinomialNB()

model.fit(X_train, y_train)

# ==========================
# Prediction
# ==========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("Accuracy :", round(accuracy * 100, 2), "%")
print("=" * 50)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# ==========================
# Save Model
# ==========================

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/spam_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\nModel Saved Successfully!")