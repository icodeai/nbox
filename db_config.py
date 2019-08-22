import os

import psycopg2

from database import Postgres

dbParameters = os.getenv('dbParameters')

class PostgresConfig(Postgres):

    def __init__(self):
        #initializes the Postgresdb class
        self.connection = None
        self.cursordb = None

    def connect(self):
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
            self.connection = psycopg2.connect(dbParameters)
            self.cursordb = self.connection.cursor()
            return 'connection successful'

        except (Exception, psycopg2.Error) as error :    
            return error
      
    def session(self):
        try:
         self.connection.set_session(autocommit = True)
         return 'autocommit enabled'
        except (Exception, psycopg2.Error) as error :    
            return error
         