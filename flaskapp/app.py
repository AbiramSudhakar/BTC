from flask import *
from datetime import datetime
import os
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/news")
def news():
    return render_template("index.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)