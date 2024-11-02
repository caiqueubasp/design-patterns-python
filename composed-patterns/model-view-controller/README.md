# Model-View-Controller (MVC) Design Pattern

O padrão de projeto Model-View-Controller (MVC) é uma abordagem arquitetural que separa a aplicação em três componentes principais: Model, View e Controller. Essa separação facilita a manutenção e a escalabilidade do código.

## Componentes do MVC

### Model
O Model representa os dados da aplicação e a lógica de negócios. Ele é responsável por gerenciar o estado da aplicação e responder às solicitações de dados do Controller.

```python
class Model:
    def __init__(self):
        self.data = "Hello, MVC!"

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
```

### View
A View é responsável pela apresentação dos dados ao usuário. Ela exibe os dados fornecidos pelo Model e envia as interações do usuário ao Controller.

```python
class View:
    def display_data(self, data):
        print(f"Data: {data}")
```

### Controller
O Controller atua como um intermediário entre o Model e a View. Ele recebe as entradas do usuário, processa essas entradas (possivelmente alterando o estado do Model) e atualiza a View.

```python
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_data(self, data):
        self.model.set_data(data)
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        self.view.display_data(data)
```

## Exemplo de Uso

```python
if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Exibir dados iniciais
    controller.update_view()

    # Atualizar dados
    controller.set_data("New Data")
```

## Quando Usar o Padrão MVC

### Recomendações
- **Aplicações com Interface Gráfica (GUI)**: Facilita a separação entre a lógica de negócios e a interface do usuário.
- **Aplicações Web**: Ajuda a organizar o código em camadas distintas, tornando-o mais modular e testável.
- **Projetos de Longa Duração**: Facilita a manutenção e a escalabilidade do código.

### Quando Evitar
- **Aplicações Simples**: Pode adicionar complexidade desnecessária a projetos pequenos e simples.
- **Desempenho Crítico**: A separação de responsabilidades pode introduzir overhead, o que pode ser um problema em sistemas onde o desempenho é crítico.
