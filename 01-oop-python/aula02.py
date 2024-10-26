from datetime import datetime

class Pessoa:
    def __init__(self: object, nome: str):
        self.nome = nome
        self.nascimento = datetime.now()

    def __str__(self: object):
        return self.nome
    
    def __repr__(self: object):
        return self.nome
    
    
    
class Carro:   
    def __init__(self: object, is_sedan: bool = False) -> None:
        self.is_sedan = is_sedan
        self.velocidade = 0
        self.motorista = None

    def __str__(self: object) -> str:
        if self.motorista:
            return f'Carro: {self.is_sedan} - Motorista: {self.motorista}'
        return f'Carro: {self.is_sedan} - Sem motorista'

    def dirigir(self: object, motorista: Pessoa) -> None:
        self.motorista = motorista
        self.acelerar(20)

    def acelerar(self: object, velocidade: int) -> None:
        self.velocidade += velocidade

    def parar(self: object) -> None:
        self.velocidade = 0
        self.motorista = None
            
            