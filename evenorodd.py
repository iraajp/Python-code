def check_even_odd():
    while True:
        # Get user input
        user_input = input("Enter a number (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'q':
            print("Program terminated. Goodbye!")
            break
        
        # Try to convert input to an integer
        try:
            number = int(user_input)
            
            # Check if the number is even or odd
            if number % 2 == 0:
                print(f"{number} is an even number.")
            else:
                print(f"{number} is an odd number.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

# Run the program
if __name__ == "__main__":
    print("Even or Odd Number Checker")
    print("==========================")
    check_even_odd()