"""
WAP to create a dictionary containing name of the competition 
winner student's name as key and number of their wins as value.
"""

# Code Starts Here

# Using for loop
n = int(input("Enter number of students (winners) > "))
winList = {}
for i in range(n):
    name = input("Enter winner's name > ")
    wins = int(input(f"Number of time {name} won > "))
    winList[name] = wins
print(winList)

# Using while loop
total = int(input("Enter number of students (winners) > "))
added = 0
winList = {}
while added != total: 
    name = input("Enter winner's name > ")
    wins = int(input(f"Number of time {name} won > "))
    winList[name] = wins
    added+=1
print(winList)