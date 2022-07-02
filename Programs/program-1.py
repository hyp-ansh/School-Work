# Program 1 : Program to display the output of arithmetic operations
# Basic Arithmetic Calcuator
result = None
num1 = float(input("Enter first number -> "))
num2 = float(input("Enter second number -> "))
op = input("Choose one arthmetic operation [+] [-] [*] [/] [//] [%] -> ")
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Enter number other than 0")
    else:
        result = num1 / num2
elif op == "//":
    result = num1 // num2
elif op == "%":
    result = num1 % num2
else:
    print("UnknownInputError")

print(f"Solution -> {result}")