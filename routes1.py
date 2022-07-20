from flask import Flask, render_template, url_for, flash, redirect
from pytforms import RegistrationForm, LoginForm
from flask import app
posts = [
    {
    "author":"Stephen",
    "title":"Blog Post 1",
    "content":"First Post Content",
    "date_posted":"April 20th, 2020"
    },
    {
    "author":"Dapaah",
    "title":"Blog Post 2",
    "content":"Second Post Content",
    "date_posted":"April 22th, 2020"
    },
{
    "author":"Kobby",
    "title":"Blog Post 3",
    "content":"Third Post Content",
    "date_posted":"April 24th, 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():
    #     flash(f"Account created for {form.username.data}!", "success")
    #     return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.email.data == "admin@blog.com" and form.password.data == "password":
        flash(f"Account created for {form.email.data}!", "success")
        return redirect(url_for('home'))
    else:
        flash("Login Unsuccessuful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)