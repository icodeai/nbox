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
        
    def test_create_table(self):
        """
        Test function to create a table
        """
        b = ('''CREATE TABLE TEST (ID INT PRIMARY KEY NOT NULL,
            NAME    TEXT    NOT NULL,
            AGE     INT     NOT NULL,
            ADDRESS CHAR(50),
            SALARY  REAL);''')
        self.assertEqual('success', a.create_table(b))
    
    def test_insert_rows(self):
        """
        Test for inserting rows
        """
        b = ("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
        self.assertEqual('success', a.insert_rows(b))
        
    def test_show_table(self):
        """
        Test function to show table
        """
        b = ("SELECT id, name, address, salary from COMPANY")
        self.assertEqual('success', a.show_table(b))

if __name__ == '__main__':
    unittest.main()