from abc import ABCMeta, abstractmethod


# Abstract Factory
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_pizza(self):
        pass
    
    
    @abstractmethod
    def create_pizza_veg(self):
        pass
    
    
    
# Concrete Factory 1
class IndianPizzaFactory(PizzaFactory):
    def create_pizza(self):
        return ChickenPizza()
    
    
    def create_pizza_veg(self):
        return PaneerPizza()
    
# Concrete Factory 2
class USPizzaFactory(PizzaFactory):
    def create_pizza(self):
        return MexicanPizza()
    
    
    def create_pizza_veg(self):
        return BroccoliPizza()
    
    
# Abstract Product 1
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass
    
    
# Abstract Product 2
class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass
    
    
# Concrete Product 1
class BroccoliPizza(VegPizza):
    def prepare(self):
        print(f'Prepare {type(self).__name__} Pizza')
        

# Concrete Product 2
class MexicanPizza(Pizza):
    def serve(self, VegPizza):
        print(f'{type(self).__name__} is served with Mexican Pizza in {type(VegPizza).__name__}')
        

class PaneerPizza(VegPizza):
    def prepare(self):
        print(f'Prepare {type(self).__name__} Pizza')

        

# Concrete Product 3
class ChickenPizza(Pizza):
    def serve(self, VegPizza):
        print(f'{type(self).__name__} is served with Chicken Pizza in {type(VegPizza).__name__}')
        

# Concrete Product 4
class IndianPizza(Pizza):
    def serve(self, VegPizza):
        print(f'{type(self).__name__} is served with India Pizza in {type(VegPizza).__name__}')
        
        
        
# Client
class PizzaStore:
     
    def make_pizza(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.pizza = factory.create_pizza()
            self.veg_pizza = factory.create_pizza_veg()
            self.veg_pizza.prepare()
            self.pizza.serve(self.veg_pizza)
            
            
pizza_store1 = PizzaStore()
pizza_store1.make_pizza()