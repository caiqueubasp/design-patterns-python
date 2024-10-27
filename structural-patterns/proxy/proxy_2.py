from abc import ABCMeta, abstractmethod


# Interface
class Carteira(metaclass=ABCMeta):
    @abstractmethod
    def pagar(self):
        pass
    

# Objeto real
class Banco(Carteira):
    
    def __init__(self):
        self.cartao = None
        self.conta = None
        
    def __get_conta(self):
        self.conta = self.cartao
        
        return self.conta
    
    def __tem_saldo(self):
        print(f'{type(self).__name__} tem saldo')
        return True
    
    
    def set_cartao(self, cartao):
        self.cartao = cartao
        
    def pagar(self):
        if(self.__tem_saldo()):
            print(f'{type(self).__name__} pagou')
            return True
        else:
            print(f'{type(self).__name__} não pagou')
            return False
        
        
# Proxy

class CartaoDebito(Carteira):
    
    def __init__(self):
        self.banco = Banco()
        
    def pagar(self):
        cartao = input('Digite o número do cartão: ')
        self.banco.set_cartao(cartao)
        return self.banco.pagar()
    
    
    
# Cliente
class Cliente:
    
    def __init__(self):
        print(f'{type(self).__name__} quer pagar')
        self.cartao = CartaoDebito()
        self.comprei = None
        
    def fazer_pagamento(self):
        self.comprei = self.cartao.pagar()
        
    def __del__(self):
        if(self.comprei):
            print(f'{type(self).__name__} pagou')
        else:
            print(f'{type(self).__name__} não pagou')
            
            
if(__name__ == '__main__'):
    cliente = Cliente()
    cliente.fazer_pagamento()