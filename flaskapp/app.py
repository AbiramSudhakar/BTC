from urllib import request
from flask import *
from datetime import datetime
import os
import sqlite3

from graphviz import render

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/news")
def news():
    return render_template("index.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/wallet")
def wallet():
    return render_template("wallet.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/loginconf", methods=['POST'])
def loginconf():
    em=request.form['email']
    pw=request.form['password']
    myconn=sqlite3.connect("./database/user.db")
    mycur=myconn.cursor()

@app.route("/wallet")
def wallet():
    return render_template("wallet.html")


@app.route("/signupconf", methods=['POST'])
def signupconf():
    nm=request.form['name']
    em=request.form['email']
    dob=request.form['dob']
    pwd=request.form['password']
    myconn=sqlite3.connect('user.db')
    print("Suc")
    mycur=myconn.cursor()
    link="../static/assets/image/default.jpg"
    pic=mycur.execute('SELECT BulkColumn FROM Openrowset( Bulk "./static/assets/image/default.jpg", Single_Blob) as img')
    print("Imgsuccess")
    mycur.execute("INSERT INTO INV VALUES (:name,:dob,:email,:password,:pic)", {'name': nm, 'dob': dob, 'email': em, 'password': pwd, 'pic': 'pic'})
    print("success")
    myconn.commit()
    myconn.close()
    return render_template('signin.html')


if __name__ == "__main__":
    app.run(debug=True)