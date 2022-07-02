"""
WAP that takes 2 integers from  user and prints the message 
saying first number is divisible by second number or not.
"""

# Code Starts Here

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 % num2 == 0:
    print("First number is divisible by second number")
else:
    print("First number is not divisible by second number")
