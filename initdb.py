from flaskblog import app, db
from flaskblog.models import User, Post
from datetime import datetime

app.app_context().push()
db.create_all()

posts_data = [
    {
        'author': 'John Doe',
        'title': 'Introduction to Python',
        'content': 'This post covers the basics of Python programming language.',
        'date_posted': datetime.strptime('January 1, 2024', '%B %d, %Y'),
    },
    {
        'author': 'Jane Smith',
        'title': 'Getting Started with Flask',
        'content': 'Learn how to create a simple web application using Flask.',
        'date_posted': datetime.strptime('January 1, 2024', '%B %d, %Y'),
    },
    {
        'author': 'Alice Johnson',
        'title': 'Exploring Jinja Templating',
        'content': 'Understanding the power of Jinja templating in Flask applications.',
        'date_posted': datetime.strptime('January 1, 2024', '%B %d, %Y'),
    },
    {
        'author': 'Bob Williams',
        'title': 'Working with SQLite3 in Python',
        'content': 'A guide on using SQLite3 for database operations in Python applications.',
        'date_posted': datetime.strptime('January 1, 2024', '%B %d, %Y'),
    },
    {
        'author': 'Eva Davis',
        'title': 'Dockerizing Your Python Applications',
        'content': 'Learn how to containerize your Python applications using Docker.',
        'date_posted': datetime.strptime('January 1, 2024', '%B %d, %Y'),
    },
    {
        'author': 'Carlos Rodriguez',
        'title': 'Getting Started with Bootstrap',
        'content': 'Learn how to enhance the styling and responsiveness of your web applications using Bootstrap.',
        'date_posted': datetime.strptime('January 1, 2024', '%B %d, %Y'),
    }
]

for post_data in posts_data:
    author = User.query.filter_by(username=post_data['author']).first()
    
    if not author:
        # Si el autor no existe, crea un nuevo usuario
        author = User(username=post_data['author'], email=f"{post_data['author'].lower()}@example.com", password='password')
        db.session.add(author)
        db.session.commit()

    post = Post(
        title=post_data['title'],
        content=post_data['content'],
        date_posted=post_data['date_posted'],
        author=author
    )
    
    db.session.add(post)
    db.session.commit()

print("DB populated!")
