# Meta framework


class MetaStuff(object):
    # Magic - framework reserved
    def __init__(self):
        pass

    # Mangled
    def __mangled(self):
        pass

    # Private
    def _readData(self):
        pass

    # Public
    def InputData(self):
        pass

    # Class method
    @classmethod
    def className(cls):
        pass

    # Static - no need for an arg
    @staticmethod
    def staticFunc():
        pass


class Overloading(int):
    age = 0

    def __init__(self, age):
        self.age = age

    # Overload the greater than operator
    def __gt__(self, comp):
        print('Python framework is calling gt')
        return super.__gt__(self, comp)


comp1 = Overloading(123)
comp2 = Overloading(456)
print(comp1 < comp2)
