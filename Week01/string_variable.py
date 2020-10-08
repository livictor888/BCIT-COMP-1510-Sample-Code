"""
We can assign strings to variables, and then print the variables.

What we are actually doing is creating a string object in memory. The
string object occupies a space in memory that we can visit using the
address of the string. The address is usually a big hexadecimal number
that doesn't help us at all. We assign the address of the string object
to a variable. That variable stores the address. When we print the
variable, the Python runtime sees the address in the variable, visits
that address, sees the string there, and substitutes the string for
the variable name in the print statements.

Everything in Python has an address in memory. That address is what we
store in variables.
"""


# Create variables to reference two strings.
first_name = 'Kathryn'
last_name = 'Marino'

# Display the values referenced by the variables.
print(first_name, last_name)

