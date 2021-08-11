import unittest
from ..models import source

Source=source.Source

class testSource(unittest.TestCase):
    '''
    Sources sub-class that will help me test the behaviors of the source class
    '''

    def setup(self):
        '''
        A method that will run before any other test runs
        '''
        self.new_source=Source('abc-news-au','ABC news AU', 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.', 'http://www.abc.net.au/news', 'general', 'en', 'au')

    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_source,Source))

if __name__=='__main__':
    unittest.main()
        