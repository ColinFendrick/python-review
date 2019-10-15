class StringClass:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def __str__(self):
        return "name: %s, age: %d, balance: %02f" % (self.name, self.age, self.balance)

    def __repr__(self):
        return "(%s, %d, %02f)" % (self.name, self.age, self.balance)

    def __int__(self):
        return self.age

    def __float__(self):
        return self.balance


x = StringClass("Godzilla", 20, 123.234)
print(str(x))
print(repr(x))
print(int(x))
print(float(x))

print("str(%s), repr(%r), int(%i), float(%f)" % (x, x, x, x))

print("Int: %5d, Dec: %05d" % (42, 24))

print("Name: [%20s], Age: %03d, Balance: $%07.2f" % ("Godzilla", 22, 22.43))
