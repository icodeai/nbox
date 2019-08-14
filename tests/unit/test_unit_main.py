from .. import  main
import unittest

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
        pass
    
if __name__ == '__main__':
    unittest.main()