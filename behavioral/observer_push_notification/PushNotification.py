from AbcSubscriber import AbcSubscriber

class PushNotification():

    subscribers = set()
    
    def publish_something(self, value):
        print('Publishing content...')
        self.notify(value)
    
    def add_subscriber(self, observer):
        if not isinstance(observer, AbcSubscriber):
            raise TypeError('Given observer is not type of AbcSubscriber')
        self.subscribers.add(observer)

    def remove_subscriber(self, observer):
        self.subscribers.remove(observer)

    def notify(self, value):
        for subscriber in self.subscribers:
            subscriber.update(value)