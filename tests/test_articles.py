import unittest
from app.models import Articles

class articlesTest(unittest.TestCase):
    '''
    A sub-class that will test the behaviors of my articles
    '''
    def setup(self):
        '''
        This is a method that runs before every other test runs
        '''
        self.new_article=Articles('Reuters', 'Omar Mohammed', 'Athletics-Kenya\'s Kipchoge cements legacy as greatest marathon runner - Reuters', 'About 30 kilometres into the men\'s marathon in Sapporo on Sunday...', 'https://www.reuters.com/lifestyle/sports/athletics-kenyas-kipchoge-cements-legacy-greatest-marathon-runner-2021-08-08/', 'https://cutt.ly/6QTz8zA', '2021-08-08T04:39:00Z', 'TOKYO, Aug 8 (Reuters) - About 30 kilometres into the men\'s marathon in Sapporo on Sunday, Kenya\'s Eliud Kipchoge pulled away')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__=='__main__':
    unittest.main()