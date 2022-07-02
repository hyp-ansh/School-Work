# Program to find the sum of all the positive numbers entered by
# the user. As soon as the user enters a negetive number, 
# stop taking in an further input from the user and display sum

entry = 0
sum1 = 0
print("Enter number to find their sum, negetive number ends the loop:")
while True:
    entry = int(input())
    if entry < 0:
        break
    sum1 += entry
print(f"Sum = {sum1}")
"""
<<OUTPUT>>
Enter number to find their sum, negetive number ends the loop:
3
4
5
-1
Sum = 12
"""