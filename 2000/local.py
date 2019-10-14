def DoSomething():
    DoTheThing = "LOCAL"

# print(DoTheThing)
DoTheThing = 'GLOBAL'
print(DoTheThing)
DoSomething()
print(DoTheThing)