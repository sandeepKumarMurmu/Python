'''
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
'''

x = 5
y = "John"
print(x)
print(y)


# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# example
y = 4       # y is of type int
y = "Sally" # y is now of type str
print(y)


'''
# Casting
If you want to specify the data type of a variable, this can be done with casting.
'''
a = int(1)
b = str("python")
c = float(3)

print("int : ",a)
print("str : ",b)
print("float : ",c)


'''
# Get the Type
You can get the data type of a variable with the type() function.
'''

print("type of a : ",type(a))
print("type of b : ",type(b))
print("type of c : ",type(c))


'''
# Single or Double Quotes?
String variables can be declared either by using single or double quotes:
'''

string = "test"
# same as 
string1 = 'test'

'''
# Case-Sensitive
Variable names are case-sensitive.
'''
t = 4
# not same as 
T = 4

###### Python Variables - Assign Multiple Values
# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
t1, t2, t3 = 'test1', 'test2', 'test3'
print("t1 : ",t1)
print("t2 : ",t2)
print("t3 : ",t3)


'''
# One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
'''

p1 = p2 = p3 = 'same variable testing'
print("p1 : ",p1)
print("p2 : ",p2)
print("p3 : ",p3)

'''
# Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
'''

fruits = ['orange', 'apple', 'mango']
f1, f2, f3 = fruits
print("f1 : ",f1)
print("f2 : ",f2)
print("f3 : ",f3)


'''
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
'''
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

'''
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain as it was, 
global and with the original value.
'''

'''
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
'''