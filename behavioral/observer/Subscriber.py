from ABCObserver import ABCObserver

class Subscriber(ABCObserver):
    def update(self, value):
        print(f'{self}: Receiving updates... {value}')