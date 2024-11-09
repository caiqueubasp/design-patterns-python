from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    
    @abstractmethod
    def handle(self):
        pass
    

class ConcreteStateA(State):
    
    def handle(self):
        print("ConcreteStateA")
        
        
class ConcreteStateB(State):
    
    def handle(self):
        print("ConcreteStateB")
        
        
class Context(State):
    
    def __init__(self):
        self.state = None
        
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
        
    def handle(self):
        self.state.handle()
        
        
context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()

context.setState(stateA)
context.handle()

context.setState(stateB)
context.handle()