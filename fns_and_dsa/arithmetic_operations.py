def add(num1: float, num2: float) -> float:
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    return num1 * num2

def divide(num1: float, num2: float) -> float:
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def perform_operation(num1: float, num2: float, operation: str) -> float:
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    # Check if the operation is valid
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."

# Example usage:
# result = perform_operation(10, 0, 'divide')
# print(result)  # Output: Error: Division by zero is not allowed.
  
