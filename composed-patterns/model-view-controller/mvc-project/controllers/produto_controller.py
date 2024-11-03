from tornado.web import RequestHandler

from models.produto_model import ProdutoModel


class Index(ProdutoModel):
    
    def get(self):
        products = ProdutoModel.get_all()
        self.render('index.html', products=products)
        
        
class Novo(RequestHandler):
    
    def get(self):
        self.render('novo.html')
        
    def post(self):
        nome = self.get_argument('nome', None)
        preco = self.get_argument('preco', None)
        
        product = ProdutoModel(nome=nome, preco=preco)
        product.save()
        
        self.redirect('/')
        
        
class Atualizar(RequestHandler):
    
    def get(self, id, status, nome, preco):
        product = ProdutoModel.get_by_id(id)
        product.status = status
        product.nome = nome
        product.preco = preco
        product.update()
        
        self.redirect('/')
        

class Deletar(RequestHandler):
        
        def get(self, id):
            product = ProdutoModel.get_by_id(id)
            product.delete()
            
            self.redirect('/')
            
