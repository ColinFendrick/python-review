class Skitz:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            self.__age = 0
        elif age > 120:
            self.__age = 120
        else:
            self.__age = age


skitz = Skitz(88)
print(skitz.age)
