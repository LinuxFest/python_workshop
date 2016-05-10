"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""


class Car:
    """Common base class for all cars"""  # ClassName.__doc__.
    wheelsNumber = 4
    count = 0  # This variable is shared between all instances of the class

    # constructor
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        self.count += 1

    def printInfo(self):
        print "Car information:\n number: %d \n name: %s \n model: %s \n color: %s" % (
            self.count, self.name, self.model, self.color)


print "Class name is " + Car.__name__
print "Class documentation: " + Car.__doc__ + "\n"
car1 = Car("Peykan", "Javanan", "Gojeyi")
car1.printInfo()

# Garbage collections
a = "sample string"  # Create object <sample string>
b = a  # Increase ref. count  of <sample string>
c = [b]  # Increase ref. count  of <sample string>

del a  # Decrease ref. count  of <sample string>
b = "new string"  # Decrease ref. count  of <sample string>
c[0] = "another string"  # Decrease ref. count  of <sample string>


# method and operator overriding


# inheritance
class MyCar(Car):
    def __init__(self, name, model, color, company):
        Car.__init__(self, name, model, color)
        self.company = company

    def get_company(self):
        print " company: " + self.company


google_car = MyCar("google_car", "auto", "white", "Google")
google_car.printInfo()
google_car.get_company()
