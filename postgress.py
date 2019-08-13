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
                print('Database connection close')

if __name__ == '__main__':
    a = PostgresDb
    a.connect()