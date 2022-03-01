import io


def make_file():
    with open('newfile.txt', 'w') as file_object:
        print(type(file_object))  # Just for fun
        file_object.write("If you can't handle me at my worst, ")
        file_object.write("you probably have healthy boundaries -- Anonymous")


def read_file():
    with open('newfile.txt') as file_object:
        contents = file_object.read()
        print(contents)
        file_object.seek(io.SEEK_SET)  # return to beginning
        file_object.seek(54)  # move forward 54 characters
        awesome = file_object.read(18)  # read 18 characters
        print(awesome)
        remember = file_object.tell()  # memorize location
        print(remember)
        file_object.seek(io.SEEK_SET)  # return to beginning
        contents = file_object.read()
        print(contents)
        file_object.seek(remember + 4)
        author = file_object.read()
        print(author)


def main():
    make_file()
    read_file()


if __name__ == "__main__":
    main()
