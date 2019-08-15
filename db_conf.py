import os
import psycopg2 as pg 

from database import Postgres

DATABASE_URL = os.getenv('DATABASE_URL')


class myDatabaseAdb(Postgres):
   
    
    def connect(self,DATABASE_URL):
        """Create Connection 
        ARGS: 
            Takes in url of the database with correct credentials

        OUTPUT : 
            Returns connection Object if connection is successful or else error
        """
        try:
            connection = pg.connect(DATABASE_URL)
            return connection
        except Exception as e:
            return e

        
    def cursor(self,DATABASE_URL):
        """create cursor object which enables us to perform CRUDE operations
        ARGS :
            Takes DATABASE_URL as an argument

        OUTPUT : 
            Returns cursor object
            
        """

        connection = self.connect(DATABASE_URL)
        cursor = connection.cursor()

        return cursor
            

        

        

db = myDatabaseAdb().cursor(DATABASE_URL)
print(db)
        
