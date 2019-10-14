class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


try:
    raise MyError('Tossing an error')
    # eh = 12 / 0
    # pass
except Exception as ex:
    print('Catch everything: ', ex)
    # raise
else:
    print('All is well')
