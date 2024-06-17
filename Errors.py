def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Inputs must be numbers.")
    finally:
        print("Execution completed.")

# Example usage
divide_numbers(10, 2)   
# This will print the result and "Execution completed."
divide_numbers(10, 0)   
# This will print an error message and "Execution completed."
divide_numbers(10, 'a') 
# This will print an error message and "Execution completed."
