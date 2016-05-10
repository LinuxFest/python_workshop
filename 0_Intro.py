# Every thing in python 3 is an object
# Object : id(cannot change), type(cannot change) and value(mutable can change, immutable cannot)
x = 2
print (x)
print (id(x))
print (type(x))

# If you change the value of x, it may look like it's changing but it's not, let's check id
x = 3
print (x)
print (id(x))

x = 2
print (id(x))

# Most fundemental types in Python are immutable > numbers, strings, tuples
# Mutable objects include > lists, dictionaries, other objects depending on implementation
