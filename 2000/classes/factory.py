class MyData(object):
    def __init__(self):
        self.name = 'default'
        self.age = 999
    def InputData(self):
        result = MyData()
        result.name = input('What is your name? ')
        while True:
            try:
                result.age = int(input('How old are you? '))
                break
            except ValueError:
                print('Sorry, that value is not a number.')
            except:
                print('Unhandled exception')
            finally:
                print('----------------------')
        return result

x = MyData()
x.InputData()
