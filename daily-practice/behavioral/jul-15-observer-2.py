import abc

# Subject
class Blog:
    def __init__(self):
        self._subscribers = set()
    
    def add_subscriber(self, subscriber):
        self._subscribers.add(subscriber)
    
    def unsubscribe(self, subscriber):
        self._subscribers.discard(subscriber)

    def _notify(self, data):
        for subs in self._subscribers:
            subs.update(data)

    def publish_post(self, new_post):
        self._notify(new_post)

# Obsever
class Observer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._new_post = None

    @abc.abstractmethod
    def update(self, new_post):
        pass

# Concrete observer
class Subscriber(Observer):
    def update(self, new_post):
        print('Received post...')
        self._new_post = new_post

# Program
blog = Blog()

s1 = Subscriber()
s2 = Subscriber()

blog.add_subscriber(s1)
blog.add_subscriber(s2)

blog.publish_post('New post...')

blog.unsubscribe(s2)

blog.publish_post('New post...')
