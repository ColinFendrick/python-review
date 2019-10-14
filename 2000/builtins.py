ins = dir(__builtins__)

count = 0
for index, avail in enumerate(ins):
    if index % 3 == 0:
        print(avail.center(25))
        continue
    print(avail.center(25), end='')
