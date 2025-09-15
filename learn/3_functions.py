# Functions

# 11. Write a function to calculate the square of a number.
def square_number():
    def square(num):
        return num * num
    number = int(input("Enter a number: "))
    print(f"Square of {number} is {square(number)}")

# 12. Create a function that returns whether a number is palindrome or not.
def is_palindrome():
    num = int(input("Enter a number: "))
    check = str(num) == str(num)[::-1]
    if check:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")

# 13. Implement a function to calculate power of a number (x^y) without using built-in functions.
def power_number():
    def power(x, y):
        result = 1
        for _ in range(y):
            result *= x
        return result
    base = int(input("Enter base (x): "))
    exponent = int(input("Enter exponent (y): "))
    print(f"{base}^{exponent} = {power(base, exponent)}")
