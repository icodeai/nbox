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
  
    def test_select_table(self):
        """
        Test fetch and display of records
        """
        b = "SELECT id, name, address, salary from COMPANY"
        self.assertEqual('success', a.select_table(b))
        
if __name__ == '__main__':
    unittest.main()