import re

at_regex = re.compile(r'.*at')
match_object = at_regex.findall('The fat cat and rat in the hat sat on the flat mat with pat the bat to chat')
print(match_object)
