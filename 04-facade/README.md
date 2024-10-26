# Facade Design Pattern

O padrão de projeto Facade é um padrão estrutural que fornece uma interface simplificada para um conjunto de interfaces em um subsistema. Ele define uma interface de nível mais alto que torna o subsistema mais fácil de usar.

## Objetivo

O objetivo do padrão Facade é esconder a complexidade de um sistema e fornecer uma interface simplificada para o cliente.

## Exemplo em Python

Vamos considerar um exemplo onde temos um sistema complexo de um home theater. O sistema inclui várias classes como `DVDPlayer`, `Amplifier`, `Projector`, etc. A classe `HomeTheaterFacade` fornecerá uma interface simplificada para o cliente.

### Código

```python
class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def play(self, movie):
        print(f"Playing {movie}")

    def off(self):
        print("DVD Player is off")

class Amplifier:
    def on(self):
        print("Amplifier is on")

    def set_volume(self, level):
        print(f"Setting volume to {level}")

    def off(self):
        print("Amplifier is off")

class Projector:
    def on(self):
        print("Projector is on")

    def off(self):
        print("Projector is off")

class HomeTheaterFacade:
    def __init__(self, dvd_player, amplifier, projector):
        self.dvd_player = dvd_player
        self.amplifier = amplifier
        self.projector = projector

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.dvd_player.on()
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.projector.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd_player.off()
        self.amplifier.off()
        self.projector.off()

# Uso do Facade
dvd_player = DVDPlayer()
amplifier = Amplifier()
projector = Projector()

home_theater = HomeTheaterFacade(dvd_player, amplifier, projector)
home_theater.watch_movie("Inception")
home_theater.end_movie()
```

### Explicação

- **DVDPlayer, Amplifier, Projector**: Estas são as classes complexas que compõem o subsistema.
- **HomeTheaterFacade**: Esta é a classe Facade que fornece uma interface simplificada para o cliente.
- **watch_movie**: Método que liga todos os componentes necessários e começa a reproduzir o filme.
- **end_movie**: Método que desliga todos os componentes.

## Conclusão

O padrão Facade é útil para simplificar a interação com sistemas complexos, fornecendo uma interface de alto nível que esconde os detalhes de implementação do cliente.
