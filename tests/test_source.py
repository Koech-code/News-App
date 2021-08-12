import unittest
from app.models import Source

class testSource(unittest.TestCase):
    """
    SourcesTest class to test the behavior of the Sources class
    """
    def setUp(self):
        """
        Method that runs before each other test runs
        """
        self.new_source = Source('abc-news','ABC news','Your trusted source for breaking news',"https://abcnews.go.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == "__main__":
    unittest.main()