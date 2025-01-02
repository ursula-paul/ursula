#from justpy.List import numbers
# append adds at the last of the list
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

#insert add in middle or begining
numbers1 = [5, 2, 1, 7, 4]
numbers1.insert(0,10)
print(numbers1)

# remove: removes an item
numberss = [5, 2, 1, 7, 4]
numberss.remove(5)
print(numberss)

#clear: empties the list
numberss1 = [5, 2, 1, 7, 4]
numberss1.clear()
print(numberss1)

#pop: removes the last item in the list
numberrs = [5, 2, 1, 7, 4]
numberrs.pop()
print(numberrs)

#index: to check for the existence of our list or in
numberrs1 = [5, 2, 1, 7, 4]
print(numberrs1.index(5))

#in this returns a boolean
numberrs11 = [5, 2, 1, 7, 4]
print(50 in numberrs11 )

#count: to count the occurance of a number
numbberrs11 = [5, 2, 5, 1, 7, 5, 4]
print(numbberrs11.count(5))

#sort: to sort numbers ( the sort method sort the numbers in assending order)
# but to sort in decending order you add reverse
numbberrss11 = [5, 2, 5, 1, 7, 5, 4]
numbberrss11.sort()
numbberrss11.reverse()
print(numbberrss11)

#copy creates a new list
numbbeerrss11 = [5, 2, 5, 1, 7, 5, 4]
numbbeerrss112 = numbbeerrss11.copy()
numbbeerrss11.append(10)
print(numbbeerrss112)
print(numbbeerrss11)

#Write a program to remove the duplicate in a program
num = [5, 2, 2, 5, 1, 1, 7, 7, 5, 4, 4,8]

seen = set() # does not accept duplicate
unique_num = []
for n in num: # for n(5) in num
    if n not in seen: # if n(5) is not in seen
        unique_num.append(n) # add to unique_num [n:5], n:2
        seen.add(n) # add to see [n:5]. n:2
print (unique_num)

numbers = [2,2,4,6,3,4,6,1]
uniques =[]
for number in numbers: #  number(2) in numbers
    if number not in uniques: # if 2 is not in unique
        uniques.append(number) # number:2
        uniques.sort()
print(uniques)


