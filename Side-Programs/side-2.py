def charCount(ch, st):
    count = 0
    for char in st:
        if ch == char: count += 1
    return count
st = input("Enter the string : ")
ch = input("Which character to count : ")
Count = charCount(ch,st)
print(f"In string '{st}': '{ch}' is {Count} times")