def square(number):
    return number * number

print (square(3))

# exception (error handling)
# in python exist code 0 means successful and anything apart from 0 like(1) means crash/failed
# use comments to explain why's and how's not what's
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')
