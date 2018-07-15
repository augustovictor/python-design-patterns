import abc

# Handler
class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self, complaint_lvl):
        pass


# Concrete handler
class ComplaintLvl1(Handler):
    def handle_request(self, complaint_lvl):
        if complaint_lvl is 'lvl1':
            print('solved by lvl1')
        else:
            self._successor.handle_request(complaint_lvl)

class ComplaintLvl2(Handler):
    def handle_request(self, complaint):
        if complaint is 'lvl2':
            print('Solved by lvl2')
        else:
            self._successor.handle_request(complaint)

# Program
complaint = 'lvl2'

h2 = ComplaintLvl2()
h1 = ComplaintLvl1(h2)

h1.handle_request(complaint)