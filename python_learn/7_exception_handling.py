# Exception Handling

# 25. Write a program to handle division by zero error.
def division_by_zero_error():
    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        result = numerator / denominator
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# 26. Write a program to handle multiple exceptions using try-except blocks.
def muti_exception_error():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")

