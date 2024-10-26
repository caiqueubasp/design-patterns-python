from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass
    
    
class Dog(Animal):
    def do_say(self):
        print('Bark')
        

class Cat(Animal):
    def do_say(self):
        print('Meow')
        
        
class Duck(Animal):
    def do_say(self):
        print('Quack')
        
        
# forest factory defined

class ForestFactory(object):
    def make_sound(self, type):
        return eval(type)()
    
    
# client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('Qual animal você quer? (Dog/Cat/Duck): ')
    obj = ff.make_sound(animal)
    obj.do_say()
