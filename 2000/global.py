def SetGlobal():
    global GlobalString
    GlobalString = "GLOBALSTRING"


def Remote():
    print(GlobalString)


SetGlobal()
print(GlobalString)
GlobalString = "RESETGLOBALSTRING"
Remote()
