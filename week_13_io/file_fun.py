import io


def make_file():
    with open('newfile.txt', 'w') as file_object:
        print(type(file_object))
        file_object.write("Hello")


def read_file():
    with open('newfile.txt') as file_object:
        contents = file_object.read()
        print(type(contents))
        print(contents)
        file_object.seek(io.SEEK_SET)
        more_contents = file_object.read()
        print(more_contents)


def main():
    make_file()
    read_file()


if __name__ == "__main__":
    main()
