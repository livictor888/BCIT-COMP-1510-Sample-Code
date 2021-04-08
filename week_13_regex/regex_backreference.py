import re


def main():
    while True:
        four_of_a_kind = re.compile(r'(.)\1{3}')
        user_input = input("Enter your text: ")
        match_object = four_of_a_kind.search(user_input)
        if match_object:
            print('You entered:', match_object.group())
        else:
            print("No acceptable.")


if __name__ == "__main__":
    main()
