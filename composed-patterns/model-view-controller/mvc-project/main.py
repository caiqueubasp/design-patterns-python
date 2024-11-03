from tornado import ioloop
from tornado import httpserver
from tornado.web import Application

from controllers.produto_controller import Index, Novo, Atualizar, Deletar


class RunApp(Application):
    
    def __init__(self):
        handlers = [
            (r'/', Index),
            (r'/produto/novo', Novo),
            (r'/produto/update/(\d+)/status/(\d+)', Atualizar),
            (r'/produto/delete/(\d+)', Deletar),
        ]
        
        settings = dict(
            debug=True,
            template_path='views',
            static_path='static'
        )
        
        Application.__init__(self, handlers, **settings)
        
        
if __name__ == '__main__':
    app = RunApp()
    server = httpserver.HTTPServer(app)
    server.listen(8888)
    ioloop.IOLoop.instance().start()
    print('Server running on http://localhost:8888')