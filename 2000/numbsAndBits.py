num = 321
hexNum = hex(num)
octNum = oct(num)
binNum = bin(num)

print('octal -> base',
    int(octNum.split('o')[1], 8)
)

print('hex -> base',
    int(hexNum.split('x')[1], 16)
)

print('bin -> base',
    int(binNum, 0)
)
