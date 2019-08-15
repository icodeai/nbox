from abc import (ABC, abstractmethod)
import psycopg2
from psycopg2 import Error



class Postgres(ABC):

    @abstractmethod
    def connect(self,database_url):
        pass

    # @abstractmethod
    def session(self,):
        autocommit = True
        pass

    # @abstractmethod
    def create_database(self):
        pass

    # @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self):
        pass

    # @abstractmethod
    def select_table(self,query):
        pass

    # @abstractmethod
    def create_table(self,query):
        pass

    # @abstractmethod
    def insert_rows(self,query):
        pass

    # @abstractmethod
    def show_table(self,query):
        pass

    # @abstractmethod
    def drop_table(self,query):
        pass

    # @abstractmethod
    def close(self):
        pass
    
    class Database(Postgres):
    def __init__(self):
        self.connection
        self.cur
    
    def connect(self, user, password, host, port, database):
        
        try:
            self.connection = psycopg2.connect(user = "admin", password = "admin", host = "127.0.0.1", port = "5432", database = "postgres_db")
                             
            self.cursor = connection.cursor()

            return self.cursor
        
        except (Exception, psycopg2.Error) as error :
            return "Error while connecting to PostgreSQL", error

    
    def session(self):
        autocommit = True
        self.connection.set_session(autocommit=autocommit)

    
    def create_database(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error)as error:
            print("Error while creating the Database")

   
    def status():
        pass

    
    def cursor(query):
        pass

    
    def select_table(self, query):
        self.cur.execute(query)
        row = self.cur.fetchall()
        return row
        

   
    def create_table(self, query):
        try:
            create_table_query = """Create table"""

            self.cur.execute(create_table_query)
            self.connection.commit()
        
        except (Exception, psycopg2.Error)as error:
            print("Error while creating the table")
   
    def insert_rows(self, query):

        try:
            cursor = self.cursor()
            cursor.execute(query)
            self.connection.commit()

        except (Exception, psycopg2.Error)as error:
            print("Error while creating the Database")

    def show_table(self, query):

        try:
            cursor = self.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

        except (Exception, psycopg2.Error)as error:
            print("Error while fetching rows")
        

    
    def drop_table(self, query):
        
        try:
            self.cur.execute(query)
            self.connection.commit()

        except (Exception, psycopg2.Error)as error:
            print("Error while droping the table")

    
    def close(self):
        self.cursor().close()
        self.connection.close()
        
