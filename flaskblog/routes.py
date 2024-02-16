from flask import render_template, url_for, redirect, flash
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import Post
from flaskblog import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=Post.query.all())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect('/')
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Log in unsuccessful. Please check your credentials.", "danger")
    return render_template('login.html', title='Login', form=form)