from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"