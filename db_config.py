import os

import psycopg2 as p

from database import Postgres

DATABASE_URL = os.getenv('DATABASE_URL')

class PostgresConfig(Postgres):

    
    def connect(self,database_url):
        '''Create a connection to a PostgreSQL database instance.
        
        Args:
            database_url (str): A url with a given user database credentials.
        
        Returns:
            object: A PostgreSQL Connection Object. 
                    This connection is thread-safe and can be shared among many threads.
            
            str: It is returned incase there is a database error or exception that may 
                 occur while working with PostgreSQL from Python. 
        '''
        
        try:

            connection = p.connect(database_url)
            connection.autocommit = True
            return connection

        except:

            return 'failed to connect to database.'
      
    def cursor(self):
        '''Create a cursor object which allows us to execute PostgreSQL command
           through Python source code.
           Cursors created from the same connection are not isolated, i.e., any changes
           done to the database by a cursor are immediately visible by the other cursors.
        
        Returns:
            Object:cursor object.
        '''
        try: 

            connection = self.connect(DATABASE_URL)
            cursor = connection.cursor()
            return cursor

        except:
            return 'Can not exucute PostgreSQL command'

    def create_database(self, db_name):
        """Creates a Postgres database.
        
        Arguments:
            db_name(str): A name of the given database.
        
        Returns:
            None if no exception or error mssg incase there is one. 
        """
    
        try: 

            query = f"""CREATE DATABASE {db_name};"""
    
            conn = self.connect(DATABASE_URL)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
           
        except  :
            return "Error while connecting to PostgreSQL"

if __name__ == "__main__":
    db = PostgresConfig()
    
    print(db.connect(DATABASE_URL))
    print(db.create_database('db_name'))
