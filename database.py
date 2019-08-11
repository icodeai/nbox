from abc import (ABC, abstractmethod)
import psycopg2


class Postgres(ABC):

    @abstractmethod
    def connect(user, password, host, port, database):
        pass

    @abstractmethod
    def session():
        autocommit = True
        pass


    @abstractmethod
    def create_database():
        pass

    @abstractmethod
    def status():
        pass

    @abstractmethod
    def cursor(query):
        pass

    @abstractmethod
    def select_table(query):
        pass


    @abstractmethod
    def create_table(query):
        pass

    @abstractmethod
    def insert_rows(query):
        pass

    @abstractmethod
    def show_table(query):
        pass

    @abstractmethod
    def drop_table(query):
        pass

    @abstractmethod
    def close():
        pass

class PostgresDb(Postcgres):
    
    def connect_db(self, db_url):
        """
        Connect to a postgress database
        """
        try:
            self.conn = psycopg2.connect(db_url)
            cur = conn.cursor()
        except Exception as error:
            print(error)

    def create_database(self, query):
        """
        Create a database
        """
        self.cur.execute(query)
        self.conn.commit()
    
    def cursor(self, conn):
        """
        Create a cursor
        """
        self.cur = self.conn.cursor()

    def select_table(Postgres):
        pass

    def create_table(self, query):
        self.cur.execute(query)
        

    def insert_rows(self, query):
        self.cur.execute(query)

    def show_table(Postgres):
        """
        Shows all data in table
        """
        
    def drop_table(Postgres):
        """
        Deletes all tables
        """
        
    def close_table(Postgres):
        pass

