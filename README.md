# flask-blog

A CRUD blog application made with Python 3.12, Flask, SQLite3 and SQLAlchemy.

### Run

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

export SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
export SECRET_KEY="<SECRET_KEY_FOR_SESSIONS_SECURITY>"
export EMAIL_USER="<EMAIL_FOR_RESET_PASSWORD_SIMULATION>"
export EMAIL_PASS="<PASS_FOR_RESET_PASSWORD_SIMULATION>"

python3 run.py
```

Go to http://127.0.0.1:5000/

## How to generate a secret with the python interpreter

```python
import secrets

secrets.token_hex(16)
```

## Features

- Register, login and logout
- Flash messages
- Form validations
- Encrypted passwords
- See and update account username, email, password and profile picture
- Create, Read, Update and Delete posts
  
    ![register](https://github.com/agustin-chavez/flask-blog/assets/39955956/846797ec-c244-4534-b67f-04c31a8b7e94)
  
    ![login](https://github.com/agustin-chavez/flask-blog/assets/39955956/f6e54f8c-82fb-4d58-a38b-a16cba767303)
  
    ![validations](https://github.com/agustin-chavez/flask-blog/assets/39955956/f6e3ac4f-e347-4f3f-86c1-92524cbc574f)

    ![home](https://github.com/agustin-chavez/flask-blog/assets/39955956/c2463aa0-ce38-494b-9c8f-21f30d258fcf)

    ![account](https://github.com/agustin-chavez/flask-blog/assets/39955956/cd2e5eea-df0a-477e-9952-f3b622dbda95)

    ![post](https://github.com/agustin-chavez/flask-blog/assets/39955956/701f2d72-394f-430b-8dfd-611f8bcb3a66)
  
    ![posts](https://github.com/agustin-chavez/flask-blog/assets/39955956/63eb7081-e7c1-44ef-8a0a-05154ea33a9a)

    ![update](https://github.com/agustin-chavez/flask-blog/assets/39955956/e4347a6a-99eb-427e-a5e9-2027796ece1f)

    ![delete](https://github.com/agustin-chavez/flask-blog/assets/39955956/5843b1e3-0631-4ab8-932d-6c63455fd39c)


## Development notes for reference

### Set environment variable and run

```bash
export FLASK_APP=flaskblog.py
flask run
```

### Run directly with Python

```bash
python flaskblog.py
```

### Create a virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate

pip install --upgrade pip
pip install Flask
pip install flask-wtf

python3 run.py
```

Go to http://127.0.0.1:5000/

### Database with Flask-SQLAlchemy

SQLAlchemy, a Python Object-Relational Mapping (ORM) tool, simplifies database interaction with Python classes,
abstracting SQL queries. Its flexibility spans various databases, such as SQLite, MySQL or PostgreSQL allowing seamless
transitions without code rewrites.

```bash
pip install flask-sqlalchemy
```

After creating the models, run the initdb.py script to populate some data in the database, or if just want the tables
run:

```python
from flaskblog import app, db

app.app_context().push()
db.create_all()
```

### Modules and Packages

In Python, both packages and modules are mechanisms for organizing and structuring code.

Modules: These are individual Python files containing reusable code. Each file with a .py extension is considered a
module. A module can include functions, classes, and variables, and it can be imported into other scripts to reuse its
functionality.

Packages: These are directories containing multiple modules and optionally sub-packages. Packages are designed to
organize and structure larger projects. A package must contain a special file named __init__.py to indicate that the
directory should be treated as a Python package.

### Reorganize project structure

```bash
├── flaskblog
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   └── main.css
│   └── templates
│       ├── about.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
├── initdb.py
└── run.py
```

Now in our project directory we have a python package and a python module to run the app, and another to initialize de
database.
The __init__.py file tells python that this is a package and help us avoid circular dependencies with imports.

```bash
python initdb.py
python run.py
```

### Authorization and Authentication

```bash
pip install flask-login
pip install flask-bcrypt

python

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing')
>>> "a password hash in bytes"
bcrypt.generate_password_hash('testing').decode('utf-8')
>>> "a password hash as a text string"
```

With bcrypt, the hash function generates a unique value even when the same password is used. This is beneficial because
it prevents someone from attempting to crack passwords using hash tables.

```bash
hashed = bcrypt.generate_password_hash('my_super_secure_password').decode('utf-8')
bcrypt.check_password_hash(hashed, 'wrong_password')
>>> False
bcrypt.check_password_hash(hashed, 'my_super_secure_password')
>>> True
```

Flask-Login provides user session management for Flask applications, making it easier to handle user authentication and
user sessions. It allows you to manage user sessions, handle user login/logout, and restrict access to certain views or
routes based on the user's authentication status.

### Images

To enhance site performance and prevent slowdowns, it's advisable to scale down large profile images before saving them
to the filesystem. This can be achieved using various Python libraries, such as Pillow (PIL), which is commonly used for
image processing.

```bash
pip install Pillow
```

```python
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename
```

### Mail

```bash
pip install flask-mail
```
