from better_profanity import profanity
import re
from flask import Flask, render_template, redirect
from replit import web, db
app = Flask(__name__)
users = web.UserStore()

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")





app.run(host='0.0.0.0', port=81,debug=True)