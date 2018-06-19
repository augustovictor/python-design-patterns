from AbcSubscriber import AbcSubscriber

class Subscriber(AbcSubscriber):
    def update(self, value):
        print(f'Observer received value: {value}')