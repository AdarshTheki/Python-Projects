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

