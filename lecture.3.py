#while loop
i= 1
while i <= 6:
    print('*' * i )
    i = i + 1
print("Done")

#gueesing game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won! ')
        break
else:
    print("Sorry! You failed!")


########### car game ##############
command = ""
while True:
    command = input ("> "). lower()
    if command == "start":
        print("car started....")
    elif command == "stop":
        print("car stopped....")
    elif command == "help":
        print('''
start - To start the car
stop - To stop the car
quite - To quite
        ''')
    elif command == "quite":
        break
    else:
        print(" sorry, i don't understand that!")

command = ""
started = False
while True:
    command = input ("> "). lower()
    if command == "start":
        if started:
            print("car already started!")
        else:
            started = True
            print("car started....")
    elif command == "stop":
        if not started:
            print("car already stopped!")
        else:
            started = False
            print("car stopped....")
    elif command == "help":
        print('''
start - To start the car
stop - To stop the car
quite - To quite
        ''')
    elif command == "quite":
        break
    else:
        print(" sorry, i don't understand that!")

########## for loops############

for item in range(5 , 10 ):              # for item in 'python'
    print(item)                          # for item in [ 1, 2, 3, 4, 5]
                                        # for item in range ( 5, 10, 2)

 # question calculate the total cost of all the items in shopping cart?

prices = [ 10, 20 , 30]
total = 0

for price in prices:
    total += price
print(f"Total:{total}")

###### nested loops##########

for x in range (4):
    for y in range(3):
        print(f'({x} , {y})')

#imp question
numbers = [ 5, 3, 5, 2, 4, 2, 2]
for x_count in numbers:
    print('x' * x_count  )

numbers = [5, 3, 5, 2, 4, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)