from abc import ABC, abstractmethod

class Command(ABC):
    
    def __init__(self, receiver):
        self.receiver = receiver
    
    @abstractmethod
    def execute(self):
        pass
    
    
class InstallCommand(Command):
    
    def __init__(self, receiver):
        self.receiver = receiver
    
    def execute(self):
        self.receiver.install()
        
        
class Receiver:
    
    def install(self):
        print('Receiver Action...')
    
    
class Invoker:
    
    def command(self, command):
        self.command = command
    
        
    def execute(self):
        self.command.execute()
        
        
        
if __name__ == '__main__':
    receiver = Receiver()
    command = InstallCommand(receiver)
    invoker = Invoker()
    
    invoker.command(command)
    invoker.execute()