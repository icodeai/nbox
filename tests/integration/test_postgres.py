import os
from unittest import TestCase

from db_config import PostgresConfig


TEST_DATABASE_URL       = os.getenv('TEST_DATABASE_URL')
WRONG_TEST_DATABASE_URL = os.getenv('WRONG_TEST_DATABASE_URL')


class PostgresTestCase(TestCase):
    
    def setUp(self):
        self.postgres = PostgresConfig()
       
    
    def test_make_good_connection(self):
        print(TEST_DATABASE_URL)
        self.assertNotEqual(self.postgres.connect(TEST_DATABASE_URL),
                            'failed to connect to database.')

    def test_create_database(self):
        self.assertNotEqual(self.postgres.create_database(TEST_DATABASE_URL),
                            'connected')