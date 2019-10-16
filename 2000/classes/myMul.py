#!/usr/bin/env python3


class MyMul:
    def __init__(self):
        self._val = 0

    def assign(self, str_value):
        try:
            self._val = int(str_value)
        except:
            print('Value cannot be converted to int - resetting it to 0')
            self._val = 0
        return self._val

    def __imul__(self, ival):  # overloading in place multiplication
        print('ival', type(ival), ival)
        self._val = self._val * ival
        return self # Return the whole of self

    def __mul__(self, dval):  # overloading standard multiplication
        print('dval:', type(dval), dval)
        return self._val * dval


myMul = MyMul()
myMul.assign('2')
print(myMul * 10)
print(myMul * 10.131)
myMul *= 7
print('imul', myMul._val)
