def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


def decorate_and_return(func):
    def wrapper_returns(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return func(*args, **kwargs) # What is happening here?
    return wrapper_returns


@do_twice
def say_cake():
    print("Cake! Gâteau! 케이크!, 蛋糕! bánh ngọt! Торт! केक!")


# @my_decorator
# def say_cake():
#     print("Cake! Gâteau! 케이크!, 蛋糕! bánh ngọt! Торт! केक!")


@decorate_and_return
def return_greeting(name):
    return f"Hi {name}"


@do_twice
def greet_with_cake(name):
    print(f"Cake for {name}!")


def main():
    say_cake()
    greet_with_cake("everyone")
    hi_justin = return_greeting("Justin")
    print(hi_justin)


if __name__ == "__main__":
    main()

