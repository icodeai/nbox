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
        #self.assertEqual('Version', a.connect())
        #self.assertEqual(None, a.connect())
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()