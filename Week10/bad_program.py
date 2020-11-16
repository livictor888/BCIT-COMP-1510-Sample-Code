def menu():
    # does stuff
    do_something()


def do_something():
    user_input = input("Ask for data")  # Or calculate some value that can vary
    if user_input:  # Or if the value meets some test
        do_something_else()
    else:
        do_something()  # Try again


def do_something_else():
    user_input = input("Ask for data")
    if user_input:
        do_something_else()
    else:
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()

# Represents the call stack
# menu
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# menu
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# menu
# main
