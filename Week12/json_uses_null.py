"""
Note how JSON uses null, while Python uses None.
The json library takes care of this automatically for us!
"""

import json

string_of_json_data = '{ "name": "Zofia", "isCat": true, "miceCaught": 0, "felineIQ": null}'
# json.loads converts None to null
json_data_as_python = json.loads(string_of_json_data)
print(json_data_as_python)

python_dictionary = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
# json.dumps converts None to null
string_of_json_data = json.dumps(python_dictionary)
print(string_of_json_data)
