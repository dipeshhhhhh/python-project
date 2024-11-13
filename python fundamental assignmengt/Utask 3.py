def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle division by zero
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    while True:
        # Display menu
        print("\nSimple Calculator")
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Get user input for operation selection
        operation = input("Enter choice (1/2/3/4/5): ")

        # Check if user wants to exit
        if operation == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Validate operation selection
        if operation not in ['1', '2', '3', '4']:
            print("Invalid input! Please select a valid operation (1/2/3/4).")
            continue

        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform selected operation
        if operation == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")

# Call the calculator function to start the program
if __name__ == "__main__":
    calculator()
