ins = dir(__builtins__)

for count, avail in enumerate(ins, 1):
    if count % 3 == 0:
        print(avail.center(25))
        continue
    print(avail.center(25), end='')
