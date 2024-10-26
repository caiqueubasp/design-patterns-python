import sqlite3

class SingletonMeta(type):
    
    __instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
    
class Database(metaclass=SingletonMeta):
    
    connection = None
    
    def connect(self):
        if self.connection is None:
            print('Nao existe conexao com o banco de dados... Cirando uma nova conexao...')
            self.connection = sqlite3.connect('data.db')
            self.cursor = self.connection.cursor()
        return self.cursor
    
    
db1 = Database().connect()
db2 = Database().connect()