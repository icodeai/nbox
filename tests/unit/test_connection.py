import os
import unittest
from Postgres import Postgresdb

user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')

class TestCnnctn(unittest.TestCase):

    def test_connection(self):
        db = Postgresdb()
        self.assertEqual(db.connect(user,password,host,port,database),
                            'connection successful')

if __name__ == "__main__":
    unittest.main()
