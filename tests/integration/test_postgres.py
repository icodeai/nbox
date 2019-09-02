import os
from unittest import TestCase

from db_config import PostgresConfig


TEST_DATABASE_URL       = os.getenv('TEST_DATABASE_URL')
WRONG_TEST_DATABASE_URL = os.getenv('WRONG_TEST_DATABASE_URL')


class PostgresTestCase(TestCase):
    
    def setUp(self):

        self.postgres      = PostgresConfig()
        self.database_name = 'database_for_testing'
        self.query         = """CREATE TABLE IF NOT EXISTS test_table_one (
                table_id serial PRIMARY KEY NOT NULL,
                table_number int NOT NULL,
                table_info character varying(1000),
                date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
                )"""
        self.table_name    = 'test_table_one'
       
    def test_make_good_connection(self):  
        self.assertNotEqual(self.postgres.connect(TEST_DATABASE_URL),
                            'failed to connect to database.')

    def test_close_connection(self):
        connection = self.postgres.connect(TEST_DATABASE_URL)
        self.assertEqual(self.postgres.close(connection),"Close connection successful")

    def test_close_connection_failure(self):
        connection = self.postgres.connect(WRONG_TEST_DATABASE_URL)
        self.assertEqual(self.postgres.close(connection),"Close connection failed")
        self.assertNotEqual(self.postgres.connect(TEST_DATABASE_URL),
                            'failed to connect to database.')
    
    def test_create_table(self): 
        self.assertNotEqual(self.postgres.create_table(
            self.query, TEST_DATABASE_URL), 'Failed to create table')
 
    def test_fail_create_table(self):
        self.assertEqual(self.postgres.create_table(
            self.query, WRONG_TEST_DATABASE_URL), 'Failed to create table')

    def test_drop_table(self):        
        self.postgres.create_table(self.query, TEST_DATABASE_URL)
        self.assertNotEqual(self.postgres.drop_table(
            self.table_name, TEST_DATABASE_URL), f"Unable to drop table {self.table_name}")

    def test_fail_drop_table(self):
        self.assertEqual(self.postgres.drop_table(
            self.table_name, WRONG_TEST_DATABASE_URL), f"Unable to drop table {self.table_name}")    
 
    def test_create_database(self):
        self.assertNotEqual(
            self.postgres.create_database(self.database_name),
            f"failed to create database {self.database_name}")    
      
    def test_drop_database(self):
        self.postgres.create_database(self.database_name)
        self.assertNotEqual(
            self.postgres.drop_database(self.database_name),
            f"failed to drop database {self.database_name}")
           

    def tearDown(self):
        self.postgres.drop_table(self.table_name, TEST_DATABASE_URL)
        self.postgres.drop_database(self.database_name)

    def test_show_table(self):
        self.assertNotEqual(self.postgres.show_table(TEST_DATABASE_URL),
                            'Failed to show tables')
