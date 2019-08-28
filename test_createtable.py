import os
from unittest import TestCase
from db_config import PostgresConfig

TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')


class PostgresTestCase(TestCase):
    def test_make_good_connection(self):
        print(TEST_DATABASE_URL)
        self.assertNotEqual(self.postgres.connect(TEST_DATABASE_URL), 'failed to connect to database.')

    def test_create_table(self):
        self.assertNotEqual(self.postgres.create_table(TEST_DATABASE_URL), 'connected')
