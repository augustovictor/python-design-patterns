from AbstractClass import MyAbstractClass

class ABCImp(MyAbstractClass):
    def __init__(self, value=None):
        self.prop = value

    def do_something(self, value):
        self.prop *= 2 + value

    @property
    def some_property(self):
        return self.prop

i = ABCImp()
print(i)