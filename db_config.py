import os
import psycopg2
import psycopg2 as error
from database import Postgres


DB_LINK = os.environ.get('DB_LINK')


class Databaseconfig(Postgres):
    def __init__(self):
        self.connect = connect
    
    def connect(self, DB_LINK):

        """Connect to database

            ARGS: 
                Takes in the url to the databese credentials.

            RETURN: 
                    Returns connection successful or else error message.
        """
        
        
        try:
            connection = psycopg2.connect(DB_LINK) 
            return connection

        except (Exception, psycopg2.Error) as error :
            return "Error while connecting to PostgreSQL", error


    def cursor(self, DB_LINK):

        """create cursor object which iterates through the SQL statments

            ARGS:
                Takes DB_LINK as an argument.

            RETURN: 
                Returns cursor object.
            
        """

        connection = self.connect(DB_LINK)
        cursor = connection.cursor()
        return cursor


        