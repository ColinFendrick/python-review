GlobalString = 'GLOBAL'

def ChangeGlobal():
    global GlobalString
    GlobalString = 'NEW GLOBAL'

print(GlobalString)
ChangeGlobal()
print(GlobalString)
GlobalString = 'THIRD GLOBAL'
print(GlobalString)
