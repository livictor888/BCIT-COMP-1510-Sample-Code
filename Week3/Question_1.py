"""
COMP 1510 202030
Lab 02
"""


def base_conversion(destination_base, original_value):
    # do something
    return 0


base_10 = 200
dest_base = 4
result = base_conversion(dest_base, base_10)
print("Called base_conversion with " + str(base_10) + str(dest_base) + " equals " + str(result))

base_10 = 200000000
dest_base = 4
result = base_conversion(dest_base, base_10)
print("This proves the function  reacts correctly to invalid arguments")
print("Called base_conversion with " + str(base_10) + str(dest_base) + " equals " + str(result))
