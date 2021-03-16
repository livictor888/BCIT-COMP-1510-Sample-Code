from enum import Enum, auto


class UserStatus(Enum):
    """
    An enumeration is a special kind of thing that can only have
    specific values.

    In this case, we are defining the class User_Status to be an enumeration
    that contains four possible states.

    Putting Enum inside parentheses in the class declaration means that
    UserStatus is a kind of Enum. A subtype. A subclass. A child class.
    A specialized version. A customized version. Etc., etc., ...
    """
    PENDING = auto()
    INACTIVE = auto()
    ACTIVE = auto()
    DELETED = auto()


def main():
    current_user_status = UserStatus.ACTIVE

    if current_user_status == UserStatus.ACTIVE:
        current_user_status = UserStatus.INACTIVE


if __name__ == "__main__":
    main()
