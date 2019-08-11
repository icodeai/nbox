from abc import (ABC, abstractmethod)
import psycopg2


class Postgres(ABC):

    @abstractmethod
    def connect(user, password, host, port, database):
        pass

    @abstractmethod
    def session():
        autocommit = True
        pass


    @abstractmethod
    def create_database():
        pass

    @abstractmethod
    def status():
        pass

    @abstractmethod
    def cursor(query):
        pass

    @abstractmethod
    def select_table(query):
        pass


    @abstractmethod
    def create_table(query):
        pass

    @abstractmethod
    def insert_rows(query):
        pass

    @abstractmethod
    def show_table(query):
        pass

    @abstractmethod
    def drop_table(query):
        pass

    @abstractmethod
    def close():
        pass

class PostgresDb(Postcgres):
    pass

    def connect_db(Postgres):
        pass

    def check_session(Postgres):
        pass

    def createdatabase(Postgres):
        pass

    def cursor(Postgres):
        pass

    def select_table(Postgres):
        pass

    def create_table(Postgres):
        pass

    def insert_ows(Postgres):
        pass

    def show_table(Postgres):
        pass

    def drop_table(Postgres):
        pass

    def close_table(Postgres):
        pass

