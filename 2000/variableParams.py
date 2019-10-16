def args(*argv):
    for ref in argv:
        print(ref)


args('One', 'Two', 'Three')


# This is for dict
def argsD(**argv):
    for ref in argv.values():
        print(ref)


argsD(foo='One', bar='Two', baz='Three')
