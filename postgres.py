import psycopg2
import sys,os
from abc import ABC,abstractclass

class Postgresql(ABC):

    def __init__(self,username,password,hostname,port,database):
    """
    Utility for exploring and querying a database.
    Parameters
    -----------
    username: str
        Your username for the database
    password: str
        Your password for the database
    hostname: str
        Hostname your database is running on (i.e. "localhost", "10.20.1.248")
    port: int
        Port the database is running on. defaults to default port for db.
            portgres: 5432
     dbname: str
        Name of the database

    """
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.database = database
        self.schema = schema
        
        self.url = f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'

        self.conn = psycopg2.connect(database = self.url[1:])
        self.cursor = self.conn.cursor()
        

    @abstractmethod
    def session(self,schema_):
        self.conn.autocommit = True
        self.execute("SET search_path TO {}, public".format(self.schema))

        self.conn.close() 

    @abstractmethod
    def create_database(self, database):
        """
        Function to create database
        Parameters
        -----------   
        databasee name :str
        """
        try:
            self.cursor.execute("Create Database {}".format(self.database))
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)


    @abstractmethod
    def status(self):
        try:
            conn = psycopg2.connect(f'database={self.database} user={self.username} host={self.hostname} password={self.password}'
            conn.close()
            return True
        except:
            return False

    @abstractmethod
    def cursor(self):
            """
                returns the number of cursor calls attributed to SELECT, INSERT...
            """
        query = ""
        cur = self.conn.cursor()
        cur.execute(query)

        rowcount = cur.rowcount()
        self.conn.commit()
        cur.close()

        return rowcount

        
    @abstractmethod
    def select_table(self,table_name):
        """
        Select the table in your database's schema 
        Parameters
        -----------   
        table_name:str
        """

        query = "SELECT {0} from {1};".format(columns,table)
        return self.cursor.execute(query)

    @abstractmethod
    def create_table(self,table_name):
    ## function to create a table for the database.
    #
    #  @param table name for which to query.

        query = "CREATE TABLE {} ".format(self.table_name)
        return self.cursor.execute(query)

    @abstractmethod
    def insert_rows(self,table_name,data):
    """
    function to insert row of data into a database.
    
      @param table The database's table from which to query.
    
      @param rowdata which to insert
    
    """
        self.data = data
        query = "INSERT INTO {} VALUES {}".format(self.table_name,self.data)
        self.cursor.execute(query)

    @abstractmethod
    def show_table(self):
        """
         search through your database's schema for a table.
        Parameters
        -----------
         
           loop through cursor.fetchall()
        """

        query = "SELECT {} from {}".format(self.table_name,self.database)
        
        self.cursor.execute(query)

        for table in self.cursor.fetchall():
            print(table)

    @abstractmethod
    def drop_table(self):
        """
        removes the selected table from the database
        """
        query = "DROP TABLE {}".format(self.table_name)
        self.cursor.execute(query)

    @abstractmethod
    def close(self):
        #Function to close a datbase connection.

        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()










         





