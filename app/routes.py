# define routes
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    # try call user's list
    user = {"username": "irfan shukri"}

    # fake post
    posts = [
        {"author": {"username": "John"}, "body": "test post1"},
        {"author": {"username": "Jane"}, "body": "test post2"},
        {"author": {"username": "Samad"}, "body": "test post3"},
        {"author": {"username": "irfan shukri"}, "body": "test post4"},
        {"author": {"username": "wok yoh"}, "body": "test post5"},
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        flash(
            f"Login requested for user {loginForm.username.data}, remember_me={loginForm.remember_me.data}"
        )

        return redirect(url_for("index"))

    return render_template("login.html", title="Login", form=loginForm)
