"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""

plus = 2 + 3
minus = 4.5 - 6
mul = 4.6 * 1.6
div = 12 / 3
rem = 17 % 5
quotient = 17 // 5
square = 6 ** 2
cube = 4 ** 3

print "plus: {}".format(plus)
print "minus: {}".format(minus)
print "mul: {}".format(mul)
print "div: {}".format(div)
print "rem: {}".format(rem)
print "quotient: {}".format(quotient)  # Rounded away from zero (to negative infinity)
print "square: {}".format(square)
print "cube: {}".format(cube)

string1 = "s1"
string2 = "s2"

print string1 + string2
print string1 * 3

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print list1 + list2
print list1 * 2

print list1[1]
list1.append(8)
print list1
