# app.py

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(
    open("model/spam_model.pkl","rb")
)

vectorizer = pickle.load(
    open("model/vectorizer.pkl","rb")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    email = request.form["email"]

    transformed = vectorizer.transform([email])

    prediction = model.predict(transformed)

    result = "Spam Email" if prediction[0] == 1 else "Not Spam"

    return render_template(
        "index.html",
        prediction_text=result
    )

if __name__ == "__main__":
    app.run(debug=True)