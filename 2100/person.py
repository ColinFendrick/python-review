from CrudFramework import Thing


class Person(Thing):
    def __init__(self):
        super().create('Making a Person out of Thing')


person = Person()
