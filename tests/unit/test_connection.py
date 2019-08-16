import os
import unittest
from Postgres import Postgresdb

dbParameters = os.getenv('dbParameters')

class TestCnnctn(unittest.TestCase):

    def test_connection(self):
        db = Postgresdb()
        self.assertEqual(db.connect(dbParameters),
                            'connection successful')

if __name__ == "__main__":
    unittest.main()
