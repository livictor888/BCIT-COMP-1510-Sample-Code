"""
When we talk about scope, we talk about LEGB: Local, Enclosing, Global, then Built-in scopes.

What does this code do?
"""

global_variable = 'global_variable'


def outer(outer_parameter='outer_parameter'):
    local_variable_in_outer = 'local_variable_in_outer'

    def inner():
        print(global_variable, outer_parameter, local_variable_in_outer)
    inner()


def main():
    outer()


if __name__ == "__main__":
    main()
