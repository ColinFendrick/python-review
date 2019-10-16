class MyWhile(object):
    def __init__(self, age, name):
        self.name = name
        self.age = age

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


MyWhile('colin', 29).InputData()
