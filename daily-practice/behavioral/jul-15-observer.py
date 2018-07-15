import abc

# Subject
class Newsletter:
    def __init__(self):
        self._observers = set()
        
    def add_observer(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.discard(observer)

    def _notify(self, data):
        for o in self._observers:
            o.update(data)

# Observer interface
class Observer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._data = None
    
    @abc.abstractmethod
    def update(self, data):
        pass

# Concrete observer
class Subscriber(Observer):
    def update(self, data):
        print('Update received')
        self._data = self._data = data


news = Newsletter()

s1 = Subscriber()
s2 = Subscriber()

news.add_observer(s1)
news.add_observer(s2)

news._notify('a')

news.remove_observer(s2)
news._notify('a')