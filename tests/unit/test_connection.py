import os
import unittest
from db_config import PostgresConfig

class TestCnnctn(unittest.TestCase):

    def test_connection(self):
        db = PostgresConfig()
        self.assertEqual(db.connect(),
                            'connection successful')

