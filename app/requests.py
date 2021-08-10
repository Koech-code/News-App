from app import app
import urllib.request,json
from .models import source

Source = source.Source
# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    # base_url='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    get_source_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_source_url ) as url:
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
       
        new_source=Source(id, name, description, url , category, language)
        source_results.append(new_source)

    return source_results