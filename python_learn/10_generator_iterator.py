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

