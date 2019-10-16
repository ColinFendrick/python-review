class MyWhile(object):
    def _update(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, name, age):
        self._update(name, age)

    def InputData(self):
        result = MyWhile('What?', -1)
        result.readData()
        return result

    def readData(self):
        self.name = input('What is your name? ')
        while True:
            try:
                self.age = int(input('How old are you? '))
                break
            except ValueError:
                print('Sorry, that age is not numeric.')
            except:
                print('Unhandled exception')
            finally:
                print('...')

    def update(self, name, age):
        self._update(name, age)

info = MyWhile('colin', 29)
print(info.name, info.age)
info.update('james', 47)
print(info.name, info.age)
info._update('ralph', 234)
print(info.name, info.age)
