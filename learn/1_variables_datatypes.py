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
