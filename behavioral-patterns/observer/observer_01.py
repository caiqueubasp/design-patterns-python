

class Object:
    
    def __init__(self):
        self.__observers = []
        
        
    def __repr__(self):
        return '::Object::'
    
    def register(self, observer):
        self.__observers.append(observer)
        
        
    def notyfy_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)
            
            
            
class ObserverA:
    
    def __init__(self, object):
        object.register(self)
        
    def notify(self, object, *args):
        print(f'{self.__class__.__name__}:: Got {args} From {object}')
        
        
        
class ObserverB:
    
    def __init__(self, object):
        object.register(self)
        
    def notify(self, object, *args):
        print(f'{self.__class__.__name__}:: Got {args} From {object}')
        
        

object = Object()
observer_a = ObserverA(object)
observer_b = ObserverB(object)

object.notyfy_all('notification')
    