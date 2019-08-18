import os
from unittest import TestCase

from create_tables import create_tables


TEST_DATABASE_URL       = os.getenv('TEST_DATABASE_URL')
WRONG_TEST_DATABASE_URL = os.getenv('WRONG_TEST_DATABASE_URL')


class PostgresTestCase(TestCase):
    
    def setUp(self):
        self.postgres = create_tables()
       
    
    def test_create_tables(self):
        print(TEST_DATABASE_URL)
        self.assertNotEqual(self.postgres.create_tables(TEST_DATABASE_URL),
                            'failed to create tables.')