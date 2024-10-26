# Facade

class EventManager:
    
    def __init__(self):
        print('EventManager():: Vou organizar o evento para você. \n\n')
        
    def organizar(self):
        self.hotel = Hotel()
        self.hotel.reservar()
        
        self.passagem = Passagem()
        self.passagem.comprar()
        
        self.carro = Carro()
        self.carro.alugar()
        
        self.evento = Evento()
        self.evento.organizar()
        
    
# subsystem 1

class Hotel:
    
    def __init__(self):
        print('Hotel():: Vou reservar o hotel para você. \n')
    
    def __available(self):
        print('Hotel:: Quarto disponível. \n')
        return True
        
    def reservar(self):
        self.__available()
        print('Hotel:: Reserva feita com sucesso. \n')
        

# subsystem 2

class Passagem:
    
    def __init__(self):
        print('Passagem():: Vou comprar a passagem para você. \n')
    
    def __available(self):
        print('Passagem:: Passagem disponível. \n')
        return True
        
    def comprar(self):
        self.__available()
        print('Passagem:: Compra feita com sucesso. \n')
        

# subsystem 3

class Carro:
        
        def __init__(self):
            print('Carro():: Vou alugar um carro para você. \n')
        
        def __available(self):
            print('Carro:: Carro disponível. \n')
            return True
            
        def alugar(self):
            self.__available()
            print('Carro:: Aluguel feito com sucesso. \n')
            
            
# subsystem 4

class Evento:
    
    def __init__(self):
        print('Evento():: Vou organizar o evento para você. \n')
        
    def organizar(self):
        print('Evento:: Evento organizado com sucesso. \n')
        
        
# client

class Cliente:
    
    def __init__(self):
        print('Cliente():: Vou chamar o EventManager para organizar o evento para mim. \n')
        em = EventManager()
        em.organizar()
        
    def __del__(self):
        print('Cliente():: Tudo feito. \n')
        
        
if __name__ == '__main__':
    client = Cliente()
    
    