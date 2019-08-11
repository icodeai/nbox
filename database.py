from abc import (ABC, abstractmethod)
import psycopg2


class databaseall(ABC):

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



class Postgres(database):

    def __init__(self):
        self.connection = None
        self.cursordb

    def connect(self, user, password, host, port, database):
        try:
            self.connection = psycopg2.connect(user, password, host, port,database)
            self.cursordb = self.connection.cursor()
            #connection properties
            print ( self.connection.get_dsn_parameters(),"\n")
        
        except (Exception, psycopg2.Error) as error :    
            print ("Error while connecting to PostgreSQL", error)

    def session(self):
        autocommit = True
        pass
    
    def create_database(self):
        pass

    def status(self):
        #shows if there is a connection to the database
        if self.connection:
            print("connection exists")
        else:
            print("no connection")

    def cursor(self,query):
        #uses cursor to execue a query
       self.cursordb.execute(query) 

    def select_table(self,query):
        #requires a sql statement to select required table
        try:
            self.cursordb(query)
            table = self.cursordb.fetchall()
            for row in table:
                print(row)

        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)

    def create_table(self,query):
        #requires an sql statement to create required table
        self.cursordb.execute(query)
        self.connection.commit()

    def insert_rows(self,query,row_data):
        #inserts a single row ,query and row data specified as arguments
        try:
            self.cursordb.execute(query, row_data)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
                  print("Failed to insert row ", error)
    
    def show_table(self,query):
        #requires an show table sql statement
        self.cursordb.execute(query)
        return self.cursordb.fetchall()

    def drop_table(self,query):
        self.cursordb.execute(query)
        self.connection.commit()

    def close(self):
        if (self.connection):
            self.cursordb.close()
            self.connection.close()
        else:
            print("no connection exists currently")