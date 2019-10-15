class MyClass:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def __dict__(self):
        from collections import OrderedDict
        result = OrderedDict()
        result['Name'] = self.name
        result['Age'] = self.age
        result['Bal'] = self.balance
        return result


newClass = MyClass('Colin', 28, 123.456)
print(newClass.__dict__())
# Print keys
print(*newClass.__dict__())
