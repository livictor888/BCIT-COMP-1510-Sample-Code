def menu():
    while True:
        # does stuff
        do_something()


def do_something():
    user_input = input("Ask for data")  # Or calculate some value that can vary
    if user_input:  # Or if the value meets some test
        do_something_else()
    else:
        return


def do_something_else():
    user_input = input("Ask for data")
    if user_input:
        return
    else:
        # do whatever has to be done
        return


def main():
    menu()


if __name__ == "__main__":
    main()
