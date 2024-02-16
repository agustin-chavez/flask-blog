# flask-blog
A blog application made with Python and Flask

## Notes

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
```

Go to http://127.0.0.1:5000/

### Database with Flask-SQLAlchemy
SQLAlchemy, a Python Object-Relational Mapping (ORM) tool, simplifies database interaction with Python classes, abstracting SQL queries. Its flexibility spans various databases, such as SQLite, MySQL or PostgreSQL allowing seamless transitions without code rewrites.

```bash
pip install flask-sqlalchemy
```

After creating the models, run the initdb.py script to populate some data in the database, or if just want the tables run:
```python
from flaskblog import app, db
app.app_context().push()
db.create_all()
```

### Modules and Packages
In Python, both packages and modules are mechanisms for organizing and structuring code.

Modules: These are individual Python files containing reusable code. Each file with a .py extension is considered a module. A module can include functions, classes, and variables, and it can be imported into other scripts to reuse its functionality.

Packages: These are directories containing multiple modules and optionally sub-packages. Packages are designed to organize and structure larger projects. A package must contain a special file named __init__.py to indicate that the directory should be treated as a Python package.


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

Now in our project directory we have a python package and a python module to run the app, and another to initialize de database.
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

With bcrypt, the hash function generates a unique value even when the same password is used. This is beneficial because it prevents someone from attempting to crack passwords using hash tables.

```bash
hashed = bcrypt.generate_password_hash('my_super_secure_password').decode('utf-8')
bcrypt.check_password_hash(hashed, 'wrong_password')
>>> False
bcrypt.check_password_hash(hashed, 'my_super_secure_password')
>>> True
```

Flask-Login provides user session management for Flask applications, making it easier to handle user authentication and user sessions. It allows you to manage user sessions, handle user login/logout, and restrict access to certain views or routes based on the user's authentication status.

