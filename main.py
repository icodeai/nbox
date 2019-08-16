from database import Postgres
import psycopg2

class DataBase(Postgres):

    def __init__(self):
        self.conn, self.cur = None

    def connect(self,user, password, host, port, database):
        """
        This method creates a connection to the Postgres database.
        """
        try:
            self.conn = psycopg2.connect(user = user, password = password, database = database, host = host, port = port)
            print("Connection established")
        except:
            print("Connection not established")
            self.conn = "Connection not established"
        return self.conn

    def session(self):
        autocommit = True
        self.conn.set_session(autocommit=autocommit)

    def create_database(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            print("An error occurred while creating the Database")

    def status(self):
        pass

    def cursor(self):
        try:
            if (self.conn):
                self.cur = self.conn.cursor()
        except:
            self.cur= "An error occurred while creating the cursor"
        return self.cur

    def select_table(self, query):
        self.cur.execute(query)
        rows= self.cur.fetchall()
        return rows

    def create_table(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def insert_rows(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def show_table(self, query):
        self.cur.execute(query)
        rows= self.cur.fetchall()
        return rows

    def drop_table(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        if (self.conn):
            self.cur.close()
            self.conn.close()
        else:
            print("No existing connection")