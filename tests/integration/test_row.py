import os
from unittest import TestCase
from db_config import PostgresConfig


class PostgresTestCase(TestCase):
         
    def test_row(self):
        query ='''CREATE TABLE IF NOT EXISTS TESTTABLE 
                  (testvalue int,
                   anothervalue int)
                   '''
        anotherquery='''INSERT INTO TESTTABLE(testvalue,anothervalue)
                        VALUES(12,13);
                    '''
        db = PostgresConfig()
        db.connect()
        a = db.create_table(query)
        b = db.insert_rows(anotherquery)
        self.assertEqual(b,"row created")
