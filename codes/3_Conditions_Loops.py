from __future__ import print_function

"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""

x = 10
y = 2
print(x == 10)
print(x == 20)

if x == 10:
    print("x equal to 10")
else:
    print("x is not equal to 10")

if x == 10 and y == 3:
    print(x + y)
elif y == 2 or x == 20:
    print(x - y)

a = 1
b = 2
result = 'a is bigger than b' if a > b else 'a is smaller than b'
print(result)

listA = [1, 2, 3, 4]

if 3 in listA:
    print("3 is in listA")

if 5 not in listA:
    print("5 is not in list A")

# ------------------------------------------
# Loops
print("Numbers:")
for i in range(1, 10):
    print(i)

print("Numbers:")
for i in range(100, 10, -5):
    print(i)

print("Alist:")
for x in listA:
    print(x)

fh = open('data.txt')
for i in fh.readlines():
    print(i, end='')

sample_string = 'sample string'
for i, c in enumerate(sample_string):
    print(i, c)
    if c == "s":
        print('index is {}'.format(i))
    if c == "t":
        print("breaking...")
        break

# nested loops
import numpy as np

for x, y in np.ndindex((3, 2)):
    print(x, y)

# while loop
count = 0
while count < 5:
    print(count, " is  less than 5")
    count += 1
else:
    print(count, " is not less than 5")
