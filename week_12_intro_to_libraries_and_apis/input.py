"""
There are some fantastic examples here:

https://docs.python.org/3.9/library/json.html
"""

import json


with open('input.json', 'r') as data:
	obj = json.load(data)
	with open('output.txt', 'w') as output:
		output.write(obj['name'] + "'s Hobbies:\n")
		for hobby in obj['hobbies']:
			output.write(hobby + "\n")
