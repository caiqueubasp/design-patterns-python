from db import _execute



class ProdutoModel:
    
    def __init__(self, nome, preco, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = 1 # 1 - Ativo, 0 - Inativo
        
        # Se a tabela produtos não existir, cria a tabela
        query = 'CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, status INTEGER)'
        _execute(query)
        
    def save(self):
        query = f'INSERT INTO produtos (nome, preco, status) VALUES ("{self.nome}", {self.preco}, {self.status})'
        _execute(query)
        
    def update(self):
        query = f'UPDATE produtos SET nome = "{self.nome}", preco = {self.preco}, status = {self.status} WHERE id = {self.id}'
        _execute(query)
        
    def delete(self):
        query = f'DELETE FROM produtos WHERE id = {self.id}'
        _execute(query)
        
        
    @staticmethod
    def get_all():
        query = 'SELECT * FROM produtos'
        return _execute(query)
    
    @staticmethod
    def get_by_id(id):
        query = f'SELECT * FROM produtos WHERE id = {int(id)}'
        product = _execute(query)[0]
        product = ProdutoModel(nome=product[1], preco=product[2], id=product[0])