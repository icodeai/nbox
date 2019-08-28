import os

import psycopg2 as p

from database import Postgres

DATABASE_URL = os.environ.get('Database_URL')

class PostgresConfig(Postgres):

    
    def connect(self, DATABASE_URL):
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

            connection = p.connect(DATABASE_URL)
            return connection

        except (Exception, p.Error) as error:
            return ("Error while connecting to PostgreSQL", error)
      
    def cursor(self, DATABASE_URL):
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

    def create_table(self, query):
        '''Creates a table in a given database.

        Args:
            query : an sql query to be executed.
            database_url : it contains database connection credentials.

        Returns:
            creates a table or it returns an error message in the event of a failure.
        '''

        try:
            connection = self.connect(DATABASE_URL)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()


        except (Exception, p.DatabaseError) as error:
            print('Failed to create table', error)


if __name__ == "__main__":
    db = PostgresConfig()
    query = '''CREATE TABLE alpha (
	id INT,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	app_name VARCHAR(50) NOT NULL,
	email VARCHAR(35),
	gender VARCHAR(10) NOT NULL);'''
    db.connect(DATABASE_URL)
    db.create_table(query)
