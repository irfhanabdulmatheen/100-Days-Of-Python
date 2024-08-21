print("Enter the first number: ")
num1 = float(input())

print("Enter the second number: ")
num2 = float(input())

print("Enter the operation (+, -, *, /): ")
operation = input()

if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")

