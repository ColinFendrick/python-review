from MyNewModule import CallFunc as Call

print("__doc__:", Call.__doc__, end="\n\n--=*=--\n\n")

help(Call)

print("aka: Calls():", Call())
dir(MyNewModule)