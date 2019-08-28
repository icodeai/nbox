from abc import ABC, abstractmethod


class Postgres(ABC):

    @abstractmethod
    def connect(self,database_url):
        pass

    # @abstractmethod
    def session(self):
        autocommit = True
        pass

    @abstractmethod
    def create_database(self, database_name):
        pass

    # @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self):
        pass

    # @abstractmethod
    def select_table(self,query):
        pass

    @abstractmethod
    def create_table(self, query, database_url):
        pass

    # @abstractmethod
    def insert_rows(self,query):
        pass

    @abstractmethod
    def show_table(self,query):
        pass

    @abstractmethod
    def drop_table(self, table_name, database_url):
        pass

    @abstractmethod
    def close(self):
        pass
