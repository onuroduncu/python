#variables
#---------------
"""
we don't have to write the variables as following.
121abc
-abc
+abc
*abc
/abc
ğİç -->no turkish characters
abs -->function in python
1234
a b c
we should wrtite as following.
_abc
abc
a1

variable notations
------------------------
mySecretWorld -->camelcase
MySecretWorld -->pascal notation
PI_NUMBER or pi_number -->snake(underscore) notation
intTotal or strTotal -->hungarian notation
PINUMBER --> uppercase
pinumber --> lowercase
"""
#error
#print = "Hello world" #TypeError: 'str' object is not callable
#print("hi") 

a = "Hello world"
print(a) #Hello world
print(type(a)) #<class 'str'>

b = 5
print(type(b)) #<class 'int'>
c = 4.7
total = b + c
print(total) #9.7
mult = b * c
print(mult) #23.5
div = b / c
print(type(div)) #<class 'float'>
print(div) #1.0638297872340425
abst = b - c
print(abst) #0.2999999999999998
print(total * 2) #19.4
