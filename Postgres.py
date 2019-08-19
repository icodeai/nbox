import os 
import psycopg2

class Postgresdb(Postgres):

    def __init__(self):
        #initializes the Postgresdb class
        self.connection = None
        self.cursordb = None

    def connect(self, user, password, host, port, database):
        '''connects to Postgresdb
        Args:
            user
            password
            host
            port
            database
        returns:
            the connection parameters if the connection is successful
        '''
        try:
            self.connection = psycopg2.connect(user, password, host, port,database)
            self.cursordb = self.connection.cursor()

            return self.connection.get_dsn_parameters()

        except (Exception, psycopg2.Error) as error :    
            print ("Error while connecting to PostgreSQL", error)

    def session(self):
        # autocommit = True
        pass
    
    def create_database(self):
        pass

    def status(self):
        #shows if there is a connection to the database
        return self.connection.status()

    def cursor(self,query):
        #uses cursor to execue a query
      return  self.cursordb.execute(query) 

    def select_table(self,query):
        #requires a sql statement to select required table
        try:
            self.cursor(query)
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