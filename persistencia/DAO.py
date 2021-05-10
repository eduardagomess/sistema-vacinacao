import pickle
from abc import ABC, abstractmethod


class DAO(ABC):

    @abstractmethod
    def __init__(self, datasource: str = ''):
        self.__data_source = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__data_source, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__data_source, "rb"))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass
<<<<<<< HEAD

=======
>>>>>>> 1d0f923f2aa8d69428828e4ccb76c87bd5248d01
