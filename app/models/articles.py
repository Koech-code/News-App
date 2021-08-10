
class Articles:
    '''
    This is my sources class which helps create instances of news sources
    '''

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
    
