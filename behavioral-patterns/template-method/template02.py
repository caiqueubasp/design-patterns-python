from abc import ABCMeta, abstractmethod

class ClasseAbstrata(metaclass=ABCMeta):
    
    @abstractmethod
    def metodo1(self):
        pass
    
    @abstractmethod
    def metodo2(self):
        pass
    
    def template_method(self):
        print("Definindo o algorithm com o template method")
        self.metodo1()
        self.metodo2()
        
        
class ClasseConcreta1(ClasseAbstrata):
    
    def metodo1(self):
        print("Implementação do método 1 da classe concreta 1")
        
    def metodo2(self):
        print("Implementação do método 2 da classe concreta 1")
        
        
        
class Cliente:
    
    def main(self):
        concreta1 = ClasseConcreta1()
        concreta1.template_method()
        
        

cliente = Cliente()
cliente.main()
