# Reverse the string
st = input("Input the string : ")
for i in range(-1, -len(st)-1, -1):
    print(st[i],end='')
