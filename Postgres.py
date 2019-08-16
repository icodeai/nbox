
import psycopg2
from database import Postgres

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

if __name__ == "__main__":
    db = Postgresdb()
    print(db.connect())