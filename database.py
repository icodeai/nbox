import psycopg2 as pc


class DataBaseConnection(Postgres):

    
    def connect(self,user, password, host, port, database):
        '''This methode creates a user connection to the database.

        Parameters:
            user -- The username you use to work with PostgreSQL, The default username for the PostgreSQL database is Postgres. 
            password --  Password is given by the user at the time of installing the PostgreSQL.
            host --   Host is the server name or Ip address on which PostgreSQL is running. if you are running on localhost, then you can use localhost, or it’s IP i.e., 127.0.0.0.
            port -- connection port number.
            database --  Database name to which you want to connect.

        Returns: None
        '''
        try:

            self.con = pc.connect(user = user, password = password,host = host, port = port, database = database)
            print('Database connected')
        except Exception:
            print('Could not connect to database')

    def cursor(self,query):
        '''Allows code to execute PostgreSQL command in a database session.

        Parameters:
            query -- syntax to retrieve data from a database.
        '''
        self.cur = self.con.cursor(query)

    def session(self):
        '''This method ensures that a query or action will be executed in its own.'''
        self.cur.autocommit = True

    def create_database(self):
        '''Creates a database using a query and the name of  the database.'''
        self.cur.execute("CREATE DATABASE %s;" % self.database)

    def status(self):
        pass

    def create_table(self,query):
        '''Creates a table inside the database.

        Parameters:
            query -- syntax to create  a table ie SELECT FROM TABLENAME(FIELDS).

        Returns: a new table
        '''
        self.cur.execute(query)
        self.con.commit()

    def select_table(self,query):
        '''Selects a specific table from the database.

        Parameters:
            query -- algorithim Extracts the table from the database. ie SELECT * FROM TABLENAME().

        Retunrns: a selected table.
        '''
        self.cur.execute(query)
        self.con.commit()

    def insert_rows(self,query,values):
        '''Inserts a new observation into the table.

        Parameters:
            query -- syntax to insert new data into the table. ie INSERT INTO TABLENAME()
            values -- The new values or rows to be inseted.

        Returns: An updated table.
        '''
        try:
            self.cur.execute(query(values))
            self.con.commit()
        except Exception as e:
            print(e)

    def show_table(self,query):
        '''Traverses through the table and shows its contents.

        Parameters:
            query -- syntaxs to fetch data table.

        Return: The table contents.
        '''
        self.cur(query)
        table = self.cur.fetchall()

    def drop_table(self,query):
        '''Deletes a table from the database.

        Parameters:
            query -- synatx to drop the table from the database. ie DROP TABLENAME().

        Returns: An updated database
        '''
        try:
                
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print(e)
    def close(self):
        '''Closes a database connection.

        Returns: A closed connection to a database.
        '''
        if self.con:
            self.con.close()
            print('Connection closed')
        else:
            print('No connection to close')




    

