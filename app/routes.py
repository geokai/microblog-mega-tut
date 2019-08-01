from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'George'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Meghan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Robert'},
            'body': 'The auto-complete is blocking!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)