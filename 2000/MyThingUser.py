import NewThing
print('___init___doc: \n=======\n')
help(NewThing)
dir(NewThing)

print('Import Module:\n=====\n')
import NewThing.MyNewThing
help(NewThing.MyNewThing)
dir(NewThing.MyNewThing)

print('Module as alais:\n=====\n')
import NewThing.MyNewThing as booya
help(booya)
dir(booya)
