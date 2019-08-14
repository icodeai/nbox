import os
import psycopg2 as pg 

from database import Postgres

DATABASE_URL = os.getenv('DATABASE_URL')


class myDatabaseAdb(Postgres):
    """Test db connection"""
    def connect(self,db_url):
        try:
            connection = pg.connect(db_url)
            print("conncection success")
        except Exception as e:
            return e

db = myDatabaseAdb().connect(DATABASE_URL)
print(db)
        
