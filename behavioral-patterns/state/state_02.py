from abc import ABCMeta, abstractmethod


class ComputerState(metaclass=ABCMeta):
    name = 'state'
    allowed = []
    
    def change_state(self, state):
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, ' => switching to', state.name, '*** not possible. ***')
            
    def __str__(self):
        return self.name
    
    
class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']
    
    
    
class Off(ComputerState):
    name = 'off'
    allowed = ['on']
    
       
class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']
    
    
class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']
    


class Computer:
    
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()
        
    def change(self, state):
        self.state.change_state(state)
        
        
        
if __name__ == '__main__':

    comp = Computer()
    
    # On
    comp.change(On)
    
    # Off
    comp.change(Off)
    
    # On
    comp.change(On)
    
    # Suspend
    comp.change(Suspend)
    
    # Hibernate
    comp.change(Hibernate)
    
    # Off
    comp.change(Off)
    
    # Try to hibernate - not possible
    comp.change(Hibernate)
    
    # On
    comp.change(On)
    
    # Hibernate
    comp.change(Hibernate)