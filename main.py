import os
from flask import Flask, render_template, request
import calendar

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    number = request.form["number"]
    roman = calendar.number_to_roman(number)
    return render_template("convert.html", number=number, roman=roman)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
