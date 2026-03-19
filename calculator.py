def add(a, b):
    """
    Adds two numbers and returns the result.VVVCXVXC
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second.
    Includes basic error handling for division by zero.
    """
    # Prevent application crash if user tries to divide by zero
    if b == 0:
        return "Error: Cannot divide by zero!"
    
    return a / b

if __name__ == "__main__":
    print("Testing calculator module...")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 / 0 = {divide(10, 0)}")
