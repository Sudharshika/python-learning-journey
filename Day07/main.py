# Day 7: Introduction to if Statement

# Problem 1:
# Take a number from the user.
# If the number is greater than 0,
# print "Positive number".
number = int(input("Number: "))
if(number>0):
    print("Positive number")
else:
    print("Negative number")

# Problem 2:
# Take a number from the user.
# If the number is divisible by 5,
# print "Divisible by 5".
number = int(input("Number: "))
if(number%5==0):
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Problem 3:
# Take the user's age as input.
# If the age is 18 or more,
# print "Eligible to vote".
age = int(input("Enter your age: "))
if(age>=18):
    print("Eligible to vote.")
else:
    print("Not Eligible to vote")
