# Day 3: Conditionals
# Problem 1: Check if a number is even or odd.
number = 90

if(number%2==0):
    print(number, "number is even")
else:
    print(number, "number is odd")

# Problem 2: Find the largest of three numbers.
num1 = 49
num2 = 54
num3 = 50

if(num2<num1 and num3<num1 ):
    print("num1 is largest.")
elif(num1<num2 and num3<num2):
    print("num2 is largest.")
else:
     print("num3 is largest.")

# Problem 3: Write a simple grading program: input a score and print “Pass” if ≥ 50, otherwise “Fail”.
score = int(input("Enter your score: "))
if(score>=50):
    print("Pass")
else:
    print("Fail")