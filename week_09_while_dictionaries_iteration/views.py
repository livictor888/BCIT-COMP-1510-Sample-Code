"""
Views are not lists!
"""

def main():
    meals = {'bfast': 'egg', 'lunch': 'poke', 'dinner': 'spinach'}
    keys = meals.keys()
    values = meals.values()
    entries = meals.items()
    print(type(keys))
    print(type(values))
    print(type(entries))


if __name__ == '__main__':
    main()
