import pickle

class DAO():
    def __init__(self, data_source):
        self.__data_source = data_source
        self.__cache = {}

        try:
            self.__load()
        except:
            self.__dump()
    
    @property
    def data_source(self):
        return self.__data_source
    
    def __dump(self):
        with open(self.data_source, 'wb') as f:
            pickle.dump(self.__cache, f)
    
    def __load(self):
        with open(self.data_source, 'rb') as f:
            self.__cache = pickle.load(f)
    
    def add(self, chave, objeto):
        self.__cache[chave] = objeto
        self.__dump()
    
    def get(self, chave):
        self.__load()
        if chave in self.__cache:
            return self.__cache[chave]
        else:
            return None
    
    def remove(self, chave):
        self.__load()
        if chave in self.__cache:
            del self.__cache[chave]
            self.__dump()

    def get_all(self):
        self.__load()
        return self.__cache
