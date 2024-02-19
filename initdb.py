from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from datetime import datetime
from flask import current_app

current_app.app_context().push()
db.create_all()

from datetime import datetime

posts_data = [
    {
        'author': 'johndoe',
        'title': 'Introduction to Python Programming',
        'content': 'In this comprehensive guide, we delve deep into the fundamentals of Python programming language. From basic syntax to advanced concepts, this post covers it all.',
        'date_posted': datetime(2024, 1, 1),
    },
    {
        'author': 'janesmith',
        'title': 'Mastering Flask for Web Development',
        'content': 'Explore the intricacies of Flask and learn how to build dynamic web applications with this step-by-step tutorial. Get ready to embark on a journey of Flask mastery.',
        'date_posted': datetime(2024, 1, 2),
    },
    {
        'author': 'alicejohnson',
        'title': 'Deep Dive into Jinja Templating in Flask',
        'content': 'Uncover the power and flexibility of Jinja templating in Flask applications. This in-depth exploration will guide you through harnessing the full potential of Jinja.',
        'date_posted': datetime(2024, 1, 3),
    },
    {
        'author': 'bobwilliams',
        'title': 'SQLite3 Database Operations in Python',
        'content': 'Navigate the world of SQLite3 for database operations in Python applications. This comprehensive guide provides practical tips and tricks for effective database management.',
        'date_posted': datetime(2024, 1, 4),
    },
    {
        'author': 'evadavis',
        'title': 'Dockerizing Python Applications for Scalability',
        'content': 'Learn the art of containerization with Docker and discover how it can enhance the scalability and deployment of your Python applications. Get ready to dockerize!',
        'date_posted': datetime(2024, 1, 5),
    },
    {
        'author': 'carlosrodriguez',
        'title': 'Bootstrap: Elevating Web Application Styling',
        'content': 'Take your web application styling to the next level with Bootstrap. This tutorial guides you through the integration and utilization of Bootstrap for enhanced aesthetics and responsiveness.',
        'date_posted': datetime(2024, 1, 6),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 7',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 7),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 8',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 8),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 9',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 9),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 10',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 10),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 11',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 11),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 12',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 12),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 13',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 13),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 14',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 14),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 15',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 15),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 16',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 16),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 17',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 17),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 18',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 18),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 19',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 19),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 20',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 20),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 21',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 21),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 22',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 22),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 23',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 23),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 24',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 24),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 25',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 25),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 26',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 26),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 27',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 27),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 28',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 28),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 29',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 29),
    },
    {
        'author': 'johndoe',
        'title': 'More Python Adventures Part 30',
        'content': 'Explore advanced Python topics in this continuation of our Python series. Dive into new concepts and techniques to elevate your Python programming skills.',
        'date_posted': datetime(2024, 1, 30),
    },
]

for post_data in posts_data:
    author = User.query.filter_by(username=post_data['author']).first()
    
    if not author:
        username = post_data['author'].replace(' ', '.')
        email = f"{post_data['author'].lower().replace(' ', '.')}@example.com"
        hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')

        author = User(username=username, email=email, password=hashed_password)
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
