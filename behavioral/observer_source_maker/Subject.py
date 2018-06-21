from AbsObserver import AbsObserver

class Subject:
    def __init__(self):
        self.observers = set()
    
    def add_subscriber(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer must be a subclass of AbsObserver')
        observer.subject = self
        self.observers.add(observer)
    
    def remove_subscriber(self, observer):
        observer.subject = None
        self.observers.remove(observer)

    def notify_all(self, value):
        for observer in self.observers:
            observer.update(value)
    
    def post(self, value):
        print('Publishing value...')
        self.notify_all(value)