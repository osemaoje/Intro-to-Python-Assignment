# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2
    else:
        return "Invalid operation!"

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} is: {result}")
except ValueError:
    print("Invalid input! Please enter numerical values.")
