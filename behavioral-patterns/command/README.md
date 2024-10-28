# Command Design Pattern

O padrão de projeto Command é um padrão comportamental que transforma uma solicitação em um objeto, permitindo que você parametrize clientes com diferentes solicitações, enfileire ou registre solicitações e suporte operações que podem ser desfeitas.

## Estrutura

O padrão Command envolve os seguintes componentes:
- **Command**: Declara uma interface para executar uma operação.
- **ConcreteCommand**: Implementa a interface Command e define a ligação entre um objeto Receiver e uma ação.
- **Client**: Cria um objeto ConcreteCommand e define seu Receiver.
- **Invoker**: Pede ao Command para executar a solicitação.
- **Receiver**: Sabe como realizar as operações associadas a uma solicitação.

## Exemplo em Python

```python
class Command:
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Uso
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Output: Light is ON

remote.set_command(light_off)
remote.press_button()  # Output: Light is OFF
```

## Quando usar

### Recomendações de uso:
- Quando você precisa parametrizar objetos com operações.
- Quando você quer enfileirar operações, agendá-las ou executá-las remotamente.
- Quando você precisa implementar operações que podem ser desfeitas.

### Quando evitar:
- Quando a complexidade adicional não é necessária.
- Quando uma simples chamada de método é suficiente para resolver o problema.
