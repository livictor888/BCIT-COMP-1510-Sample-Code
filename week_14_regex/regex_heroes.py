import re


def main():
    while True:
        heroes_regex = re.compile(r'Batman|Tina Fey')
        user_input = input("Enter your hero(es): ")
        match_object = heroes_regex.search(user_input)
        if match_object:
            print('The hero you entered is:', match_object.group()) # the first!
        else:
            print("Not acceptable.")


if __name__ == "__main__":
    main()
