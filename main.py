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
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.close
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return 'success'        
    
    def session():
        pass
    
    def create_database():
        pass
    
    def status():
        pass
    
    def cursor():
        """
        Create a cursor area in memory where SQL statement
        are executed
        
        Arguments:
            query {[type]} -- [description]
        """
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        return 'success'
    
    def select_table(query):
        """
        Fetch and display records from database
        
        Arguments:
            query {[type]} -- [description]
        """
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return 'success'
    
    def create_table(query):
        """
        Create a table in a database
        
        Arguments:pi
            query {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()
        return 'success'        
    
    def insert_rows(query):
        """
        Funtion to insert and update records into a table
        
        Arguments:
            query {[type]} -- [description]
        """
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        return 'success'
        
    def show_table(query):
        """
        Function fetches and displays records ni the table
        
        Arguments:
            query {[SQL statement]} -- [description]
        """
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return 'success'
    
    def drop_table(query):
        pass
    
    def close():
        pass        
        
if __name__ == '__main__':
    a = PostgresDb
    a.connect()
    a.select_table("SELECT id, name, address, salary from COMPANY")
    a.create_table('''CREATE TABLE TEST (ID INT PRIMARY KEY NOT NULL,
            NAME    TEXT    NOT NULL,
            AGE     INT     NOT NULL,
            ADDRESS CHAR(50),
            SALARY  REAL);''')
    a.insert_rows("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    a.show_table("SELECT id, name, address, salary from COMPANY")