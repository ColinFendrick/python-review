class asserts():
    value = None
    def calc(self):
        self.value = 20
        value = 2
        return value
    def getValue(self):
        return self.value

foo = asserts()
assert(foo.value == None)
print(foo.calc())
assert(foo.value != None)
