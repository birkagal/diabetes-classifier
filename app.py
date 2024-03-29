import src.classify
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    result = src.classify.classify(request.json)
    if result:
        return "Positive"
    else:
        return "Negative"


if __name__ == "__main__":
    app.run()