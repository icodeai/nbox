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
            
        except (Exception, p.DatabaseError) as error:

            return f"failed to drop database {database_name}, due to {error}"



    def close(self,connection):
        try:
           
            connection.close()

            return "Close connection successful"

        except:
            return "Close connection failed"

    def create_table(self,query,database_url):
        '''Creates a table in a given database.
        
        Args:
            query (Docstring): an sql query to be executed.
            database_url (str): it contains database connection credentials.
        
        Returns:
            creates a table or it returns a message incase method fails to
             create database.
        '''
        
        try:

            conn = self.connect(database_url)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            
        except Exception:

            return 'Failed to create table'

    def drop_table(self, table_name, database_url):
        '''Drops a table if it exists in the given database.
        
        Args:
            table_name (str): name of the table to be dropped.
            database_url (str): a string containing connection database credentials.
        
        Returns:
            Drops a given table or returns a string indicating unable to drop the table.
        '''

        try:
        
            query = f"""DROP TABLE IF EXISTS {table_name} CASCADE"""
            conn = self.connect(database_url)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

        except Exception:
            
            return f"Unable to drop table {table_name}"


    def show_table(self, url=DATABASE_URL):    
        '''Show tables created in the given database.
        
        Args:
            query (Docstring): an sql query to be executed.
            database_url (str): a string containing connection database credentials.
        
        Returns:
            Show the given tables or returns a string indicating unable to show the tables.
        '''
        query = ("""SELECT table_name FROM information_schema.tables
                 WHERE table_schema = 'public'""")
        try:
            connection = self.connect(url)
            cursor = connection.cursor()
            cursor.execute( query)
            tables = cursor.fetchall()

            for table in tables:
                print (table)
        except:
            return 'connection failed'




if __name__ == "__main__":
    db = PostgresConfig()
    # print(db.connect(DATABASE_URL))
    # print(db.create_database('db_one'))
    # print(db.drop_database('db_one'))
    # print(db.close())
    # create_table_query = """CREATE TABLE IF NOT EXISTS test_table (
    # table_id serial PRIMARY KEY NOT NULL,
    # table_number int NOT NULL,
    # table_info character varying(1000),
    # date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    # )"""
    # print(db.create_table(create_table_query, DATABASE_URL))
    # table_name = 'test_table'
    # print(db.drop_table(table_name, DATABASE_URL))
    print (db.show_table())