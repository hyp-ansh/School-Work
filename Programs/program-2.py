# Program to enter the string and check if it's a palindrome or not using or not using 'for' loop
msg = input("Enter a string : ")
newlist = []
newlist[:0] = msg
l = len(newlist)
ed = l-1
for i in range(0,1):
    if newlist[i] != newlist[ed]:
        print("Given string is not palindrome")
        break
    if i <= ed:
        print("Given string is a palindrome")
        break
    l = l - 1
    ed = ed - 1