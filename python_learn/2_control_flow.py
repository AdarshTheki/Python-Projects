# Control Flow (if, for, while)

# 7. Write a program to calculate the factorial of a number using a for loop.
def factorial_number():
    num = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")

# 8. Write a program to check if a number is prime or not.
def is_prime_number():
    num = int(input("Enter a number: "))
    if num <= 1:
        print(f"{num} is not a prime number")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

# 9. Write a program to print Fibonacci numbers up to the 10th term.
def fibonacci_sequence():
    n_terms = 10
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n_terms):
        print(a, end=" ")
        a, b = b, a + b

# 10. Write a program that prints a multiplication table of a given number.
def print_multiply_tables():
    num = int(input("Enter the number for multiplication table: "))
    print(f"Multiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

