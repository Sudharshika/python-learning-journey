
# Day 5: Relational & Logical Thinking

# Problem 1:
# Take two numbers from the user.
# Convert them to integers.
# Print whether:
# - Both numbers are equal
# - The numbers are different
# - The first number is greater than the second number
# - The first number is smaller than the second number
num1 = input("num1: ")
num2 = input("num2: ")

num1 = int(num1)
num2 = int(num2)

print("Both numbers are equal: ",num1==num2) 
print("The numbers are different: ",num1!=num2) 
print("The first number is greater than the second number: ",num1>num2) 
print("The first number is smaller than the second number: ",num1<num2) 




# Problem 2:
# Take three numbers from the user.
# Print whether:
# - The first number is greater than both the other numbers
# - At least one of the last two numbers is greater than the first number
first_number = int(input("First number: "))
second_number = int(input("Second number: "))
third_number = int(input("Third number: "))

print("The first number is greater than both the other numbers: ", second_number < first_number and third_number < first_number)
print("At least one of the last two numbers is greater than the first number: ", second_number > first_number or third_number > first_number)




# Problem 3:
# Take one number from the user.
# Print whether:
# - The number is NOT greater than 10
# - The number lies between 5 and 15 (both limits included)
number = int(input("Enter a number: "))

print("The number is NOT greater than 10: ",number<=10)

if(5<=number<=15):
    print("The number lies between 5 and 15 ")

