from typing import  List, Tuple


class Curso:
    
    def __init__(self: object, nome: str = 'Curso Padrao', carga_horaria: int = 45) -> None:
        self.nome = nome
        self.carga_horaria = carga_horaria
        
        
curso1: Curso = Curso()
curso2: Curso = Curso('Python Fundamentos', 40)
curso3: Curso = Curso('Python Avançado', 60)
curso4: Curso = Curso('Python Web', 80)

print(curso1.__dict__)
print(curso2.__dict__)
print(curso3.__dict__)


nome: str = 'Geek University'
tupla: Tuple[int, int, int, int] = (1, 2, 3, 4)
lista: List[int] = [1, 2, 3, 4]

# print(nome[:4], tupla[:4], lista[:4])


class Pessoa:
    def __init__(self: object, nome: str) -> None:
        self.nome = nome
    
    def andar(self: object) -> None:
        print('está andando')
    
    
class Aluno(Pessoa):
    
    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.matricula = matricula
        

felicity = Aluno('Felicity Jones', '1234')
felicity.andar()


def gerar_fibonacci(qtd: int) -> None:
    if qtd <= 0:
        print('Quantidade deve ser maior que zero')
    else:
        print('Sequencia de Fibonacci papa {qtd} termos(s) é: ')
        contador: int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < qtd:
            print(aux1, end=' ')
            proximo = aux1 + aux2
            aux1 = aux2
            aux2 = proximo
            contador += 1
            
# gerar_fibonacci(56)


class Motor():
    def ligar(self: object) -> None:
        print('Motor ligado...')
        
        
class Pneu():
    def encher(self: object) -> None:
        print('Pneu cheio...')
        
        
class Carro():
    def __init__(self: object, modelo: str) -> None:
        self.modelo = modelo
        self.motor = Motor()
        self.pneu1 = Pneu()
        self.pneu2 = Pneu()
        self.pneu3 = Pneu()
        self.pneu4 = Pneu()
        
    def andar(self: object) -> None:
        print('Carro andando...')
    
    
fusca = Carro('Fusca')
fusca.motor.ligar()