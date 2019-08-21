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

        connection = self.connect(DATABASE_URL)
        cursor = connection.cursor()
        return cursor

    def create_database(self, database_name):
        '''Creates a database on a given postgresql server.
        
        Args:
            database_name (str): a name of the databse to be created.
        
        Returns:
             a str if database creation failed.
        '''
        
        try:
            query = f"""CREATE DATABASE {database_name};"""

            cursor = self.cursor()
            cursor.execute(query)
     
        except (Exception, p.DatabaseError) as error:

            return f"failed to create database {database_name}, due to {error}"
            

    def drop_database(self,database_name):
        '''Drops a given database in a postgresql server.
        
        Args:
            database_name (str): name of databse to drop
        
        Returns:
            a str if unable to drop the given database.
        '''
                
        try:
            query = f"""DROP DATABASE IF EXISTS {database_name};"""

            cursor = self.cursor()
            cursor.execute(query)
            
        except Exception:

            return f"failed to drop database {database_name}"



if __name__ == "__main__":
    db = PostgresConfig()
    print(db.connect(DATABASE_URL))
    print(db.create_database('db_one'))
    print(db.drop_database('db_one'))
