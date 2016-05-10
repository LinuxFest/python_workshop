# print
print "hello world"

integer_var = 2
float_var = 2.5
string_var = "SampleString"
name = "ali"
age = 20

print "This is an integer variable: %d" % integer_var
print "This is an float variable: %f" % float_var
print "This is an string variable: %s" % string_var
print "%s is %d years old." % (name, age)

print string_var[2:9]  # print from second index to ninth index (index begins from 0)
print name[:-1]  # remove last character

print name[::-1]  # reverse string

# lists
integer_list = [1, 3, 5, 7]
integer_list.append(9)
integer_list.insert(2, 4)
print integer_list

# Stack
stack_list = [1, 2, 3, 4]
integer_list.append(5)  # insert item to stack
num = integer_list.pop()
print num

# Queue
from collections import deque

queue_list = deque([1, 2, 3, 4])
queue_list.append(5)  # insert item to stack
queue_list.popleft()
print queue_list

# tuples


# dictionaries
students = {"sina": 9131062, "farzan": 9131069}
students["sajjad"] = 9231049

for name, std_num in students.iteritems():
    print "name: %s, std_num: %d" % (name, std_num)

del students["sina"]
print students
