"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""


class Car:
    """Common base class for all cars"""  # ClassName.__doc__.
    __timer = 0
    wheelsNumber = 4  # This variable is shared between all instances of the class

    # constructor
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        self.__timer = 0

    def tick(self):
        self.__timer += 1

    def get_time(self):
        print(self.__timer)

    def print_info(self):
        print ("Car information:\n name: %s \n model: %s \n color: %s" % (
            self.name, self.model, self.color))

    def message_from_class(self):
        print("Hi, I'm parent class")


print ("Class name is " + Car.__name__)
print ("Class documentation: " + Car.__doc__ + "\n")
car1 = Car("Peykan", "Javanan", "Gojeyi")
car1.print_info()
car1.tick()
car1.tick()
print(car1.get_time())
# print(car1.__timer)  # unable to access to private variables

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
    __secret_var = 20

    def __init__(self, name, model, color, company):
        Car.__init__(self, name, model, color)
        self.company = company

    def get_company(self):
        print (" company: " + self.company)

    def message_from_class(self):
        print("Hi! I'm child class")


google_car = MyCar("google_car", "auto", "white", "Google")
google_car.print_info()
google_car.get_company()
google_car.message_from_class()


# operator overloading
# !/usr/bin/python

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __eq__(self, other):
        return (self.a == other.a) and (self.b == other.b)

    # try implement __add__ function


v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3 = Vector(2, 10)

print (v1 == v2)
print (v1 == v3)
# print v1 + v2
