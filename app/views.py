from flask import render_template
from app import app
from .request import get_sources,get_articles

@app.route('/')
def index():

    title = 'Welcome To Fro News'
    return render_template('index.html',title = title)

@app.route('/articles/<id>')
def articles(id):

    title = f'{id}'

    return render_template('articles.html', title = title)