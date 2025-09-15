# Variables, Data Types & Operations
# 1. Write a Python program to swap two variables without using a third variable.
def swap_variable():
    a = 5
    b = 10
    a = a + b  # a = 15
    b = a - b  # b = 5
    a = a - b  # a = 10
    print("a =", a)  # Output: a = 10
    print("b =", b)  # Output: b = 5

# 2. What are mutable and immutable types in Python? Give examples. list, dist, set - mutable & int float, str & tuple - immutable datatype
def is_immutable_variable():
    # Mutable Example (List)
    my_list = [1, 2, 3]
    my_list[0] = 100
    print(my_list)  # Output: [100, 2, 3]

    # Immutable Example (String)
    my_str = "hello"
    # my_str[0] = 'H'  # This will raise an error
    new_str = 'H' + my_str[1:]
    print(new_str)  # Output: Hello

# 3. Write a program to check whether a number is odd or even.
def check_even_or_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# 4. Write a program to find the largest of three numbers.
def largest_three_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    print("Largest number is:", largest)

# 5. Perform string slicing, and reverse a string using slicing.
def reverse_or_slicing_str():
    text = "Artificial Intelligence"

    # Slicing (Example: first 10 characters)
    sliced_text = text[:10]
    print("Sliced Text:", sliced_text)  # Output: Artificial

    # Reverse String
    reversed_text = text[::-1]
    print("Reversed Text:", reversed_text)

# 6. Create a list of numbers from 1 to 100 and print all even numbers.
def list_of_even_number():
    numbers = list(range(1, 101))
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(even_numbers)

# ****************************************************************************************
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

# ****************************************************************************************
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

# ****************************************************************************************
# Data Structures (List, Tuple, Set, Dict)

# 14. Remove duplicates from a list.
def remove_duplicate_list():
    my_list = [1, 2, 2, 3, 4, 4, 5]
    unique_list = list(set(my_list))
    print("List without duplicates:", unique_list)

# 15. Merge two dictionaries into one.
def merge_two_dict():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)

# 16. Count frequency of elements in a list using a dictionary.
def count_frequency():
    my_list = [1, 2, 2, 3, 3, 3, 4]
    frequency = {}
    for item in my_list:
        frequency[item] = frequency.get(item, 0) + 1
    print("Element frequencies:", frequency)

# 17. Write a program to sort a list of dictionaries by a key.
def sort_list_dict():
    students = [
        {'name': 'Alice', 'score': 88},
        {'name': 'Bob', 'score': 75},
        {'name': 'Charlie', 'score': 95}
    ]
    sorted_students = sorted(students, key=lambda x: x['score'])
    print("Sorted by score:")
    for student in sorted_students:
        print(student)

# 18. Perform set operations: union, intersection, difference.
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (set1 - set2):", set1 - set2)

# ****************************************************************************************
# File Handling

# 19. Write a program to read a file line by line and print the content.
def read_text_file():
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.strip())

# 20. Write a program to count the number of words in a file.
def count_word_file():
    with open('sample.txt', 'r') as file:
        content = file.read()
    word_count = len(content.split())
    print(f"Number of words in file: {word_count}")

# 21. Write a program to append text to an existing file.
def append_text_file():
    with open('sample.txt', 'a') as file:
        file.write("\nThis line is appended.")
    print("Text appended successfully.")

# ****************************************************************************************
# OOP (Object-Oriented Programming)

# 22.Create a class Car with attributes like brand, model, and methods to display details.
def class_create():
    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model
        def display_info(self):
            print(f"Car Brand: {self.brand}, Model: {self.model}")
    # Example Usage
    my_car = Car("Toyota", "Corolla")
    my_car.display_info()

# 23. Implement inheritance: Create a Vehicle class and inherit Car from it.
def class_inheritance():
    class Vehicle:
        def __init__(self, brand):
            self.brand = brand
        def show_brand(self):
            print(f"Vehicle brand: {self.brand}")
    class Car(Vehicle):
        def __init__(self, brand, model):
            super().__init__(brand)
            self.model = model
        def show_car_info(self):
            print(f"Car Model: {self.model}")
    my_car = Car("Honda", "Civic")
    my_car.show_brand()
    my_car.show_car_info()

# 24. Use encapsulation to make class attributes private.
def class_encapsulation():
    class Person:
        def __init__(self, name, age):
            self.__name = name  # Private attribute
            self.__age = age  # Private attribute
        def get_info(self):
            return f"Name: {self.__name}, Age: {self.__age}"
    person = Person("Alice", 30)
    print(person.get_info())
    # Attempting to access private attribute directly (will raise error)
    # print(person.__name)  # AttributeError

# ****************************************************************************************
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

# ****************************************************************************************
# List Comprehensions & Lambda

# 27. Generate a list of squares of even numbers between 1 and 20 using list comprehension.
def square_list_even_number():
    squares = [x ** 2 for x in range(1, 21) if x % 2 == 0]
    print("Squares of even numbers from 1 to 20:", squares)

