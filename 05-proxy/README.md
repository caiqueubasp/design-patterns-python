# Proxy Design Pattern

O padrão de projeto Proxy é um padrão estrutural que fornece um substituto ou ponto de acesso para outro objeto. Um proxy controla o acesso ao objeto original, permitindo que você faça algo antes ou depois da solicitação chegar ao objeto original.

## Estrutura

O padrão Proxy envolve três componentes principais:
1. **Subject**: Define a interface comum para o RealSubject e o Proxy.
2. **RealSubject**: A classe real que o Proxy representa.
3. **Proxy**: Controla o acesso ao RealSubject.

## Exemplo em Python

Vamos criar um exemplo simples para ilustrar o padrão Proxy. Suponha que temos uma classe `RealSubject` que realiza uma operação custosa, e queremos controlar o acesso a essa operação usando um Proxy.

### Subject

```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass
```

### RealSubject

```python
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")
```

### Proxy

```python
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")
```

### Uso

```python
def client_code(subject: Subject):
    subject.request()

if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    client_code(proxy)
```

## Quando usar

- Quando você precisa controlar o acesso a um objeto.
- Quando você precisa adicionar funcionalidades adicionais ao objeto sem alterar seu código.

## Vantagens

- Controle de acesso ao objeto original.
- Pode adicionar funcionalidades adicionais sem modificar o objeto original.

## Desvantagens

- Pode adicionar complexidade ao sistema.
- Pode introduzir latência devido à sobrecarga do proxy.
