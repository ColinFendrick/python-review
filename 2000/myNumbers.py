ss = 0
while ss != 999:
    print('Use 999 to pass')
    print(bin(ss))
    print(hex(ss))
    ss = input('Enter number: ')
    try:
        ss = int(ss)
    except:
        ss = bytearray(ss, 'ascii')
        ss = int.from_bytes(ss, byteorder='big')

for val in range(0x20, 0x80):
    print('%s(%s)' % (hex(val), chr(val)), end='')
    if (val % 8 == 0):
        print()
