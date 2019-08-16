from abc import ABC, abstractmethod


class Postgres(ABC):

    @abstractmethod
    def connect(self,user, password, host, port, database):
        pass
