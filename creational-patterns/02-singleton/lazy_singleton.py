


class Lazy:
    
    __instance = None
    
    def __init__(self):
        if not Lazy.__instance:
            print('Criando instância...')
        else:
            print('Instância já criada...', self.get_instance())
            
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Lazy()
        return cls.__instance
    
    
    
l1 = Lazy() # A classe é inicializada, mas o objeto não é criado
print(f'Objeto craido: {Lazy.get_instance()}')
l2 = Lazy.get_instance() # O instancia é criado
