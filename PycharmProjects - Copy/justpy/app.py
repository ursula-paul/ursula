import math

price = 10
rating = 4.9
print (price)
name ='Mosh'
is_published = False
print("Ursula Paul")

#Firstname = 'John'
#color ='blue'
Age = 22
is_new = True

#get input

#input( 'What is your name?')
#print ('Hi ' + Firstname)
#input ('what is your favorite color ?')
#print (Firstname+ ' likes ' + color)

#my_name = input('What is your name?')
#favorite_color = input('What is your favorite color ?')
#print (my_name + ' likes ' + favorite_color)

# type conversation
#birth_year = input('Birth year: ' )
#print(type(birth_year))
# 2000
#age = 2024 - int(birth_year)
#print(type(age))
#2024 - 2024
#print(age)

#weight_lbs = input('(lbs): ' )
#print(type(weight_lbs))
#weight_kg = float(weight_lbs) *  0.45
#print(type(weight_kg))
#print(weight_kg)

course = 'Python for Beginners'
#         012345
another = course [:]
# returns all characters in the column

print (course[0:3])
# [0:3] this would run all the characters from 0 to 3 but exclude the third character
#print (course[0:])
print (another)
print (course[0:6])

First_name = 'Ursula'
Last_name = 'Paul'
message = First_name + ' ' + Last_name + '  is a developer'
messages = First_name + ' [ ' + Last_name + ' ] is a coder'
msg = f'{First_name} {Last_name} is a python developer'
# formatted string for readablity
print (message )
print (messages)
print(msg)

course = 'python for beginners'
print (course) # prints the course the way it was written
print (len(course)) # print length of course
print(course.capitalize()) # capitalize only the first letter
print(course.upper()) # converts the whole letters to uppercase
print(course.lower()) # converts to lower case
#print(course.find('P')) # prints the result of the first character
# find() method is case sensitive/ returns the index of the character or sequence of characters
print(course.replace('beginners','expert'))
#replace() is case sensitive
# to check if a character exist in a string
print('python' in course)# returns s boolean value

# number
#print(10/3)
#print (10//3)
#print (10%3)
#print (10**3)

# increment
x = 10
x = x + 3
print (x)
p = 5
p += 3
print (p)
r = 4
r -= 2
print (r)

#Operator Precedence #BODMAS
t = 10 + 3 * 2 ** 2
k = (10 + 3) * 2 ** 2
print (t)
print (k)

# Parenthesis
# Exponent
# Multiplication or Division
# Addition or Subtraction

g = (2+3) * 10-3
print (g)

# Math functions
y =2.10
print(round(y))

is_hot = False
is_cold = False
# as long as one of the condition is true it will run
if is_hot:
    print('it is a hot day')
    print ('drink plenty of water')
elif is_cold:
    print('it is a cold day ')
    print('wear warm cloths')
else:
   print('it is a lovely day')
print('enjoy your day')

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment : ${down_payment}")

# Logic operator
# And both condition is true
# Or one condition is true
# Not automatically converts to either true or false

has_good_credits = True
has_criminal_record = False

if has_good_credits and not has_criminal_record:
    print('Eligible for loan')

# comparisons operator (compare variable witt value )

temperature  = 35

if temperature == 30:
    print('it is a hot day')
else:
    print('it is not a hot day ')

#input('what')

name = 'ruy'

if len(name) < 3 :
    print ('name must be at least 3 characters long')
elif len(name) >50:
    print('name can be a maximum of 50')
else:
    print('name looks good ')

# While Loops

i = 1
while i <=5:
     print(i)
     i = i +1
print('Done')

# we use while loop to execute a block of code multiple times
secret_number =9
guess_count =0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    print ('try again')
    guess_count +=1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('sorry you failed')

# for loop to iterate items of a collection such as a string
# we can iterate over strings, arrays and numbers

#for item in [1,2,3,4,5]:
#    print (item)

#for item in 'python':
 #   print(item)
# 0 -> where the range starts
# 20 -> where it stops except that it does not print the last number e.g 20
# 3 -> step this means that it would go in three's
#for item in range(0,20,3):
    #print(item)

#calculate all the items in a shopping cart

prices= [10,20,30]
total =0
for price in prices:
    total += price
print(f"Total:{total}")




