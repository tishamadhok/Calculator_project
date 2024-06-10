import sys
from calculator.calculator import Calculator

def main(a: str, b: str, operation: str):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
        return

    try:
        if operation == 'add':
            result = Calculator.add(a, b)
        elif operation == 'subtract':
            result = Calculator.subtract(a, b)
        elif operation == 'multiply':
            result = Calculator.multiply(a, b)
        elif operation == 'divide':
            result = Calculator.divide(a, b)
        else:
            print(f"Unknown operation: {operation}")
            return
        print(f"The result of {a} {operation} {b} is equal to {result}")
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <a> <b> <operation>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
