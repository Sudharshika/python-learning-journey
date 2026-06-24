# Day 4: Type Casting & Arithmetic Operators

# Problem 1:
# Take two numbers from the user.
# Convert them to integers.
# Print their:
# - Sum
# - Difference
# - Product
# - Division result

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

num1 = int(num1)
num2 = int(num2)

sum_of_nums = num1 + num2
difference = num1 - num2
product = num1 * num2
division_result= num1 / num2

print("Sum: ",sum_of_nums)
print("Difference: ",difference)
print("Product: ", product)
print("Division result: ",division_result)


# Problem 2:
# Take one number from the user.
# Convert it to float.
# Print:
# - The value
# - Its type
# - The square of the number
number = int(input("Enter a number: "))
number = float(number)

print("Value: ",number)
print("Type: ", type(number))

square_number = number**2
print("square of the number is ",square_number)


# Problem 3:
# Take two numbers from the user.
# Convert both to integers.
# Print:
# - Remainder when first number is divided by second number
# - Power result (first number raised to second number)
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

num1 = int(num1)
num2 = int(num2)

remainder = num1 % num2
print("When first number is divided by second number, remainder is ",remainder)

power_result = num1**num2
print("First number raised to second number, the result is ",power_result)
