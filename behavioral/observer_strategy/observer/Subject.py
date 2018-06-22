from .AbsSubject import AbsSubject

class Subject(AbsSubject):
    def __init__(self):
        pass    

    def publish(self, value):
        print(f'Publishing something {value}')
        self.notify(value)