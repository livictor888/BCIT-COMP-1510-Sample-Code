import re


def main():
    while True:
        guffaw_regex = re.compile(r'(Ha){3,5}?')
        # guffaw_regex = re.compile(r'(Ha){3,5}')
        user_input = input("How funny is the joke?: ")

        match_object = guffaw_regex.search(user_input)
        if match_object:
            print("This funny:", match_object.group())
        else:
            print("Not funny.")


if __name__ == "__main__":
    main()
