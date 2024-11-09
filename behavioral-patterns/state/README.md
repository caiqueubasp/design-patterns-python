# State Design Pattern

O padrão de projeto State é um padrão comportamental que permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá mudar sua classe.

## Estrutura

O padrão State consiste em três componentes principais:
1. **Context**: Mantém uma referência a um objeto State que define o estado atual.
2. **State**: Define uma interface para encapsular o comportamento associado a um estado particular do Context.
3. **Concrete States**: Implementam o comportamento específico de cada estado.

## Exemplo em Python

```python
class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle(self)

class State:
    def handle(self, context):
        raise NotImplementedError("Subclasses devem implementar este método")

class ConcreteStateA(State):
    def handle(self, context):
        print("Estado A lidando com a solicitação e mudando para o Estado B")
        context.set_state(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self, context):
        print("Estado B lidando com a solicitação e mudando para o Estado A")
        context.set_state(ConcreteStateA())

# Uso
context = Context(ConcreteStateA())
context.request()  # Estado A lidando com a solicitação e mudando para o Estado B
context.request()  # Estado B lidando com a solicitação e mudando para o Estado A
```

## Quando usar

- **Recomendado**:
  - Quando o comportamento de um objeto depende de seu estado e deve mudar dinamicamente durante o tempo de execução.
  - Quando as operações têm grandes blocos condicionais que dependem do estado do objeto.

- **Não recomendado**:
  - Quando há poucos estados e o comportamento não muda frequentemente.
  - Quando a mudança de estado não é complexa e pode ser gerenciada com simples condicionais.
