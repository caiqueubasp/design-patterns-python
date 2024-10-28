from abc import ABCMeta, abstractmethod

# Command
class Order(metaclass=ABCMeta):
    
    @abstractmethod
    def execute(self):
        pass
    
    
# ConcreteCommand
class BuyStockOrder(Order):
    
    def __init__(self, stock, stock_name):
        self.stock = stock
        self.stock_name = stock_name
        
        
    def execute(self):
        self.stock.buy(self.stock_name)
        
        
# ConcreteCommand
class SellStockOrder(Order):
    
    def __init__(self, stock, stock_name):
        self.stock = stock
        self.stock_name = stock_name
        
        
    def execute(self):
        self.stock.sell(self.stock_name)
        

# Receiver
class StockTrade:
    
    def buy(self, stock_name):
        print(f"You will BUY {stock_name} stocks")
        
        
    def sell(self, stock_name):
        print(f"You will SELL {stock_name} stocks")
        
        
# Invoker
class Agent:
    
    def __init__(self):
        self.__orderQueue = []
        
        
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()
        
        

if __name__ == "__main__":
    # Client
    stock = StockTrade()
    buyStock1 = BuyStockOrder(stock, "AAPL")
    sellStock1 = SellStockOrder(stock, "GOOGL")
    buyStock2 = BuyStockOrder(stock, "MSFT")
    sellStock2 = SellStockOrder(stock, "AMZN")
    buyStock3 = BuyStockOrder(stock, "TSLA")
    sellStock3 = SellStockOrder(stock, "FB")
    buyStock4 = BuyStockOrder(stock, "NFLX")
    sellStock4 = SellStockOrder(stock, "INTC")
    
    # Invoker
    agent = Agent()
    agent.placeOrder(buyStock1)
    agent.placeOrder(sellStock1)
    agent.placeOrder(buyStock2)
    agent.placeOrder(sellStock2)
    agent.placeOrder(buyStock3)
    agent.placeOrder(sellStock3)
    agent.placeOrder(buyStock4)
    agent.placeOrder(sellStock4)
    