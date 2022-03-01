import re


def match_digits():
    while True:
        digits = re.compile(r'^(\d{1,3})(,\d{3})*$')
        user_input = input("Enter digits!")
        match_object = digits.search(user_input)
        if match_object:
            print(match_object.group())
        else:
            print("Invalid!")


def main():
    match_digits()


if __name__ == '__main__':
    main()
