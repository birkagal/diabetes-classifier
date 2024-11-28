import flask

import src.classify


app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    result = src.classify.classify(flask.request.json)
    if result:
        return "Positive"
    else:
        return "Negative"


if __name__ == "__main__":
    app.run()
