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
                            'failed to connect to database.')

    def test_close_connection(self):
        connection = self.postgres.connect(TEST_DATABASE_URL)
        
        self.assertEqual(self.postgres.close(connection),"Close connection successful")

    def test_close_connection_failure(self):
        connection = self.postgres.connect(WRONG_TEST_DATABASE_URL)
        self.assertEqual(self.postgres.close(connection),"Close connection failed")
