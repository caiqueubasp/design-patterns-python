from abc import ABCMeta, abstractmethod

class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        pass

    @abstractmethod
    def compilar_obj(self):
        pass

    @abstractmethod
    def executar(self):
        pass
    
    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_obj()
        self.executar()
        
        
class CompiladorIOS(Compilador):
    
    def coletar_fonte(self):
        print("Coletando fonte para iOS")
        
    def compilar_obj(self):
        print("Compilando o código para iOS")
        
    def executar(self):
        print("Executando o código iOS")
        
        
class CompiladorAndroid(Compilador):
    
    def coletar_fonte(self):
        print("Coletando fonte para Android")
        
    def compilar_obj(self):
        print("Compilando o código para Android")
        
    def executar(self):
        print("Executando o código Android")
        
        
        
ios = CompiladorIOS()
ios.compilar_e_executar()

android = CompiladorAndroid()
android.compilar_e_executar()