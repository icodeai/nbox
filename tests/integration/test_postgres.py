import os
from unittest import TestCase

from db_config import PostgresConfig


TEST_DATABASE_URL       = os.getenv('TEST_DATABASE_URL')
WRONG_TEST_DATABASE_URL = os.getenv('WRONG_TEST_DATABASE_URL')


class PostgresTestCase(TestCase):
    
    def setUp(self):
        self.postgres = PostgresConfig()
       
    
    def test_make_good_connection(self):
        self.assertNotEqual(self.postgres.connect(TEST_DATABASE_URL),
                            'connected')
    def test_drop_table(self):
        """
        tests for drop table method
        
        Arguments:
            query {[SQL statement]} -- [description]
        """
        self.assertNotEqual(self.postgres.drop_table(TEST_DATABASE_URL),
                                                  'connected')