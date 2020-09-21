def greet(mode, message):
    greeting = mode(message)
    print(greeting)


def main():
    yell = str.upper
    whisper = str.lower
    confused_rasp = str.swapcase

    user_input = input("What is your announcement: ")
    greet(yell, user_input)


if __name__ == "__main__":
    main()

