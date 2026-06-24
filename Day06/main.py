
# Day 6: Assignment, Precedence & Input Practice

# Problem 1:
# Create a variable with an initial value of 10.
# Update the value by:
# - Adding 5 to it
# - Subtracting 3 from it
# - Multiplying it by 2
# - Dividing it by 4
# Print the value after each update.
x = 10
x += 5
print(x) #15

x -= 3
print(x) #12

x *= 2
print(x) # 24

x /= 4
print(x) # 6


# Problem 2:
# Without using extra variables, evaluate and print the result of:
# - 10 + 2 * 5
# - (10 + 2) * 5
# - 20 / 5 + 3 ** 2
# Observe how the results differ.

print(10 + 2 * 5) #10+10 = 20
print(( 10 + 2 ) * 5) #12*5 = 60
print(20 / 5 + 3 ** 2) #(20/5+9) = 4+9 = 13



# Problem 3:
# Take two numbers from the user.
# Calculate:
# - Their average
# - Their square difference (difference squared)
# Print both results with clear messages.

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
total = num1+num2
avg = total/2
square_difference = (num1- num2)**2

print(f"Average of {num1} and {num2} is ",avg)
print(f"Square difference of {num1} and {num2} is ",square_difference)
