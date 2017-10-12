# Shakil Rafi and Leo Liu
# SoftDev pd7
# HW08 -- redirect
# 2017-10-09

from flask import Flask, render_template, session, url_for, redirect, request, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

# hard-coded username/password
usr="TakingTheL"
pwd="srafi1"

@app.route("/")
def root():
    if "username" in session:
        return redirect(url_for("welcome"))
    else:
        return redirect(url_for("login"))

@app.route("/welcome")
def welcome():
    if "username" in session:
        username = session["username"]
        return render_template("index.html", username=username)
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST","GET"])
def login():
    if "username" in session:
        return redirect(url_for("root"))
    username = request.form.get("username")
    password = request.form.get("password")
    authenticated, msg = authenticate(username, password)
    if authenticated:
        session["username"] = username
        return redirect(url_for("root"))
    else:
        flash(msg)
        return render_template("login.html")

def authenticate(user, passwd):
    print "authenticating user: %s passwd: %s" % (user, passwd)
    if user == "" and passwd == "":
        return False, ""
    if user == "":
        return False, "Enter your username"
    if passwd == "":
        return False, "Enter your password"
    if user != usr:
        return False, "That user is not registered"
    if passwd != pwd:
        return False, "Wrong password"
    return True, ""

@app.route("/signout")
def signout():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
