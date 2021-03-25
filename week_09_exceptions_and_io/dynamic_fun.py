"""
Demonstrate recursion efficiency and dynamic programming.
"""

import time


def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def fibonacci(nth_term, result_dictionary):
    if nth_term == 0:
        result_dictionary[nth_term] = 0
        return 0
    elif nth_term == 1:
        result_dictionary[nth_term] = 1
        return 1
    try:
        return result_dictionary[nth_term]
    except KeyError:
        result = fibonacci(nth_term - 1, result_dictionary) + \
                 fibonacci(nth_term - 2, result_dictionary)
        result_dictionary[nth_term] = result
        return result


@timer
def fibonacci_manager(nth_term, result_dictionary):
    return fibonacci(nth_term, result_dictionary)


def main():

    dynamic_memory = {}
    print(fibonacci_manager(0, dynamic_memory))
    print(fibonacci_manager(1, dynamic_memory))
    print(fibonacci_manager(10, dynamic_memory))
    print(fibonacci_manager(100, dynamic_memory))


if __name__ == "__main__":
    main()
