import os
import psycopg2
import psycopg2 as error
from database import Postgres
from create_tables import Create_tables

DATABASE_URL = os.environ.get('DATABASE_URL')

def drop_table(self,Postgres, query):
    """ Drop tables in the nbox database"""
    
    try:
        self.cur.execute(query)
        self.connection.commit()

    except (Exception, psycopg2.Error)as error:
        print("Error while droping the table")