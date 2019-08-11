from abc import (ABC, abstractmethod)
import psycopg2 as pc


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


class DataBaseConnection(Postgres):

    def connect(self,user, password, host, port, database):
        try:

            self.con = pc.connect(user = user, password = password,host = host, port = port, database = database)
            print('Database connected')
        except Exception:
            print('Could not connect to database')

    def cursor(self,query):
        self.cur = self.con.cursor(query)

    def session(self):
        self.cur.autocommit = True

    def create_database(self):
        self.cur.execute("CREATE DATABASE %s;" % self.database)

    def status(self):
        pass

    def create_table(self,query):
        self.cur.execute(query)
        self.con.commit()

    def select_table(self,query,):
        self.cur.execute(query)
        self.con.commit()

    def insert_rows(self,query,values):
        self.cur.execute(query(values))
        self.con.commit()

    def show_table(self,query):
        self.cur(query)
        table = self.cur.fetchall()

    def drop_table(self,query):
        self.cur.execute(query)
        self.con.commit()
    def close(self):
        if self.con:
            self.con.close()
            print('Connection closed')
        else:
            print('No connection to close')




    

