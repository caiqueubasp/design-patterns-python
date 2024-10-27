from abc import ABCMeta, abstractmethod

# Assunto / Tópico
class Subject(metaclass=ABCMeta):
    
    def __init__(self):
        self.__subscribers = []
        self.last_news = None
        
    def subscribe(self, observer):
        self.__subscribers.append(observer)
        
    def unsubscribe(self, subscriber=None):
        if not subscriber:
            return self.__subscribers.pop()
        else:
            return self.__subscribers.remove(subscriber)
      
    def notify_subscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()
            
    def set_news(self, news):
        self.last_news = news
        self.notify_subscribers()
        
    def show_news(self):
        return f'Breaking News: {self.last_news}'
    
    def subscribers(self):
        return [type(subscriber).__name__ for subscriber in self.__subscribers]
        
# Interface Observer
class SubscribeType(metaclass=ABCMeta):
    
    @abstractmethod
    def update(self):
        pass
    
# Observador A
class SubscribersSMS(SubscribeType):
    
    def __init__(self, subject):
        self.subject = subject
        self.subject.subscribe(self)
        
    def update(self):
        print(f'{self.__class__.__name__}:: {self.subject.show_news()}')
        
class SubscribersEmail(SubscribeType):
    
    def __init__(self, subject):
        self.subject = subject
        self.subject.subscribe(self)
        
    def update(self):
        print(f'{self.__class__.__name__}:: {self.subject.show_news()}')
        
class SubscribersWhatsapp(SubscribeType):
        
    def __init__(self, subject):
        self.subject = subject
        self.subject.subscribe(self)
        
    def update(self):
        print(f'{self.__class__.__name__}:: {self.subject.show_news()}')
            
# Cliente
if __name__ == '__main__':
    subject = Subject()
    
    SubscribersSMS(subject)
    SubscribersEmail(subject)
    SubscribersWhatsapp(subject)
    
    print(f'Subscribers List: {subject.subscribers()}')
    
    subject.set_news('Economy News')
    subject.notify_subscribers()
    
    print(f'Removing : {type(subject.unsubscribe()).__name__}')
    print(f'Subscribers List: {subject.subscribers()}')
    
    subject.set_news('Sports News')
    subject.notify_subscribers()
