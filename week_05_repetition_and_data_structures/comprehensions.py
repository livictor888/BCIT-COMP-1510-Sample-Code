"""
Experiment with comprehensions."""


def main():
    counts = []
    for value in range(26):
        counts.append(0)
    letters = [chr(letter) for letter in range(65, 92)]
    tally = dict(zip(letters, counts))
    print(tally)
    tally_2 = {letter: count for letter in letters for count in counts}
    print(tally_2)


if __name__ == "__main__":
    main()
