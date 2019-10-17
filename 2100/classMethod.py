# Basic controller class
from MyFramework import Person


class ThingCtrl02:
    @classmethod
    def Create(cls):
        return Person()


var = ThingCtrl02.Create()

if var.create() is True:
    print("Testing Success")
