

class University(type):
    
    def __call__(cls, *args, **kwargs):
        print(f'==== Esses sao os args: {args}')
        return type.__call__(cls, *args, **kwargs)
    
    

class Geek(metaclass=University):
    
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        
        
        
g1 = Geek(17, 18)
print(g1)
g2 = Geek(19, 20)
print(g2)