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
            return 'Can not execute PostgreSQL commands'

    def create_table(self,tb_name):
        """
        Creates a table in the database.

        Arguments:
        ----------
            tb_name(str): The name of the table.

        Returns:
        --------
            Returns Table created successful or Error while creating a table incase the table is not created.
        """
        try:
            query = f"""CREATE TABLE TABLE2
                (ID serial PRIMARY KEY     NOT NULL,
                username VARCHAR (50) UNIQUE NOT NULL,
                password VARCHAR (50) NOT NULL
                );"""
    
            conn = self.connect(DATABASE_URL)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return "Table created successfully."
        except:
            #Exception as e
            return "Error while creating a table."
             # return e

if __name__ == "__main__":
    db = PostgresConfig()
    print(db.connect(DATABASE_URL))
    print(db.create_table('tb_name'))
