# Modules & Packages

# 29. Write a Python script to import the math module and compute square root of a number.
def module_square_root():
    import math
    num = float(input("Enter a number: "))
    sqrt = math.sqrt(num)
    print(f"Square root of {num} is {sqrt}")

# 30. Write a custom module with functions for addition and subtraction, and import it in another script.
def module_export_fn():
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    return {add,subtract}

