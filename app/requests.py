import  urllib.request, json
from models import Articles, Sources
import os
# import requests

api_key=None
source_url=None
articles_url=None

def configure_request(app):
    global api_key,source_url,articles_url
    api_key=app.config['NEWS_API_KEY']
    source_url=app.config['NEWS_API_BASE_URL']
    articles_url=app.config['ARTICLES_API_URL']

def get_sources(category):
    '''
    A function to get news sources by categories
    '''

    src_url= source_url.format(category, api_key)

    with urllib.request.urlopen(src_url) as url:
        sources_data=url.read()
        get_repsonse=json.loads(sources_data)

        sources_result=None

        if get_repsonse['sources']:
            sources_output=get_repsonse['sources']
            sources_result=process_news(sources_output)

    return sources_result

def process_news(sourceList):
    sources_result=[]
    for source in sourceList:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        category=source.get('category')
        language=source.get('language')
        country=source.get('country')

        new_source=Sources(id, name, description, url , category, language, country)
        sources_result.append(new_source)
        
    return sources_result


        

