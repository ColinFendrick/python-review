class A:
    pass


class B(A):
    pass


class C:
    pass


a = A()
b = B()
c = C()

try:
    if isinstance(a, object):
        print('a is instance of object')

    if isinstance(b, A):
        print('b is instance of A')

    if not isinstance(a, B):
        print('a is not an instance of B')

    if not isinstance(c, (A, B)):
        print('c is not an instance of A or B')

    if issubclass(B, A):
        print('B is a subclass of A')
    
    if issubclass(C, object):
        print('C is as subclass of object')

    if issubclass(A, A):
        print('A class is a sublass of itself')

except TypeError as ex:
    print(ex)
