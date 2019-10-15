from typing import Literal

print('Enter 1 or 0: ')


def check(first: Literal[0, 1], second: Literal[0, 1]) -> None:
    if first and second:
        print('Both true')
    elif first:
        print('First true')
    elif second:
        print('Second True')
    elif not (first or second):
        print('Both falsep')
    else:
        raise ValueError('Must be 1 or 2')


check(int(input('FIRST: ')), int(input('SECOND: ')))
