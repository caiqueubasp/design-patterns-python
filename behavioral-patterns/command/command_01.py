class Installer:
    
    def __init__(self, source, destination):
        print('Installing...')
        self.options = []
        self.source = source
        self.destination = destination
        
    def preferences(self, option):
        self.options.append(option)
        
    def install(self):
        for option in self.options:
            print('Installing', option)
            if list(option.values())[0]:
                print(f'Copying {self.source} to {self.destination}')
            else:
                print('Installation Done!')
                
if __name__ == '__main__':
    # Inicia a instalação
    installer = Installer('python3.9.1.gzip', '/usr/bin/')
    
    # O usuario escolhe a opção de instalação
    installer.preferences({'python': True})
    installer.preferences({'java': False})
    
    # Executa a instalação
    installer.install()
