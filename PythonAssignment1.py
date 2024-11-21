# Basic Calculator Program
print("Welcome to my Basic Calculator!")

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose a mathematical operation
print("Choose an operation: + for addition, - for subtraction, * for multiplication, / for division")
operation = input("Enter the operation: ")

# Perform the operation and display the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please choose +, -, *, or /.")

print("Thank you for using my Basic Calculator!")
