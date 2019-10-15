class MyData(object):
    def readData(self):
        self.name = input('What\'s your name?')

        while True:
            try:
                self.age = int(input('What\'s your age?'))
                break
            except ValueError as ex:
                print('Sorry, age is not a number!', ex)


info = MyData()
info.readData()
print(info.name, info.age)
