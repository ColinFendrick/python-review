# NewGlobal = 'new global'


# def loc():
#     NewLocal = 'new local'
#     print(locals())
#     print(globals())


# loc()

# if globals() is locals():
#     print('globals and locals the same')


assert(globals() is locals())


def foo():
    newVar = 0
    assert(globals() is not locals())


foo()
assert(globals() is locals())
