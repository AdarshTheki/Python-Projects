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

