from AbsObserver import AbsObserver

class Observer(AbsObserver):
    def update(self, value):
        print(f'{self.name} received value...{value}')