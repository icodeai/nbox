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

        connection = p.connect(DATABASE_URL)
        cursor = connection.cursor()
        return cursor
    
    def select_table(self, query):
        """"
        Fetch and disaplay records from a database
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''CREATE TABLE COMPANY
                (ID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL,
                AGE            INT     NOT NULL,
                ADDRESS        CHAR(50),
                SALARY         REAL);''')
            return 'Table created successfully'
        except:
            return 'failed to create tables'
            
