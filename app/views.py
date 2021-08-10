from flask import render_template
from app import app
from .requests import get_source

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_source()
    print(general_news)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, general = general_news)

# Views
@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('source.html',id = source_id)