#!/usr/bin/python

"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""

# Single line comments start with a number symbol.

""" Multi line strings can be written
    using three "s, and are often used
    as comments
"""

print ('This is an string too')
print ("line 1\n line2")
print ("escape\\n character")

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# print
print ("hello world")

# basic data types

# Boolean values
bool1, bool2 = True, False
print (type(bool1), bool1)
print (0 == bool2)
print (1 < 2 < 3)  # chained comparision

# String and Numbers

integer_var = 2
float_var = 2.5
string_var = "SampleString"
name = "ali"
age = 20
c1 = 1 + 2j  # complex numbers
c2 = 2.5 + 4j

print ("This is an integer variable: %d" % integer_var)
print ("This is an float variable: %f" % float_var)
print ("This is an string variable: %s" % string_var)
print ("%s is %d years old." % (name, age))
print (c1 + c2)
print (c1 * c2)

print (string_var[2:9])  # print from second index to ninth index (index begins from 0)
print (name[:-1])  # remove last character

print (name[::-1])  # reverse string

# Lists
integer_list = [1, 3, 5, 7]
integer_list.append(9)
integer_list.insert(2, 4)
print (integer_list)

# Tuple
sample_tuple = (1, 2, 3)
# sample_tuple.append????, No because it's immutable
print (type(sample_tuple), sample_tuple)

# Stack
stack_list = [1, 2, 3, 4]
stack_list.append(5)  # insert item to stack
num = stack_list.pop()
print (num)

# Queue
from collections import deque

queue_list = deque([1, 2, 3, 4])
queue_list.append(5)  # insert item to stack
queue_list.popleft()
print (queue_list)

# Set
a = {"Ali", "Akbar", "Asghar", "Ali"}
b = {"Hassan", "Ali", "Hossein"}
print (a.intersection(b))
#  print a & b
print (a.union(b))
print (a - b)
print (a ^ b)

# Dictionaries
students = {"sina": 9131062, "farzan": 9131069}
students["sajjad"] = 9231031

for name, std_num in students.iteritems():
    print ("1.name: %s, std_num: %d" % (name, std_num))

for name, std_num in students.iteritems():
    print("2.name: {}, std_num: {}".format(name, std_num))

del students["sina"]
print (students)

# matrix
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (matrix_a)
print (zip(*matrix_a))
