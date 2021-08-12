# from app import app
import urllib.request,json
from .models import Source, Articles

# Articles=articles.Articles
# Source = source.Source

api_key = None
base_url = None
article_url= None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url= app.config['NEWS_ARTICLES_API_URL']


def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    # base_url='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    get_source_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_sources_response = json.loads( get_source_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results= process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    '''
    source_results = []
    for source_item in source_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category=source_item.get('category')
        language=source_item.get('language')
        country=source_item.get('country')
       
        new_source=Source(id, name, description, url , category, language,country)
        source_results.append(new_source)

    return source_results


def get_articles(article):

    articles_url = article_url.format(article,api_key)
    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_outcome = None

        if articles_response['articles']:
            articles_outcome_items = articles_response['articles']
            articles_outcome = process_new_articles(articles_outcome_items)

    return articles_outcome

def process_new_articles(articles_list):
    articles_outcome = []
    for one_article in articles_list:
        source = one_article.get("source")
        author = one_article.get("author")
        description = one_article.get("description")
        title = one_article.get("title")
        url = one_article.get("url")
        urlToImage = one_article.get("urlToImage")
        publishedAt = one_article.get("publishedAt") 

        new_article = Articles(source, author, title, description, url, urlToImage, publishedAt)
        articles_outcome.append(new_article)
    
    return articles_outcome

def articles_source(source):
    sources_a_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(source,api_key)

    with urllib.request.urlopen(sources_a_url) as url:
        art_data = url.read()
        response = json.loads(art_data)
        source_articles = None
        if response['articles']:
            source_articles_list = response['articles']
            source_articles = process_articles_source(source_articles_list)
    return source_articles

def process_articles_source(article_list):
    source_articles = []
    for art in article_list:
        source = art.get("source")
        author = art.get('author')
        title = art.get('title')
        description = art.get('description')
        url = art.get('url')
        urlToImage = art.get('urlToImage')
        publishedAt = art.get('publishedAt')
        
        article_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        source_articles.append(article_object)
    return source_articles