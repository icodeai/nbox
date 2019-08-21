from database import Postgres
import psycopg2

class DataBase(Postgres):

    def __init__(self):
        self.conn, self.cur = None

    def connect(self,user, password, host, port, database):
        """
        This method creates a connection to the Postgres database.

        Parameters:
        -----------
        user: str
            The username of the account you want to connect with

        password: str
            The password for the account you want to connect to the database with
        
        host: str
            The name of the host

        port: int
            The port number of the database

        database: str
            The name of the database you want tp connect to

        Returns
        -------
        str:
             A confirmation of whether the connection has been established or not
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
        """
        This method creates a database.

        Parameters:
        -----------
        query: str
            The query that creates the database
        """
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
        """
        This method selects a table from a database given a defined query

        Parameters:
        -----------
        query: str
            The query that selects a table from the database

        Returns
        -------
            rows of the table selected
        """
        self.cur.execute(query)
        rows= self.cur.fetchall()
        return rows

    def create_table(self, query):
        """
        This method creates a table.

        Parameters:
        -----------
        query: str
            The query that creates the table
        """
        self.cur.execute(query)
        self.conn.commit()

    def insert_rows(self, query):
        """
        This method inserts rows in a given table

        Parameters:
        -----------
        query: str
            The query that inserts rows to a table
        """
        self.cur.execute(query)
        self.conn.commit()

    def show_table(self, query):
        """
        This method shows the table selected given a certain query.

        Parameters:
        -----------
        query: str
            The query that selects the table

        Returns:
            rows
        """
        self.cur.execute(query)
        rows= self.cur.fetchall()
        return rows

    def drop_table(self, query):
        """
        This method drops a table from the database.

        Parameters:
        -----------
        query: str
            The query that drops a table from the database
        """
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        """
        This method closes the cursor and the connection to the database if the exist.
        """
        if (self.conn):
            self.cur.close()
            self.conn.close()
        else:
            print("No existing connection")