from better_profanity import profanity
import re
from flask import Flask, render_template, redirect, request, current_app
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
    users.current["pic"] = request.headers["X-Replit-User-Profile-Image"]
    if web.auth.name not in db["names"]:
        print("hi")
        users.current["time"] = ["0","10","0"]
        users.current["time"]
        db["names"].append(web.auth.name)
    return render_template("home.html", profile_pic=users.current["pic"],name=web.auth.name)


@app.route("/maths")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def maths():
    return render_template("maths.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/number")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def number():
    return render_template("number.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/time")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def time():
    return render_template("time.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/current")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def current():
    return render_template("current.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/countdown-timer" , methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def countdown():
    if request.method == "POST":
        hours = request.form["hours"]
        min = request.form["min"]
        sec = request.form["sec"]
        try:
            int(hours+min+sec)
        except:
            return "Enter a Number"
        else:
            if int(hours) > 24 or int(min) > 60 or int(sec) > 60:
                return "Number is to big"
            elif int(hours) < 0 or int(min) < 0 or int(sec) < 0:
                return "Number to small"
            users.current["time"] = [hours,min,sec]
    return render_template("countdown.html", profile_pic=users.current["pic"],name=web.auth.name, time=users.current["time"][0:])

@app.route("/write")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def write():
    return render_template("write.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/stopwatch")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def stopwatch():
    return render_template("stopwatch.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/tasks" , methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def tasks():
    if request.method == "POST":
        pass
    tasks = ["task1","this is task1","1","task2","this is task2","2"]
    return render_template("tasks.html", profile_pic=users.current["pic"],name=web.auth.name, time=users.current["time"][0:], tasks=tasks)

@app.route("/games")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def games():
    return render_template("games.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/play")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def play():
    return render_template("play.html", profile_pic=users.current["pic"],name=web.auth.name,game=request.args.get("game"))

@app.route("/edit", methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def edit():
    return render_template("edit.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/sw.js", methods=["GET"])
def sw():
    return current_app.send_static_file("sw.js")

app.run(host='0.0.0.0', port=81,debug=True)