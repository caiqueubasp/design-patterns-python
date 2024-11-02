# Template Method Design Pattern

O padrão de projeto Template Method define o esqueleto de um algoritmo em uma operação, postergando a definição de alguns passos para subclasses. Ele permite que subclasses redefinam certos passos de um algoritmo sem alterar a estrutura do próprio algoritmo.

## Estrutura

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print("AbstractClass diz: Eu estou fazendo a maior parte do trabalho")

    def base_operation2(self):
        print("AbstractClass diz: Mas eu deixo subclasses sobrescreverem algumas operações")

    def base_operation3(self):
        print("AbstractClass diz: Mas eu sou responsável pelo trabalho principal")

    @abstractmethod
    def required_operations1(self):
        pass

    @abstractmethod
    def required_operations2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass1 diz: Implementação de Operation1")

    def required_operations2(self):
        print("ConcreteClass1 diz: Implementação de Operation2")

class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass2 diz: Implementação de Operation1")

    def required_operations2(self):
        print("ConcreteClass2 diz: Implementação de Operation2")

    def hook1(self):
        print("ConcreteClass2 diz: Sobrescrevendo Hook1")
```

## Exemplo de Uso

```python
def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()

if __name__ == "__main__":
    print("Mesmo código cliente pode funcionar com diferentes subclasses:")
    client_code(ConcreteClass1())
    print("")
    client_code(ConcreteClass2())
```

## Quando Usar

### Recomenda-se usar o Template Method quando:
- Você deseja permitir que os clientes estendam apenas certas partes de um algoritmo, mas não todo o algoritmo.
- Você tem várias classes que fazem variações do mesmo algoritmo.

### Não é recomendável usar o Template Method quando:
- Você precisa de flexibilidade total e não deseja impor uma estrutura rígida ao algoritmo.
- As subclasses precisam alterar a estrutura do algoritmo de maneira significativa.
