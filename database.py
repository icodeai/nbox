from abc import (ABC, abstractmethod)
import psycopg2


class Postgres(ABC):

    @abstractmethod
    def connect(self,user, password, host, port, database):
        self.conn= psycopg2.connect(user = user, password = password, database = database, host = host, port = port)
        return self.conn

    @abstractmethod
    def session(self):
        autocommit = True
        pass

    @abstractmethod
    def create_database(self, query):
        self.cur.execute(query)
        self.conn.commit()

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self, query):
        self.cur = self.conn.cursor()
        return self.cur

    @abstractmethod
    def select_table(self, query):
        self.cur.execute(query)
        pass

    @abstractmethod
    def create_table(self, query):
        self.cur.execute(query)
        self.conn.commit()

    @abstractmethod
    def insert_rows(self, query):
        self.cur.execute(query)
        self.conn.commit()

    @abstractmethod
    def show_table(self, query):
        self.cur.execute(query)
        rows= self.cur.fetchall()
        return rows

    @abstractmethod
    def drop_table(self, query):
        self.cur.execute(query)
        self.conn.commit()

    @abstractmethod
    def close(self):
        self.conn.close()