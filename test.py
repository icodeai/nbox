from database import Postgres
import psycopg2

class test(Postgres):


    def __init__(self):
        self.connection
        self.cursor
    
    
    def connect(self,user, password, host, port, database):
    """
         connects to the postregsql database

        Args:
            user  : username you use to work with PostgreSQL, The default username for the PostgreSQL database is Postgres
            password :  Password is given by the user at the time of installing the PostgreSQL.
            host  :  server name or Ip address on which PostgreSQL is running
            port :   Port on which PostgreSQL is running
            database : Database name to which you want to connect.
       
        Returns :
            Connection  to the database 

    """    
        try:
            #pass
         self.connection =psycopg2.connect(user, password, host, port, database)
         self.cursor = self.connection.cursor()
         return self.connection
        except (Exception, psycopg2.Error) as error :
           print ("Error while connecting to PostgreSQL", error)

    def session():
    """

    """    
        try:
           # pass
        except (Exception, psycopg2.Error) as error :
            pass
    def create_database():
    """
        create a database
    """  
        try:
           # pass

        except  (Exception, psycopg2.Error) as error :
            pass  

    def status():
    """
     Current status of  the connection
    """
        try:
            #pass
            return self.connection.status
        except  (Exception, psycopg2.Error) as error :
            pass    

    def cursor(query):
    """
        Return the cursor
    """
        try:
            #pass
            return self.cursor
        except (Exception, psycopg2.Error) as error :
            pass     

    def select_table(query):
    """
        select a table
    """
        try:
            #pass
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            pass    

    def create_table(query):
    """
        Create the table
    """
        try:
            #pass
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            pass    

    def insert_rows(query):
    """
        insert rows in the table
    """
        try:
            #pass
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            pass    


    def show_table(query):
    """
        show the current table
    """
        try:
            #pass
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            pass    

    def drop_table(query):
    """
        drop a table from the database
    """
        try:
            #pass
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            pass    

    def close(connection):
    """
        close the connection to database
    """
        try:
            #pass
            self.connection.close()
        except (Exception, psycopg2.Error) as error :
            pass        