# 28. Write a lambda function to check whether a number is even.
def lambda_check_even():
    is_even = lambda x: x % 2 == 0
    num = int(input("Enter a number: "))
    print(f"{num} is even? {is_even(num)}")

# ****************************************************************************************
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

# ************************************************************************
# Generators & Iterators

# 31. Generator to Yield First N Fibonacci Numbers
def yield_fibonacci():
    def fibonacci_generator(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    for number in fibonacci_generator(10):
        print(number, end=" ")

# 32. Custom Iterator Class to Iterate Even Numbers up to N
def class_even_number():
    class EvenNumber:
        def __init__(self, max_sum):
            self.max_sum = max_sum
            self.current = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.current > self.max_sum:
                raise StopIteration
            number = self.current
            self.current += 2
            return  number
    for i in EvenNumber(10):
        print(i, end=" ")

# ************************************************************************
# Decorators

# 33. Decorator to Measure Execution Time
def measure_execution_time():
    import time

    def execution_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Execution Time: {end - start :.4f} seconds")
            return result
        return wrapper

    @execution_time
    def compute_sum(n):
        return sum(range(n))

    print(compute_sum(12123))

# 34. Decorator That Prints Start and End Messages
def start_end_decorator():
    def decorator_func(func):
      def wrapper(*args, **kwargs):
        print("start function")
        result = func(*args, **kwargs)
        print("end function")
        return result
      return wrapper

    @decorator_func
    def greet(name):
        print(f"Hello, {name}!")
    greet('Adarsh')

# ************************************************************************
# Multithreading & Multiprocessing

# 35. Multiple threaded Program to Print Numbers 1 to 10 from Two Threads
def multi_threaded_print():
    import threading

    def print_number():
        for i in range(1, 11):
            print(i)

#     create two thread
    t1 = threading.Thread(target=print_number)
    t2 = threading.Thread(target=print_number)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 36 Multiprocessing to Compute Squares in Parallel
def multi_processing_pool():
    from multiprocessing import Pool

    def square(n):
        return n * n

    if __name__ == '__main__':
        numbers = [1, 2, 3, 4, 5]
        with Pool() as pool:
            result = pool.map(square, numbers)
        print("Squares:", result)

# ************************************************************************
# Regular Expressions

# 38. Regex to Validate Email Address
def regex_validation():
    import re
    email = input("Enter email: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        print("Valid email")
    else:
        print("Invalid email")

# 38. Extract All Phone Numbers from Text Using Regex
def regex_extract_number():
    import re

    text = "Contact us at 123-456-7890 or 987-654-3210."
    pattern = r'\d{3}-\d{3}-\d{4}'

    phones = re.findall(pattern, text)
    print("Phone Numbers found:", phones)

# ************************************************************************
# Working with JSON & APIs

# 39. Read Data from JSON File
def read_json_data():
    import json
    # Assume sample.json contains: {"name": "Alice", "age": 25}
    with open('sample.json', 'r') as file:
        data = json.load(file)
    print(data)

# 40. HTTP GET Request to Public API (using requests)
def req_public_apis():
    import requests
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        data = response.json()
        print(data[:2])
    else:
        print("Invalid to fetch data")

# ************************************************************************
# Data Analysis Basics

# 41. Read a CSV file using pandas and display the first 5 rows.
def read_csv_file():
    import pandas as pd

    df = pd.read_csv('sample.csv')
    print(df.head()) # display first 5 rows

# 42. Calculate mean, median, standard deviation, & filter rows of a column in a DataFrame.
def calc_mean_median_std_df():
    import pandas as pd

    data = { 'age': [23, 26, 29, 50, 32,18]}
    df = pd.DataFrame(data)
    mean_age = df['age'].mean()
    median_age = df['age'].median()
    std_dev_age = df['age'].std()
    filter_age = df[df['age'] > 30]
    print(f"Mean: {mean_age}, median: {median_age}, std: {std_dev_age}, filter: {filter_age}")

# ************************************************************************
# Bonus ML-Related Python Practice

# 44. Write a program to implement Linear Regression from scratch (without scikit-learn).
def linear_regression():
    import numpy as np
    # Sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])
    # Calculate coefficients
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    m = numerator / denominator
    c = y_mean - m * x_mean
    print(f"Linear Regression Model: Y = {m:.2f}X + {c:.2f}")

# 45. Implement simple gradient descent to minimize a quadratic function.
def quadratic_equation():
    # Minimize f(x) = (x - 3)^2
    x = 0  # Initial guess
    learning_rate = 0.1
    iterations = 100

    for _ in range(iterations):
        gradient = 2 * (x - 3)
        x = x - learning_rate * gradient

    print(f"Minimum at x = {x:.2f}")

# 46. Write a NumPy program to perform matrix multiplication.
def matrix_multiply():
    import numpy as np

    a = np.array([[1, 2],[3, 4]])
    b = np.array([[5, 6],[7, 8]])
    result = np.matmul(a, b)
    print("Matrix Multiplication Result:\n", result)
