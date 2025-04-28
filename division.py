def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Invalid input"

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = safe_division(num1, num2)
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter valid numbers")