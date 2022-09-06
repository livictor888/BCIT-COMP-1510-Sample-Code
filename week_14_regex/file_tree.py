import os
import os.path as path
import re


def find_files(pattern, base='.'):
    """Find files based on pattern.

    Walks the filesystem starting at base and returns a list
    pf filenames that match the given pattern.
    """

    regex = re.compile(pattern)
    matches = []
    for root, dirs, files in os.walk(base):
        for file in files:
            if regex.match(file):
                matches.append(path.join(root, file))
    return matches
