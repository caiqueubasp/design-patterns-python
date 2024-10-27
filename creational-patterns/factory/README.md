## Padrão de Projeto Factory

O padrão de projeto Factory é um padrão de criação que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. Este padrão é útil quando a criação do objeto envolve lógica complexa ou quando o tipo de objeto a ser criado pode variar dependendo das condições.

### Exemplo Prático em Python

Vamos considerar um exemplo prático onde temos uma fábrica de veículos. Dependendo do tipo de veículo solicitado, a fábrica criará uma instância de `Carro` ou `Moto`.

### Simple Factory
A Simple Factory é um padrão de criação que encapsula a lógica de criação de objetos em um único ponto. Não é um padrão de projeto oficial do GoF, mas é amplamente utilizado.

```python

class Carro:
    def drive(self):
        return "Dirigindo um carro"

class Moto:
    def ride(self):
        return "Pilotando uma moto"

class VeiculoFactory:
    @staticmethod
    def criar_veiculo(tipo):
        if tipo == "carro":
            return Carro()
        elif tipo == "moto":
            return Moto()
        else:
            raise ValueError("Tipo de veículo desconhecido")


# Uso
veiculo = VeiculoFactory.criar_veiculo("carro")
print(veiculo.drive())
```

### Factory Method

O Factory Method define uma interface para criar um objeto, mas permite que as subclasses decidam qual classe instanciar. Ele delega a responsabilidade de criação para subclasses.


```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def operacao(self):
        pass

class Carro(Veiculo):
    def operacao(self):
        return "Dirigindo um carro"

class Moto(Veiculo):
    def operacao(self):
        return "Pilotando uma moto"

class VeiculoCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def criar_veiculo(self):
        veiculo = self.factory_method()
        return veiculo

class CarroCreator(VeiculoCreator):
    def factory_method(self):
        return Carro()

class MotoCreator(VeiculoCreator):
    def factory_method(self):
        return Moto()

# Uso
creator = CarroCreator()
veiculo = creator.criar_veiculo()
print(veiculo.operacao())

```

### Abstract Factory

O Abstract Factory fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

```python
from abc import ABC, abstractmethod

class Carro(ABC):
    @abstractmethod
    def drive(self):
        pass

class Moto(ABC):
    @abstractmethod
    def ride(self):
        pass

class CarroLuxo(Carro):
    def drive(self):
        return "Dirigindo um carro de luxo"

class MotoLuxo(Moto):
    def ride(self):
        return "Pilotando uma moto de luxo"

class CarroPopular(Carro):
    def drive(self):
        return "Dirigindo um carro popular"

class MotoPopular(Moto):
    def ride(self):
        return "Pilotando uma moto popular"

class VeiculoFactory(ABC):
    @abstractmethod
    def criar_carro(self):
        pass

    @abstractmethod
    def criar_moto(self):
        pass

class LuxoFactory(VeiculoFactory):
    def criar_carro(self):
        return CarroLuxo()

    def criar_moto(self):
        return MotoLuxo()

class PopularFactory(VeiculoFactory):
    def criar_carro(self):
        return CarroPopular()

    def criar_moto(self):
        return MotoPopular()

# Uso
factory = LuxoFactory()
carro = factory.criar_carro()
moto = factory.criar_moto()
print(carro.drive())
print(moto.ride())
```