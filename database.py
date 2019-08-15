from abc import (ABC, abstractmethod)
import psycopg2


class Postgres(ABC):

    @abstractmethod
    def connect(self,db_url):
        pass

    # @abstractmethod
    # def session():
    #     autocommit = True
    #     pass

    # @abstractmethod
    # def create_database():
    #     pass

    # @abstractmethod
    # def status():
    #     pass

    @abstractmethod
    def cursor(self):
        pass

    # @abstractmethod
    # def select_table(query):
    #     pass

    # @abstractmethod
    # def create_table(query):
    #     pass

    # @abstractmethod
    # def insert_rows(query):
    #     pass

    # @abstractmethod
    # def show_table(query):
    #     pass

    # @abstractmethod
    # def drop_table(query):
    #     pass

    # @abstractmethod
    # def close():
    #     pass
