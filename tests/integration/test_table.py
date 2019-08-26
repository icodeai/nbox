import os
from unittest import TestCase
from db_config import PostgresConfig


class PostgresTestCase(TestCase):
         
    def test_table(self):
        query ='''CREATE TABLE IF NOT EXISTS TESTTABLE 
                  (testvalue int,
                   anothervalue int)
                   '''
        db = PostgresConfig()
        db.connect()
        a = db.create_table(query)
        self.assertEqual(a,"table created")
