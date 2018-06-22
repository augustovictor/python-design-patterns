from .AbsObserver import AbsObserver

class Observer(AbsObserver):
    def __init__(self):
        self.subject = None
    
    def update(self, value):
        print(f'Received value {value}')
    
    def post_something(self, value):
        print('Observer posting something...')
        self.subject.publish(value)