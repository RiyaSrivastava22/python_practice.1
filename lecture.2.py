#logical operators
#if applicant has high income AND good credit eligible for loan
from pickletools import long1

has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")

# AND: both
# OR: at least one

#if applicant has good credit AND doestn't have a criminal record
has_good_credit = True
has_criminal_record = False
#
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

#if temperature is greater than 30
# it's a hot day
# otherwise if it's less than 10
# it's a cold day
# otherwise
# it's neither hot nor cold

temperature = 50
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# if name is less than 3 characters long
#     name must be at least 3 characters
# otherwise if its more than 50 characters long
# name can be maximum of 50 characters
# otherwise
# name looks good!

#solution
name = "Riya Srivastava"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")

#project: weight converter

weight = int(input('weight: '))
unit = input('(L)bs or (K)g:')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")


