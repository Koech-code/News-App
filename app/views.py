from flask import render_template
from app import app
from .requests import get_source,articles_source,get_articles

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_source('general')
    business_news = get_source('business')
    technology_news = get_source('technology')
    print(general_news)
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title, general = general_news, business=business_news, technology=technology_news)

# Views
@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View source page function that returns the news details page and its data
    '''
    return render_template('source.html',id = source_id)

@app.route('/articles/<id>')
def sourceArticles(id):
    all_articles = articles_source(id)
    print(all_articles)
    source = id
    return render_template('articles.html', articles = all_articles, source = source)

@app.route('/News-Articles')
def NewsArticles():
    """
    View that would return news articles
     
    """
    health_articles = get_articles('health')
    education_articles = get_articles('technology')
    
    return render_template('articles.html',health=health_articles, tech =education_articles)

