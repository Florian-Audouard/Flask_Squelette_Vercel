import os
from flask import Flask, jsonify, render_template


os.chdir(os.path.dirname(__file__))
from database.database import get_data


app = Flask(__name__)


@app.route("/")
def index():  # pylint: disable=missing-function-docstring
    return render_template("index.html")


@app.route("/getDatabase", methods=["GET"])
def get_database():  # pylint: disable=missing-function-docstring
    return jsonify(get_data())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
