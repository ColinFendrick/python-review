# Basic controller class
from MyFramework.Person import Person


class ThingCtrlr01:
    @staticmethod
    def Create(recipe):
        return recipe()


var = ThingCtrlr01.Create(Person)

if var.create() is True:
    print("Testing Success")
