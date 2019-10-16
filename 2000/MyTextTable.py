for val in range(11, 91):
    print(val, end=' ')
    if (val % 10 == 0):
        print()

val = 10
while val <= 90:
    print(val, end=' ')
    val += 1
    if (val % 10 == 0):
        print()
        continue
    if (val > 90):
        print('...')
        break
