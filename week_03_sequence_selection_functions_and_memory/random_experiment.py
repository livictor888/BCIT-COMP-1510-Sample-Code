import random


def main():
    my_random = random.randint(0, 10)
    print(my_random)

    population = "water"

    chosen_letters = random.choices(population, k=26)
    print(chosen_letters)
    string_letters = "".join(chosen_letters)
    print(string_letters)

    will_this_work = random.sample(population, 5)
    print(will_this_work)


if __name__ == "__main__":
    main()
