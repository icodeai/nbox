import os
from unittest import TestCase
from db_config import PostgresConfig


class PostgresTestCase(TestCase):
         
    def test_table(self):
        query ='''CREATE TABLE TESTTABLE
                  (ID INT PRIMARY KEY  NOT NULL,
                   VALUE1          TEXT NOT NULL,)
                   '''
        db = PostgresConfig()
        db.connect()
        a = db.create_table(query)
        self.assertEqual(a ,'table created')
