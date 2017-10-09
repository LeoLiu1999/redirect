from flask import Flask, render_template, session, url_for, redirect, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

'''
hard-coded username/password
'''
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
        username=session["username"]
        return render_template("index.html",username=username)
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST","GET"])
def login():
    if "username" in session:
        return redirect(url_for("root"))
    usr_ok = False
    pwd_ok = False
    username = request.form.get("username")
    password = request.form.get("password")
    if username == usr:
        usr_ok = True
    if password == pwd:
        pwd_ok = True

    if (usr_ok and pwd_ok):
        session["username"] = username
        return redirect(url_for("welcome"))
    if usr_ok:
        return render_template("login.html",error="Wrong password. Please try again.")
    else:
        return render_template("login.html",error="Wrong username. Please try again.")

@app.route("/signout")
def signout():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
