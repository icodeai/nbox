import unittest
from main import PostgresDb
from config import config

a = PostgresDb
class TestPostgres(unittest.TestCase):
    """
    Test database connectivity
    
    Arguments:
        unittest {[type]} -- [description]
    """
    def test_connection(self):
        """
        Test that the database connection is succesful
        """
        self.assertEqual('success', a.connect())
        
    def test_cursor(self):
        """
        Test cursor function
        """
        self.assertEqual('success', a.cursor())
  
    
if __name__ == '__main__':
    unittest.main()