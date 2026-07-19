from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

history = []

# Load trained model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html", history=history)


@app.route("/predict", methods=["POST"])
def predict():

    message = request.form["message"]

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        result = "🚫 Spam Message"
        color = "red"
    else:
        result = "✅ Not Spam"
        color = "green"

    # History save
    history.insert(0, {
        "message": message,
        "result": result,
        "confidence": confidence
    })

    # Sirf last 5 predictions rakhenge
    if len(history) > 5:
        history.pop()

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        message=message,
        color=color,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)