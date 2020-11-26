import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for and store a new username."""
    username = {"name": input("What is your name? ")}
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username['name'] + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username['name'] + "!")


def main():
    greet_user()


if __name__ == "__main__":
    main()
