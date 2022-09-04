from better_profanity import profanity
import re
from flask import Flask, render_template, redirect, request
from replit import web, db
app = Flask(__name__)
users = web.UserStore()

@app.route("/")
def login():
    if web.auth.name != "":
        return redirect("/home")
    else:
        return render_template("index.html")


@app.route("/home")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def home():
    if web.auth.name  not in db["names"]:
        db["names"].append(web.auth.name)
    return render_template("home.html", profile_pic=request.headers["X-Replit-User-Profile-Image"],name=request.headers["X-Replit-User-Name"])


@app.route("/maths")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def maths():
    return render_template("maths.html", profile_pic=request.headers["X-Replit-User-Profile-Image"],name=request.headers["X-Replit-User-Name"])

@app.route("/number")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def number():
    return render_template("number.html", profile_pic=request.headers["X-Replit-User-Profile-Image"],name=request.headers["X-Replit-User-Name"])

@app.route("/time")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def time():
    return render_template("time.html", profile_pic=request.headers["X-Replit-User-Profile-Image"],name=request.headers["X-Replit-User-Name"])

@app.route("/current")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def current():
    return render_template("current.html", profile_pic=request.headers["X-Replit-User-Profile-Image"],name=request.headers["X-Replit-User-Name"])

@app.route("/countdown-timer")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def countdown():
    return render_template("countdown.html", profile_pic=request.headers["X-Replit-User-Profile-Image"],name=request.headers["X-Replit-User-Name"])

@app.route("/write")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def write():
    return render_template("write.html", profile_pic=request.headers["X-Replit-User-Profile-Image"],name=request.headers["X-Replit-User-Name"])

    
app.run(host='0.0.0.0', port=81,debug=True)