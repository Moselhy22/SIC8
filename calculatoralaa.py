num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("choose an operator (+, -, *, /, //, **, %): ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    print("Result:", num1 / num2)
elif op == '//':
    print("Result:", num1 // num2)
elif op == '**':
    print("Result:", num1 ** num2)
elif op == '%':
    print("Result:", num1 % num2)
else:
        print("Make sure you select the operator")