from abc import ABC, abstractmethod


class Postgres(ABC):

    @abstractmethod
    def connect(self, user, password, host, port, database):
        """Connect to a  postgres database 
        
        Arguments:
            user {str} -- The username for the Postgres database
            password {str,int} -- The password for the Postgres database
            host {str,int} -- The server name or the IP address on which Postgres is running on
            port {int} -- The port that the postgres server is running on
            database {str} -- The name of the Postgres database to be connected
        """
        try:
            self.connection = psycopg2.connect(user, password, host, port, database)
            self.cursor = self.connection.cursor()
        except(Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    @abstractmethod
    def session(self):
        """This method sets the session of the Postgres database
        """
        self.connection.set_session(autocommit=True)

    @abstractmethod
    def create_database(self, database):
        """Creates a postgres database
        """
        self.cursor.execute("CREATE DATABASE {];", format(self.db_name))

    @abstractmethod
    def status(self):
        """Checks the status of the database
        
        Returns:
            [str] -- The status of the database
        """
        return self.connection.status()

    @abstractmethod
    def cursor(self):
        """The cursor object used to execute the postgres queries
        
        Returns:
            [str] -- The cursor object
        """
        return self.connection.cursor()

    @abstractmethod
    def select_table(self, query):
        """Selects a table from the database
        
        Arguments:
            query {str} -- Command used to retrieve data from the selected table
        """
        self.cursor.fetchall(query)
        self.connection.commit()
       
    @abstractmethod
    def create_table(self, query):
        """Creates a table for the database
        """
        self.cursor.execute(query)
        self.connection.commit()
        print("Table created successfully in PostgreSQL")

    @abstractmethod
    def insert_rows(self, query):
        """Inserts rows into the database
        """
        self.cursor.executemany(query)
        self.connection.commit()

    @abstractmethod
    def show_table(self, query):
        """Shows all the data in the table
        """
        self.cursor.fetchall(query)
        self.connection.commit()

    @abstractmethod
    def drop_table(self, query):
        """Drops the selected table
        """
        self.cursor.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema, table_name")
        rows = self.cursor.fetchall()
        for row in rows:
            print("dropping table: ", row[1])
            self.cursor.execute("drop table " + row[1] + " cascade*-")
        
    @abstractmethod
    def close(self, connection):
        """Closes the database connection
        """
        self.connection.close()
        print("Database connection closed")
        
