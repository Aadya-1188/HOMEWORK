#using a try and except for age 
try:
    number = int(input("Enter your age:"))
    print("Your age is:" , number)

#using value error
except ValueError as ex:
    print("Exception:" , ex)