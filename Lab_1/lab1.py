# SYNTAX
#1
print("Hello World")
#2
if 5 > 2:
    print("Yes")
    
# COMMENTS
#1
# This is a comment
#2
"""
This is a comment
written in 
more than just one line
"""


# VARIABLES
#1
carname = "Volvo"
#2
x = 50
#3
x = 5
y = 10
print(x + y)
#4
x = 5
y = 10
z = x + y
print(z)
#5
x,y,z = "Orange", "Banana", "Cherry"
#6
x = y = z = "Orange"
#7
def myfunc():
  global x
  x = "fantastic"
  
  
# DATA TYPES
#1
x = 5
print(type(x))
# int
#2
x = "Hello World"
print(type(x))
# str
#3
x = 20.5
print(type(x))
# float
#4
x = ["apple", "banana", "cherry"]
print(type(x))
# list
#5
x = ("apple", "banana", "cherry")
print(type(x))
# tuple
#6
x = {"name" : "John", "age" : 36}
print(type(x))
# dict
#7
x = True
print(type(x))
# bool

# NUMBERS
#1
x = 5
x = float(x)
#2
x = 5.5
x = int(x)
#3
x = 5
x = complex(x)

# STRINGS
#1
x = "Hello World"
print(len(x))
#2
txt = "Hello World"
x = txt[0]
#3
txt = "Hello World"
x = txt[2:5]
#4
txt = " Hello World "
x = txt.strip()
#5
txt = "Hello World"
txt = txt.upper()
#6
txt = "Hello World"
txt = txt.lower()
#7
txt = "Hello World"
txt = txt.replace("H","J")
#8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# BOOLEANS
#1
print(10 > 9)
# true
#2
print(10 == 9)
# false
#3
print(10 < 9)
# false
#4
print(bool("abc"))
# true
#5
print(bool(0))
# false

# OPERATORS
#1
print(10 * 5)
#2
print(10 / 2)
#3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#4
if 5 != 10:
  print("5 and 10 is not equal")
#5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

  
# LISTS
#1
fruits = ["apple", "banana", "cherry"]
print(fruits)
#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# TUPLES
#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

# SETS
#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

# DICTIONARIES
#1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
#3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

# IF...ELSE
#1
a = 50
b = 10
if a > b:
  print("Hello World")
#2
a = 50
b = 10
if a != b:
  print("Hello World")
#3
a = 50
b = 10
if a != b:
  print("Yes")
else:
  print("No")
#4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
#5
c = 10
d = 10
if a == b and c == d:
  print("Hello")
#6
if 5 > 2:
  print("YES")
#7
a = 2
b = 5
print("YES") if a == b else print("NO")
#8
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")

# WHILE LOOP
#1
i = 1
while i < 6:
  print(i)
  i += 1

#2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# FOR LOOPS
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#3
for x in range(6):
  print(x)

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# FUNCTIONS
#1
def my_function():
  print("Hello from a function")

#2
def my_function():
  print("Hello from a function")

my_function()

#3
def my_function(fname, lname):
  print(fname)

#4
def my_function(x):
    return x + 5

#5
def my_function(*kids):
  print("The youngest child is " + kids[2])

#6
def my_function(kid):
  print("His last name is " + kid["lname"])

# LAMBDA
#1
x = lambda a : a

# CLASSES
#1
class MyClass:
  x = 5

#2
class MyClass:
  x = 5

p1 = MyClass()

#3
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#4
class Person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age

# INHERITENCE
#1
class Student(Person):
    pass
#2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


# MODULES
#1
import mymodule

#2
import mymodule as mx

#3
import mymodule
print(dir(mymodule))

#4
from mymodule import person1



 