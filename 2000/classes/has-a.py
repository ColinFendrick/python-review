class Person:
    def __init__(self, name):
        self.name = name
        self.objects = list()

    def has_a(self, zclass):
        for obj in self.objects:
            if isinstance(obj, zclass):
                return True
        return False


class Employee(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job


employee = Employee('John', 'Manager')
print(employee.job)

person = Person('John')
person.objects.append('123')
person.objects.append(123)
print('Test one:\t', person.has_a(Employee))
person.objects.append(Employee('Jim', 'Assistant Manager'))
print('Test two:\t', person.has_a(Employee))
