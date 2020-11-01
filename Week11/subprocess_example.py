"""
The subprocess module lets us start other programs.

That's right. We can use our Python program to run other programs now. WOW!
"""

import subprocess
import time


status = subprocess.run(['/usr/local/bin/python3', 'webbrowser_example.py'])
time.sleep(3)
status = subprocess.run('/System/Applications/Calculator.app/Contents/MacOS/Calculator')
