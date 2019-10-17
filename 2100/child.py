from frameworkUser import Person


class Child(Person):
    def __init__(self):
        super().__init__()
        super().create('Making a child out of a Person')


child = Child()
