def add(a: int = 5, b: int = 4) -> int:
    return a + b


def main():
    result = add(1, 2)
    print(result)
    result = add(1.0, 2.0)  # Does this work?
    print(result)
    result = add("Hello", "World")  # Does this work?
    print(result)
    result = add(5)  # What about this?
    print(result)


if __name__ == "__main__":
    main()
