from database import Postgres
import psycopg2
from config import config

class PostgresDb(Postgres):
    """
    COnnect to the postgresql database
    
    Arguments:
        Postgres {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    def connect():
        conn = None
        try:
            #Read connection params from db.ini
            params = config()
            
            #connect to psql
            print('Connecting to Posgress..../')
            conn = psycopg2.connect(**params)
            #Create cursor
            cur = conn.cursor()
        #Execute a statement
            print('Postgresql database version: ')
            cur.execute('SELECT Version()')
            
            db_version = cur.fetchone()
            print(db_version)
            #Close communication with postgress
            cur.close
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection close')

if __name__ == '__main__':
    a = PostgresDb
    a.connect()
    
    
    
    # def connect_db(self, db_url):
    #     """
    #     Connect to a postgress database
    #     """
    #     try:
    #         self.conn = psycopg2.connect(db_url)
    #         cur = conn.cursor()
    #     except Exception as error:
    #         print(error)

    # def create_database(self, query):
    #     """
    #     Create a database
    #     """
    #     self.cur.execute(query)
    #     self.conn.commit()
    
    # def cursor(self, conn):
    #     """
    #     Create a cursor
    #     """
    #     self.cur = self.conn.cursor()

    # def select_table(Postgres):
    #     pass

    # def create_table(self, query):
    #     """
    #     Create table
    #     """
    #     try:
    #         self.cur.execute(query)
    #         self.cur.close
    #         self.conn.commit()
    #     except Exception as error:
    #         print(error)
    
    # def insert_rows(self, query):
    #     self.cur.execute(query)

    # def show_table(Postgres):
    #     """
    #     Shows all data in table
    #     """
        
    # def drop_table(Postgres):
    #     """
    #     Deletes all tables
    #     """
        
    # def close_table(Postgres):
    #     pass