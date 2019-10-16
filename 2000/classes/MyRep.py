class MyRep():
    def __new__(cls):
        print('New runs // INTERCEPT')
        return super(MyRep, cls).__new__(cls)

    def __init__(self):
        print('Init runs // INTERCEPT')

    def __del__(self):
        print('Deleting the object // INTERCEPT')


one = MyRep()
two = MyRep()
del one
