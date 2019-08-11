from abc import (ABC, abstractmethod)
import psycopg2


class Postgres(ABC):

    @abstractmethod
    def connect(self,user, password, host, port, database):
        try:
            self.conn = psycopg2.connect(user = user, password = password, database = database, host = host, port = port)
            print("Connection established")
        except:
            print("Connection not established")
            self.conn = "Connection not established"
        return self.conn

    @abstractmethod
    def session(self):
        autocommit = True
        self.conn.set_session(autocommit=autocommit)

    @abstractmethod
    def create_database(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            print("An error occurred while creating the Database")

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self):
        try:
            if (self.conn):
                self.cur = self.conn.cursor()
        except:
            self.cur= "An error occurred while creating the cursor"
        return self.cur

    @abstractmethod
    def select_table(self, query):
        self.cur.execute(query)
        rows= self.cur.fetchall()
        return rows

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
        if (self.conn):
            self.cur.close()
            self.conn.close()
        else:
            print("No existing connection")