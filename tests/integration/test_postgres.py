import os
from unittest import TestCase

from db_config import PostgresConfig


TEST_DATABASE_URL       = os.getenv('TEST_DATABASE_URL')
WRONG_TEST_DATABASE_URL = os.getenv('WRONG_TEST_DATABASE_URL')


class PostgresTestCase(TestCase):
    
    def setUp(self):
        self.postgres      = PostgresConfig()
        self.database_name = 'database_for_testing'
       
    
    def test_make_good_connection(self):
        
        self.assertNotEqual(self.postgres.connect(TEST_DATABASE_URL),
                            'failed to connect to database.')

    def test_drop_database(self):

        self.postgres.create_database(self.database_name)

        self.assertNotEqual(
            self.postgres.drop_database(self.database_name),
                            "failed to drop database")

    def test_create_database(self):
        
        self.assertNotEqual(
            self.postgres.create_database(self.database_name),
                                          "failed to create database")

    def tearDown(self):
        self.postgres.drop_database(self.database_name)

