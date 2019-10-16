def subset(arg):
    for a in arg:
        if a % 2 == 0:
            yield a


sub = list(subset([1, 2, 3, 4, 5, 6]))
print('subset:', sub)


def evenOrOdd(max):
    for item in range(max):
        if item % 2 == 0:
            yield 'even', item
        if item % 2 == 0:
            yield 'odd', item


for name, num in evenOrOdd(7):
    print('{} is surely {}'.format(num, name))

def fizzBuzz(max):
    for item in range(max):
        if item % 15 == 0:
            yield 'fizzbuzz', item
        elif item % 3 == 0:
            yield 'fizz', item
        elif item % 5 == 0:
            yield 'buzz', item

for res, num in fizzBuzz(28):
    print('%s %d' % (res, num))
