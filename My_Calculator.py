num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
Operator = input("Enter operator (+, -, *, /): ")

if Operator == '+':
    print(num1 + num2)
elif Operator == '-':
    print(num1 - num2)
elif Operator == '*':
    print(num1 * num2)
elif Operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
