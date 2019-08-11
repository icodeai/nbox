import os
from abc import ABC, abstractmethod

import psycopg2 as p

DATABASE_URL = os.getenv('DATABASE_URL')

class Postgres(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def session(self,):
        autocommit = True
        pass

    @abstractmethod
    def create_database(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self,query):
        pass

    @abstractmethod
    def select_table(self,query):
        pass

    @abstractmethod
    def create_table(self,query):
        pass

    @abstractmethod
    def insert_rows(self,query):
        pass

    @abstractmethod
    def show_table(self,query):
        pass

    @abstractmethod
    def drop_table(self,query):
        pass

    @abstractmethod
    def close(self):
        pass


class PostgresConfig(Postgres):

    def connect(self, db_url):
        conn = p.connect(db_url)
        return conn
    
   
    def session(self):
        autocommit = True
        pass

    def create_database(self, database_name):

        try:
            query = """CREATE DATABASE database_name='{0}';""".format(
                database_name)
                
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(DATABASE_URL).commit()

        except (Exception, p.Error)as e:
            print("failed to create databse" + e)
        
        finally:
            
            if self.connect(DATABASE_URL):
                self.close()  

    
    def status(self):
        pass

    
    def cursor(self):

        conn = self.connect(DATABASE_URL)
        cursor = conn.cursor()
        return cursor

    
    def select_table(self,query):
        
        try:
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(DATABASE_URL).commit()

        except (Exception, p.Error)as e:
            print(e)
        
        finally:
            
            if self.connect(DATABASE_URL):
                self.close()  

    
    def create_table(self,query):
         
        try:
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(DATABASE_URL).commit()

        except (Exception, p.Error)as e:
            print(e)
        
        finally:
            
            if self.connect(DATABASE_URL):
                self.close()    

    
    def insert_rows(self,query):
        
        try:
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(DATABASE_URL).commit()

        except (Exception, p.Error)as e:
            print(e)
        
        finally:
            
            if self.connect(DATABASE_URL):
                self.close()  

    
    def show_table(self,table_name):
        
        try:
            query = """SELECT * from '{0}' """.format(
                table_name)
            cursor = self.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data

        except (Exception, p.Error)as e:
            print(e)
        
    def close(self):

        self.cursor().close()
        self.connect(DATABASE_URL).close()
        
    
    def drop_table(self,table_name):
        
        try:
            query = """DROP TABLE IF EXISTS '{0}' CASCADE""".format(table_name)
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(DATABASE_URL).commit()

        except (Exception, p.Error)as e:
            print(e)
        
        finally:
            
            if self.connect(DATABASE_URL):
                self.close()  
