def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def main():
    print("=== Simple Calculator ===")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("Choose operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    choice = input("Enter operation (1/2/3/4 or + - * /): ")

    if choice in ['1', '+']:
        result = add(num1, num2)
    elif choice in ['2', '-']:
        result = subtract(num1, num2)
    elif choice in ['3', '*']:
        result = multiply(num1, num2)
    elif choice in ['4', '/']:
        result = divide(num1, num2)
    else:
        print("Invalid operation selected.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
