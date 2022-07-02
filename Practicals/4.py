"""
Bubble Sort
"""
# Code Starts Here

# By School
a = int(input("Enter the number of element you want to be entered : "))
li = []
for i in range(a):
    val = int(input("Enter the value : "))
    li.append(val)
for i in range(a):
    for j in range(a-i-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print(li)
