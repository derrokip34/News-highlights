from flask import render_template
from app import app
from .request import get_sources,get_articles

@app.route('/')
def index():

    general_news = get_sources('general')
    business_news = get_sources('business')
    sports_news = get_sources('sports')
    entertainment_news = get_sources('entertainment')
    technology_news = get_sources('technology')
    health_news = get_sources('health')

    title = 'Welcome To Fro News'
    return render_template('index.html',title = title, general = general_news, business = business_news, sports = sports_news, entertainment = entertainment_news, technology = technology_news, health = health_news)

@app.route('/articles/<id>')
def articles(id):

    news_articles = get_articles(id)

    title = f'{id}'

    return render_template('articles.html', title = title, articles = news_articles)