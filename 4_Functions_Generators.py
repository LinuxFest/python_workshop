"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""


# Function Definition


def func1(x, y):
    z = x + y
    print ("Sum of %d and %d is %d" % (x, y, z))


func1(3, 5)


# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "easier code reuse"


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print (build_sentence(benefit))


name_the_benefits_of_functions()

# partial functions
from functools import partial

db1 = partial(func1, 5)
db1(10)


# lambda notation


# -------------------------------------------------------

# Generators

# 1: The generators are powerful possibility to create iterators
# 2: Syntax difference with functions: using yield instead of return
# 3: generator at the end of each iteration(which is mentioned by yield statement) save the local variables and
#    after next call, resume its job.
def city_generator():
    a = 10
    print (a)
    yield ("Konstanz")
    a += 1
    yield ("Zurich")
    print (a)
    yield ("Schaffhausen")
    yield ("Stuttgart")


cities = city_generator()
# print cities  # generator object
# for city in cities:
#    print city

print (cities.next())
print (cities.next())
print (cities.next())


# print cities.next()
# print cities.next()

def fib():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


fib_generator = fib()
print (fib_generator.next())
print (fib_generator.next())
print (fib_generator.next())
print (fib_generator.next())
print (fib_generator.next())
print (fib_generator.next())
print (fib_generator.next())
# you can see more information in http://www.python-course.eu/generators.php
