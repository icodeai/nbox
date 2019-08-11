from abc import (ABC, abstractmethod)
import psycopg2 as p


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

class DatabasePostgres(Postgres):

    def __init__(self):
        self.connection = None

    
    def connect(self, user, password, host, port, database):
        try:
            self.connection = p.connect(user="user", password = "password", host ="host", port = "port", database = "database_name")
            print("Connection to PostgreSQL established")
        except (Exception, p.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        return self.connection


    
    def session(self):
        self.connection.set_session(autocommit=True)

    def create_database(self):
        pass

   
    def status(self):
        if self.connection:
            print("Connection to PostgreSQL established")
        else:
            print("Error while connecting to PostgreSQL")


    def cursor(self):
        self.cur = self.connection.cursor()


    def select_table(self, query):
        self.cur.execute(query)
        self.connection.commit()
        

    def create_table(self, query):
        self.cur.execute(query)
        self.connection.commit()

    def insert_rows(self, update_query):
        self.cur.execute(update_query)
        self.connection.commit()

    def show_table(self,query):
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        self.connection.commit()
        return all_rows


    def drop_table(self, query):
        self.cur.execute(query)
        self.connection.commit()

    def close(self):
        if (self.connection):
            self.connection.close()
            self.cur.close()
            print("PostgreSQL connection is closed")
        else:
            print("No connection to PostgreSQL exists")
