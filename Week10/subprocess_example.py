"""
The subprocess module lets us start other programs.

That's right. We can use our Python program to run other programs now. WOW!
"""

import subprocess
import time


# status = subprocess.run('/System/Applications/Calculator.app/Contents/MacOS/Calculator')
# status = subprocess.run(['/usr/local/bin/python3.8', 'webbrowser_example.py'])

status = subprocess.run('/System/Applications/Calculator.app/Contents/MacOS/Calculator')
print(status.poll())
# time.sleep(3)
# print(status.poll())
status = subprocess.run(['/usr/local/bin/python3.8', 'webbrowser_example.py'])
