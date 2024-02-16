from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '731f60039c617522880b1aaeda012b05'

posts = [
    {
        'author': 'John Doe',
        'title': 'Introduction to Python',
        'content': 'This post covers the basics of Python programming language.',
        'date_posted': 'January 1, 2022',
    },
    {
        'author': 'Jane Smith',
        'title': 'Getting Started with Flask',
        'content': 'Learn how to create a simple web application using Flask.',
        'date_posted': 'February 15, 2022',
    },
    {
        'author': 'Alice Johnson',
        'title': 'Exploring Jinja Templating',
        'content': 'Understanding the power of Jinja templating in Flask applications.',
        'date_posted': 'May 20, 2022',
    },
    {
        'author': 'Bob Williams',
        'title': 'Working with SQLite3 in Python',
        'content': 'A guide on using SQLite3 for database operations in Python applications.',
        'date_posted': 'August 8, 2022',
    },
    {
        'author': 'Eva Davis',
        'title': 'Dockerizing Your Python Applications',
        'content': 'Learn how to containerize your Python applications using Docker.',
        'date_posted': 'November 30, 2022',
    },
    {
        'author': 'Carlos Rodriguez',
        'title': 'Getting Started with Bootstrap',
        'content': 'Learn how to enhance the styling and responsiveness of your web applications using Bootstrap.',
        'date_posted': 'December 15, 2022',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


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

if __name__ == "__main__":
    app.run(debug=True)