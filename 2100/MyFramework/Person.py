from MyFramework.AbsThing import Thing


class Person(Thing):
    @classmethod
    def Create(cls, order=None):
        print(order)
        return cls()

    def create(self):
        return True

    def read(self):
        return True

    def update(self):
        return True

    def delete(self):
        return True
