

class SanitizerChecker:
    
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not SanitizerChecker.__instance:
            SanitizerChecker.__instance = super(SanitizerChecker, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    
    
    def __init__(self):
        self.__servers = []
        
    def check_server(self, serv):
        print(f'Checking server...{self.__servers[serv]}')
        
    def add_server(self):
        self.__servers.append('server 1')
        self.__servers.append('server 2')
        self.__servers.append('server 3')
        self.__servers.append('server 4')
        
    def change_server(self):
        self.__servers.pop()
        self.__servers.append('server 5')
        
        
sanitizer1 = SanitizerChecker()
sanitizer2 = SanitizerChecker()

sanitizer1.add_server()
print(f'Cronograma de checagem de servidores... A')
for i in range(4):
    sanitizer1.check_server(i)
    
sanitizer2.change_server()
print(f'Cronograma de checagem de servidores... B')
for i in range(4):
    sanitizer2.check_server(i)