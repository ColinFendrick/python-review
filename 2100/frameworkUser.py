from CrudFramework import Thing

class Person(Thing):
    def __init__(self):
        super().create()

x = Person()
