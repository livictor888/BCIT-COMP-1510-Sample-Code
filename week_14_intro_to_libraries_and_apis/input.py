"""
There are some fantastic examples here:

https://docs.python.org/3.10/library/json.html
"""

import json


with open('input.json', 'r') as data:
	data_object = json.load(data)
	print(type(data_object))
	with open('output.txt', 'w') as output:
		output.write(data_object['name'] + "'s Hobbies:\n")
		for hobby in data_object['hobbies']:
			output.write(hobby + "\n")
