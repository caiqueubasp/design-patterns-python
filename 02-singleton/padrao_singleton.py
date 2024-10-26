
class Singleton(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print('Criando nova instância...{}'.format(cls.instance))
        return cls.instance
    
    
    
    
    
s1 = Singleton()
print(f'Instancia s1: {id(s1)}')

s2 = Singleton()
print(f'Instancia s2: {id(s2)}')