from database import Postgres
import psycopg2
from config import config

class ConnectToDb():
    pass

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
            params = config()
            print('Connecting to Posgress..../')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            print('Postgresql database version: ')
            cur.execute('SELECT Version()')
            db_version = cur.fetchone()
            print(db_version)
            cur.close
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed')
                
    
    def create_table(query):
        """
        Function to create a table in an already existing database
        """
        conn = None
        try:
            params = config()
            print('Connecting to database...')
            conn = psycopg2.connect(**params)
            print('Connection to database succesful')
            cur = conn.cursor()
            cur.execute(query)
            print('Table created succesfully')
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Connection closed')

            
        
if __name__ == '__main__':
    a = PostgresDb
    a.connect()
    a.create_table()