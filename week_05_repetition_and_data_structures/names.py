"""
Let's make some names!
"""

import random


def generate_name(syllables: int) -> str:
    """Generate a name with the specified number of syllables.

    PARAM: syllables a positive
    PRE: syllables is a positive integer
    RETURN: a string that contains the specified number of syllables.
    """
    name = ""
    for syllables in range(syllables):
        name += generate_syllable()
    return name.title()


def generate_syllable() -> str:
    """Generate and return a syllable.

    RETURN: a syllable composed of a consonant followed by a vowel"""
    return generate_consonant() + generate_vowel()


def generate_consonant() -> str:
    """Return a randomly selected consonant. Yes, y is a consonant.

    RETURN: a string containing a lowercase consonant"""
    consonants = "bcdfghjklmnpqrstvwxyz"
    return random.choice(consonants)


def generate_vowel() -> str:
    """Return a randomly selected vowel. Yes, y is a vowel.

    RETURN: a string containing a lowercase vowel"""
    vowels = "aeiouy"
    return random.choice(vowels)


def create_names_dictionary() -> dict:
    """Create and return an empty dictionary whose keys are the
    capital letters and whose values are empty lists."""
    letters = [chr(letter) for letter in range(65, 91)]
    return {letter: [] for letter in letters}


def populate_dictionary(dictionary_to_fill: dict) -> None:
    """Populate the specified dictionary with some names.

    PARAM: dictionary_to_fill whose keys are capital letters and whose
           values are possibly empty lists of strings in title case.
    POST: some names may have been added to the dictionary_to_fill"""
    quantity = int(input("How many names would you like to create: "))
    syllables = int(input("How many syllables: "))
    for count in range(quantity):
        name = generate_name(syllables)
        key = name[0].title()
        name_list = dictionary_to_fill[key]
        name_list.append(name)


def main():
    my_names = create_names_dictionary()
    populate_dictionary(my_names)
    print(my_names)


if __name__ == "__main__":
    main()
