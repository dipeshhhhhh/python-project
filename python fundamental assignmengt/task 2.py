def classify_number():
    # Start a while loop that continues until the user types 'exit'
    while True:
        # Prompt the user for input
        user_input = input("Enter a number to classify (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop if the user types "exit"

        try:
            # Try to convert the user input to a float
            number = float(user_input)

            # Classify the number using if statements
            if number > 0:
                print("The number is positive.")
            elif number < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")
        except ValueError:
            # If the conversion to float fails (invalid input), prompt the user to try again
            print("Invalid input! Please enter a valid number or type 'exit' to quit.")

# Call the function to run the program
if __name__ == "__main__":
    classify_number()
