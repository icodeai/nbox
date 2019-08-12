import psycopg2
from psycopg2 import Error
from .database import Postgres


class PostgresDB(Postgres):
    def __init__(self):
        self.conn = None
        self.cur = None
    
    def connect(self, user, password, host, port, database):
        """
        This method opens a connection to the PostgreSQL database. 
        If database is opened successfully, it returns a connection object."""

        try:
            self.conn = psycopg2.connect(user=user,
                                        password=password, 
                                        host=host, 
                                        port=port, 
                                        database=database)
            # create a cursor
            self.cur = self.conn.cursor()
            print("Connected successfully")

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        return self.conn
    

    def session(self):
        autocommit = True
        self.conn.set_session(autocommit=autocommit)
        
        
    def create_database(self, query):
        """Create a new database
        """
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            pass


    def status(self):
        """Display the connection status and data source name params
        """
        if (self.conn):
            # Print PostgreSQL Connection properties
            print (self.conn.get_dsn_parameters(),"\n")

            # create a cursor
            self.cur = self.conn.cursor()

            # Query the PostgreSQL version
            self.cur.execute("SELECT version();")

            # Fetches the next row of the query result set, 
            # returning a single sequence, or None when no more data is available
            record = self.cur.fetchone()
            print("You are connected to - ", record,"\n")
        else:
            print("No existing existing connection")

    def cursor(self):
        """
        This method creates a cursor which will be used throughout
        of the database programming with Python."""
        try:
            if (self.conn):
                self.cur = self.conn.cursor()
        except:
            pass
        return self.cur
        

    def select_table(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def create_table(self, query):
        """
        create a table in the PostgreSQL database"""
    
        try:
            self.cur.execute(query)
            self.conn.commit()
            print("Table created successfully in PostgreSQL ")
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table", error)


    def insert_rows(self, query):
        """
        Insert records into a table"""
        self.cur.execute(query)
        self.conn.commit()

    def show_table(self, query):
        """
        Display all records in a table"""
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def drop_table(self, query):
        """Delete a table from the database"""
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        """
        This method closes the database connection."""

        if (self.conn):
            self.cur.close()
            self.conn.close()
            print("PostgreSQL connection is closed")
        else:
            print("No existing connection")
