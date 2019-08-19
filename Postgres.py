import os 
import psycopg2
from database import Postgres

#env variable stored in local machine
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')

class Postgresdb(Postgres):

    def __init__(self):
        #initializes the Postgresdb class
        self.connection = None
        self.cursordb = None

    def connect(self,user,password,host,port,database):
        '''connects to Postgresdb
        Args:
            dbParameters(str): parameters required to connect to the db
        Returns:
            the connection successful if the connection is successful  

            error if unsuccessful 
        '''
        try:
            self.connection = psycopg2.connect(user,password,host,port,database)
            self.cursordb = self.connection.cursor()
            return 'connection successful'

        except (Exception, psycopg2.Error) as error :    
            return error

if __name__ == "__main__":
    db = Postgresdb()
    print(db.connect(dbParameters))