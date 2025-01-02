# if a function is not called it won't get executed


def greet_user1():
    print('Hi there'),
    print('welcome aboard')

print('Start')
greet_user1()
print('Finish')

# passing information to function

def greet_user2(first_name,last_name):
    print(f' Hi {first_name,last_name}!'), # this does not take priority
    print('welcome aboard')

print('Start')
greet_user2('John', 'Doe'), # this takes priority they are called (position argument)
greet_user2('Jane', 'Doe')
print('Finish')

# In position arguments the order at which they are positioned takes priority and it matters
# in key word arguments the order at positioned does not matter


def greet_user3(first_name,last_name):
    print(f' Hi {last_name,first_name}!'), # this does not take priority
    print('welcome aboard')

print('Start')
greet_user3(last_name = 'Doe', first_name='John')
greet_user3('Jane', 'Doe')
print('Finish')

def greet_user4(first_name,last_name):
    print(f' Hi {first_name,last_name}!'), # this does not take priority
    print('welcome aboard')

print('Start')
greet_user4(first_name = 'John', last_name='Doe')
greet_user4('Jane', 'Doe')
print('Finish')

# Global Variable

z = "awesome"

def myFunc():
    print("Python is " + z)
myFunc()

x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()

p = "awesome"

def myfunc():
  p = "fantastic"
  print("Python is " + p)

myfunc()

print("Python is " + p)

# if you use the global keyword inside a function  the variable belongs to the global scope

k ="great"
def myfunc():
  global k
  k = "wonderful"

myfunc()

print("Python is " + k)

u = 'awesome'
def myfunc():
  u = 'fantastic'
myfunc()
print('Python is ' + u)