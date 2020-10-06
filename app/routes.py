# define routes
from flask import render_template
from app import app


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
