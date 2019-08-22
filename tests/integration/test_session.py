import os
from unittest import TestCase
from db_config import PostgresConfig


class PostgresTestCase(TestCase):
         
    def test_session(self):
        db = PostgresConfig()
        self.assertNotEqual(db.session(),
                            'autocommit enabled')
