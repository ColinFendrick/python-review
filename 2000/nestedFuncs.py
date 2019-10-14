def func():
    value = 1

    def calc():
        value = 2
        print('calc:', value)
    calc()
    print('func:', value)


func()


def twoFunc():
    value = 1

    def calc():
        nonlocal value
        value = 2
        print('calc2:', value)
    calc()
    print('func2:', value)


twoFunc()
