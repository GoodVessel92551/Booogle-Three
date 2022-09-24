from better_profanity import profanity
import function as fun
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
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    users.current["pic"] = request.headers["X-Replit-User-Profile-Image"]
    if web.auth.name not in db["names"]:
        users.current["tasks"] = []
        users.current["id"] = 0
        users.current["time"] = ["0","10","0"]
        db["names"].append(web.auth.name)
    return render_template("home.html", profile_pic=users.current["pic"],name=web.auth.name)


@app.route("/maths")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def maths():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("maths.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/number")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def number():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("number.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/time")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def time():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("time.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/current")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def current():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("current.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/countdown-timer" , methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def countdown():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
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
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("write.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/stopwatch")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def stopwatch():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("stopwatch.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/tasks" , methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def tasks():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    if request.method == "POST":
        pass
    return render_template("tasks.html", profile_pic=users.current["pic"],name=web.auth.name, time=users.current["time"][0:], tasks=users.current["tasks"][0:])

@app.route("/games")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def games():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("games.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/play")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def play():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("play.html", profile_pic=users.current["pic"],name=web.auth.name,game=request.args.get("game"))

@app.route("/edit", methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def edit():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("edit.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/sw.js", methods=["GET"])
def sw():
    return current_app.send_static_file("sw.js")

@app.route('/delete')
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def delete():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    id = request.args.get("id")
    current_tasks = users.current["tasks"]
    for i in range(len(current_tasks)):
        if current_tasks[i] == int(id):
            current_tasks.pop(i)
            current_tasks.pop(i)
            current_tasks.pop(i)
            break
    if len(current_tasks)%3 == 0:
        users.current["tasks"] = current_tasks
        return redirect("/tasks")
    else:
        return "something went wrong"

@app.route('/edit_task' , methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def editit():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    if request.method == "POST":
        id = request.args.get("id")
        new_tasks = users.current["tasks"]
        title = profanity.censor(request.form["title"],censor_char="*").title()
        desc = profanity.censor(request.form["desc"],censor_char="*")
        if len(title) > 70 or len(desc) > 400 or len(title) == 0 or len(desc) == 0:
            return "You Title or Description is to long"
        for i in range(len(new_tasks)):
            if int(id) == new_tasks[i]:
                new_tasks[i+1] = title
                new_tasks[i+2] = desc
                break
        if len(new_tasks)%3 == 0:
            users.current["tasks"] = new_tasks
            return redirect("/tasks")
        else:
            return "something went wrong"
    else:
        current_tasks = users.current["tasks"]
        id = request.args.get("id")
        for i in range(len(current_tasks)):
            if current_tasks[i] == int(id):
                title2 = current_tasks[i+1]
                desc2 = current_tasks[i+2]
                return render_template("edit.html", profile_pic=users.current["pic"],name=web.auth.name,title=title2,desc=desc2)
        return redirect("/new")

@app.route('/new' , methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def new():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    if request.method == "POST":
        if len(users.current["tasks"])%3 > 20:
            return "You have reached your max amount of tasks remove some so you can make more."
        users.current["id"]=users.current["id"]+1
        new_tasks = users.current["tasks"]
        title = profanity.censor(request.form["title"],censor_char="*").title()
        desc = profanity.censor(request.form["desc"],censor_char="*")
        if len(title) > 70 or len(desc) > 400 or len(title) == 0 or len(desc) == 0:
            return "You Title or Description is to long or short"
        new_tasks.append(users.current["id"])
        new_tasks.append(title)
        new_tasks.append(desc)
        if len(new_tasks)%3 == 0:
            users.current["tasks"] = new_tasks
            return redirect("/tasks")
        else:
            return "something went wrong"
    return render_template("make.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/joinbeta", methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def joinbeta():
    if web.auth.name in db["join"]:
        return "Please wait till you request gets accepted"
    if request.method == "POST":
        join = db["join"]
        desc = profanity.censor(request.form["desc"],censor_char="*")
        name = web.auth.name
        if len(desc) > 400 or len(desc) < 0:
            return "desc is to long of short"
        join.append(name)
        join.append(desc)
        if len(join)%2 == 0:
            db["join"] = join
            return redirect("/joinbeta")
        else:
            return "something went wrong"
    return render_template("joinbeta.html", profile_pic=users.current["pic"],name=web.auth.name)

@app.route("/admin/beta" , methods=["POST", "GET"])
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def beta():
    if fun.admin(web.auth.name) != True:
        return redirect("/home")
    if request.method == "POST":
        db["beta"].append(request.form["name"])
    return render_template("beta.html", profile_pic=users.current["pic"],name=web.auth.name, tasks=db["join"][0:],names = db["beta"][0:])

@app.route("/settings")
@web.authenticated(login_res="<script>window.open('/','_self')</script>")
def settings():
    if fun.beta(web.auth.name) != True:
        return redirect("/joinbeta")
    return render_template("settings.html", profile_pic=users.current["pic"],name=web.auth.name)


app.run(host='0.0.0.0', port=81,debug=True) 