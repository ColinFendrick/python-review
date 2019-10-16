class MyClass():
    def __init__(self):
        self.value = 'aaa'

    def __eq__(self, obj): # Just check the value prop for now
        return self.value == obj.value


class InheritingClass(MyClass):
    def __init__(self):
        super().__init__()

for meta in MyClass, InheritingClass:
    print(type(meta))

myClass = MyClass()
inheritingClass = InheritingClass()
print(myClass == inheritingClass)
