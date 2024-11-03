

class Model:
    
    def __init__(self):
       self.products = {
            'ps5': {'id': 1, 'nome': 'Playstation 5', 'preco': 5000},
            'xbox': {'id': 2, 'nome': 'Xbox Series X', 'preco': 4500},
            'switch': {'id': 3, 'nome': 'Nintendo Switch', 'preco': 3000},
            'pc': {'id': 4, 'nome': 'PC Gamer', 'preco': 6000},
            'ps4': {'id': 5, 'nome': 'Playstation 4', 'preco': 2000},
            'xbox360': {'id': 6, 'nome': 'Xbox 360', 'preco': 1000},
            'switchlite': {'id': 7, 'nome': 'Nintendo Switch Lite', 'preco': 2000},
            'pcgamer': {'id': 8, 'nome': 'PC Gamer', 'preco': 5000},
            'ps3': {'id': 9, 'nome': 'Playstation 3', 'preco': 1000},
            'xboxone': {'id': 10, 'nome': 'Xbox One', 'preco': 1500},
            'switchpro': {'id': 11, 'nome': 'Nintendo Switch Pro', 'preco': 4000},
            'pcgamer2': {'id': 12, 'nome': 'PC Gamer', 'preco': 7000},
            'ps2': {'id': 13, 'nome': 'Playstation 2', 'preco': 500},
            'xboxseries': {'id': 14, 'nome': 'Xbox Series', 'preco': 4000},
            'switch2': {'id': 15, 'nome': 'Nintendo Switch', 'preco': 3000},
            'pcgamer3': {'id': 16, 'nome': 'PC Gamer', 'preco': 8000},
            'ps1': {'id': 17, 'nome': 'Playstation 1', 'preco': 300},
            'xbox2': {'id': 18, 'nome': 'Xbox 2', 'preco': 2000},
            'switch3': {'id': 19, 'nome': 'Nintendo Switch', 'preco': 3000},
            'pcgamer4': {'id': 20, 'nome': 'PC Gamer', 'preco': 9000},
       }
       
       
       
class Controlller:
    
    def __init__(self):
        self.model = Model()
        
    def get_prodcts(self):
        products = self.model.products.keys()
        
        print('Produtos disponíveis:')
        for product in products:
            print(f'{product}: {self.model.products[product]["nome"]} - R$ {self.model.products[product]["preco"]}')
            print(f'ID: {self.model.products[product]["id"]}')
            print(f'Name: {self.model.products[product]["nome"]}')
            print(f'Price: R$ {self.model.products[product]["preco"]}')
            print('')
            
            
class View:
    
    def __init__(self):
        self.controller = Controlller()
        
    def show_products(self):
        self.controller.get_prodcts()
        
        
if __name__ == '__main__':
    view = View()
    view.show_products()