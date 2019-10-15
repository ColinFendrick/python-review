print('First: {}, Second: {}'.format(22, 42))
print('Second: {1}, First: {0}'.format(22, 42))

print('First: {foo}, Second: {bar}'.format(foo='foo', bar='bar'))
print('Second: {bar}, First: {foo}'.format(foo='foo', bar='bar'))

print('Name [{0:>12s}], Age: {1:<d}, Balance: ${2:<7.2f}'.format(
    'Client', 62, 22.42))
print('Reusing single arg: {0:6.2f} or {0:6.3f}'.format(5.1234))
print('Ignoring multiple: {0:6.2f} or {0:6.3f}'.format(5.1234, 1.2345))


def showChars(num, token):
    return "\t{}".format(token * (num + 4))


def show(message):
    char = '¥'
    # Add in our own spaces and make string uppercase
    message = '  {}  '.format(message.strip().upper())
    charLine = showChars(len(message), char)
    print('{0}\n\t{2}{2}{1}{2}{2}\n{0}'.format(charLine, message, char))


show('special')
show('    asdfouas0dfusaldjfl2348u23lnfsad   ')
