# Observer Design Pattern

O padrão de projeto Observer é um padrão comportamental que define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

## Estrutura

- **Subject**: Mantém uma lista de observadores e fornece métodos para adicionar, remover e notificar observadores.
- **Observer**: Define uma interface de atualização para objetos que devem ser notificados de mudanças em um Subject.
- **ConcreteSubject**: Implementa o Subject e armazena o estado de interesse para os observadores.
- **ConcreteObserver**: Implementa a interface Observer e mantém uma referência ao ConcreteSubject.

## Exemplo em Python

### Subject

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)
```

### Observer

```python
class Observer:
    def update(self, subject):
        pass
```

### ConcreteSubject

```python
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()
```

### ConcreteObserver

```python
class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, subject):
        print(f'{self._name} recebeu a atualização! Novo estado: {subject.state}')
```

## Exemplo de Uso

```python
if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.attach(observer1)
    subject.attach(observer2)

    subject.state = "Novo Estado 1"
    subject.state = "Novo Estado 2"
```

Neste exemplo, quando o estado do `ConcreteSubject` é alterado, todos os observadores são notificados e atualizados automaticamente.
