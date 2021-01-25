"""
Python is fabulous but Python is slow. Very slow. Python is not
fast by any measurements. If you ever need to measure how long
something takes, here's a fun way to do it! File this away, we
will use it...
"""

import time

t1 = time.perf_counter()

# Code to time goes here

t2 = time.perf_counter()

print('The code took {:.2f}ms'.format((t2 - t1) * 1000.))
