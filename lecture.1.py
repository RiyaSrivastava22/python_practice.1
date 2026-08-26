your_name = input("what is your name? ")
favorite_color = input("what is your favourite color? ")
print(your_name  + " likes " + favorite_color )

#Type conversion
Birth_year = input("what is your birth year? ")
print(type(Birth_year))
age = 2026 - int(Birth_year )
print(type(age))
print(age)

#weight in kg
weight_kg = input("weight_kg")
weight_lbs = int(weight_kg) * 0.45
print(weight_lbs)
course = "python for Beginner"
print(course[0:6])
another = course[:]
print(another)

#formatted string
first = "riya"
last = "srivastava"
message = first + '[' + last + '] is a coder'
msg = f'{first} [{last}] is a coder '
print (msg)
print(message)
# string method
course = 'python for beginners'
print(len(course))
print(course.upper())
print(course)
print(course.find('p'))
print(course.replace(' beginner' , ' absolute beginner'))
print ('python' in course)  # space and uppercase , lowercase matters


#Arithmetic operations
x = 10 + 2* 2 ** 3
x = ( 2 + 3 ) * 10 - 3
print(x)

is_hot = False
is_cold = False

if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it is a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")
print("Enjoy your day")

# Question * price of the house is $1M.
# if buyer has good credit,
# they need to put 10%
# otherwise
# they need to put down 20%

#soution
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment: ${down_payment}")
