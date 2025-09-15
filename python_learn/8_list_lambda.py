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

