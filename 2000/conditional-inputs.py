print('Enter 1 or 0: ')

try:
    first = int(input('First: '))
    second = int(input('Second: '))

    if not (first in [0, 1]) or not (second in [0, 1]):
        print('You must only put a 1 or 0, not other numbers allowed.')
    elif first and second:
        print('Both true')
    elif first:
        print('One true')
    elif second:
        print('Two True')
    elif not (first or second):
        print('Both false')
    else:
        print('Something went wrong')
except ValueError:
    raise
