# Basic controller class
from MyFramework import Person


class ThingCtrl03:
    @staticmethod
    def Create(order):
        return Person.Create(order)


var = ThingCtrl03.Create('Fries and Soda')

if var.create() is True:
    print("Testing Success")
