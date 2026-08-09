# simple calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
operation = input("Enter an operation (+, -, *, /): ")
if operation == "+":
    result = float(num1) + float(num2)
    print(result)
elif operation == "-":
    result = float(num1) - float(num2)
    print(result)
elif operation == "*":
    result = float(num1) * float(num2)
    print(result)
elif operation == "/":
    result = float(num1) / float(num2)
    print(result)
else:
    print("Invalid operation")


