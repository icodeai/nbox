from abc import (ABC, abstractmethod)
import psycopg2


class Postgres(ABC):

    @abstractmethod
    def connect(self, user, password, host, port, database):
        pass

    @abstractmethod
    def session(self):
        autocommit = True
        pass

    @abstractmethod
    def create_database(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self, query):
        pass

    @abstractmethod
    def select_table(self, query):
        pass

    @abstractmethod
    def create_table(self, query):
        pass

    @abstractmethod
    def insert_rows(self, query):
        pass

    @abstractmethod
    def show_table(self, query):
        pass

    @abstractmethod
    def drop_table(self, query):
        pass

    @abstractmethod
    def close(self):
        pass
    