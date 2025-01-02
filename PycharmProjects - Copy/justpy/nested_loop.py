for x in range(4): # 0,1,2,3
    for y in range(4): #0,1,2,3
        print (f"({x},{y})")

numbers = [5,2,5,2,2]
for x_count in numbers:
    #print(numbers)
    output =''
    for count in range(x_count):
        #print(count)
        output += 'x'
    print (output)

num = [1,2,3,4,5]
print (num[2:3])

names = ['John', 'Ursula', 'Mosh', 'Sarah', 'Bob']
names [0] = 'Jon'
print (names)
#print(names[2:4])
# when we use square brackets [] we get a new list it does not modify a list

