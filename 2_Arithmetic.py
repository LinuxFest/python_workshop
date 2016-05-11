"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""
from __future__ import division

plus = 2 + 3
minus = 4.5 - 6
mul = 4.6 * 1.6
div = 12 / 3
rem = 17 % 5
quotient = 17 // 5
square = 6 ** 2
cube = 4 ** 3

print ("plus: {}".format(plus))
print ("minus: {}".format(minus))
print ("mul: {}".format(mul))
print ("div: {}".format(div))
print ("rem: {}".format(rem))
print ("quotient: {}".format(quotient))  # Rounded away from zero (to negative infinity)
print ("square: {}".format(square))
print ("cube: {}".format(cube))

print (42 / 9)
num = round(42 / 9)
print (num)
num = round(42 / 9, 2)
print (num)

string1 = "s1"
string2 = "s2"

print (string1 + string2)
print (string1 * 3)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print (list1 + list2)
print (list1 * 2)

print (list1[1])
list1.append(8)
print (list1)


# bitwise operation
def func(num):
    print('{:08b}'.format(num))
    pass


x, y = 0x60, 0xa1
print (func(x))
print (func(y))
print (func(x | y))
print (func(x & y))
print (func(x ^ y))  # xor
print (func(x << 2))  # shift left
print (func(x + 2))

