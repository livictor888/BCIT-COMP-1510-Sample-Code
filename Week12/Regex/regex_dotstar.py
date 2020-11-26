import re


def main():
    # name_regex = re.compile(r'First Name: (.+) Last Name: (.+)')
    # user_input = 'First Name: a-2 Last Name: '
    #
    # match_object = name_regex.search(user_input)
    # if match_object:
    #     print("You entered:", match_object.group())
    # else:
    #     print("Wrong input")

    non_greedy_regex = re.compile(r'<.*?>')
    match_object = non_greedy_regex.search('<Inner > Outer>')
    print(match_object.group())

    greedy_regex = re.compile(r'<.*>')
    match_object = greedy_regex.search('<Inner > Outer>')
    print(match_object.group())


if __name__ == "__main__":
    main()
