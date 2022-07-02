"""
WAP that asks the user the day number of the year from range 2 - 365 and ask the first 
day of the year (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday). 
Then the program should display the day on the day number that has been given.
"""

# Code Starts Here

in_day = input("Enter the first day of the year : ").lower()
no_day = int(input("Enter the day number [2-365]: "))

noxday = {1:"sunday", 2:"monday", 3:"tuesday", 4:"wednesday", 5:"thursday", 6:"friday", 7:"saturday"}
dayxno = {"sunday":1, "monday":2, "tuesday":3, "wednesday":4, "thursday":5, "friday":6, "saturday":7}

day_by_7 = no_day % 7

for i in dayxno: 
    if in_day == i: day_by_7 += (dayxno[i]-1)

if day_by_7 > 7: day_by_7 -= 7

print(f"{no_day}th day is {noxday[day_by_7]}")
