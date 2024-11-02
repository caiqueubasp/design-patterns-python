from abc import ABCMeta, abstractmethod

class Viagem(metaclass=ABCMeta):
    
    @abstractmethod
    def ida(self):
        pass
    
    @abstractmethod
    def dia_1(self):
        pass
    
    @abstractmethod
    def dia_2(self):
        pass
    
    @abstractmethod
    def dia_3(self):
        pass
    
    @abstractmethod
    def retorno(self):
        pass
    
    def itinerario(self):
        self.ida()
        self.dia_1()
        self.dia_2()
        self.dia_3()
        self.retorno()
        
        
    
    
class ViagemVeneza(Viagem):
    
    def ida(self):
        print("Viagem de aviao")
        
    def dia_1(self):
        print('visita a basilica de Sao Marcos')
        
    def dia_2(self):
        print('Visitar o Palacio Doge')
        
    def dia_3(self):
        print('roteiro gastronomico')
        
    def retorno(self):
        print('Viagem de aviao')
        
        
class ViagemMalvinas(Viagem):
    
    def ida(self):
        print("Viagem de onibus")
        
    def dia_1(self):
        print('Fazer atividades aquaticas')
        
    def dia_2(self):
        print('Mergulho no coral')
        
    def dia_3(self):
        print('Comer e aproveitar a vida')
        
    def retorno(self):
        print('Viagem de aviao')
        
        
class GeekTravel:
    
    def preparar_viagem(self):
        
        opcao = input('Qual Pacote voce deseja: Veneza ou Malvinas: ')
        
        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
            
        elif opcao == 'Malvinas':
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print('Opcao invalida')
            
            

agencia = GeekTravel()
agencia.preparar_viagem()    
        