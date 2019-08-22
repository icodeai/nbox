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

    def test_create_table(self):
        b = ('''CREATE TABLE TEST2 (ID INT PRIMARY KEY NOT NULL,
            NAME    TEXT    NOT NULL,
            AGE     INT     NOT NULL,
            ADDRESS CHAR(50),
            SALARY  REAL);''')
        self.assertEqual('table created', self.postgres.create_table(b))
        
    