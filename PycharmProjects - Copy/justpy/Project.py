# Build a project that converts someone weight form pounds to kilogram
# User converts weight to kilogram or pounds
#example

#Weight: 72
#(L)bs or (K)g:
# You are 160.0 pounds

#weight_lbs = input('(lbs): ' )
#print(type(weight_lbs))
#weight_kg = float(weight_lbs) *  0.45
#print(type(weight_kg))
#print(weight_kg)

#weight_pounds = input('(pounds): ')
#weight_kg = float(weight_pounds) * 2.20462
#msg = f'you are {weight_kg} pounds'
#print(msg)

#weight = int(input('weight ' ))
#unit = input('(L)bs or (k)g: ')
#if unit.upper() == 'L':
 #   converted = weight *0.45
  #  print(f" you are {converted} kilos")
#else:
 #   converted = weight /0.45
  #  print(f'you are {converted} pounds')

# Print a number that guess a number right


#secret_number = 9
#guess_count = 0
#guess_limit = 3

#while guess_count < guess_limit:
 #   guess = int(input('Guess: '))

  #  if guess == secret_number:
   #     print('You won!')
    #    break
    ##   print('Try again')

    #guess_count += 1

#if guess != secret_number:
    #print('Sorry, you failed')

command = ''
started = False
while True:
    command = input('type anything ').lower()
    if command == 'start':
        if started:
            print('car is already started ')
        else:
            started = True
            print ('Car Started.....')
    elif command == 'stop':
        if not started:
            print('car is already stopped .')
        else:
            started  = False
            print ('Car Stopped')
    elif command == 'help':
        print (""" 
Start - to start the car
Stop- to stop the car
Quit - to quit the car
        """)
    elif command == 'quit':
        break
    else:
        print("sorry i don't understand that ")




