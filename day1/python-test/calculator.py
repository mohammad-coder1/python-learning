print("simple calculator")


num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the first number:"))

print("Available operations: + - * /")
op = input("choose an operation:")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 !=0:
        print("Result:", num1 / num2 )
    else:
        print("Error: Division by zero is no allowed!")
else:
    print("Invalid operation.")
