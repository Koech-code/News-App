class Source:
    '''
    This is my sources class which helps create instances of news sources
    '''

    def __init__(self, id, name, description, url, category, language, country):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.language=language
        self.country=country


class Articles:
    '''
    This is my sources class which helps create instances of news sources
    '''

    def __init__(self, source, author, title, description, url, urlToImage, publishedAt):
        self.source=source
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
    
