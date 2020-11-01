"""
Profiling is what we call timing a piece of code.

We profile it to determine how long it takes to execute.

There is a very quick and easy way to do this. The time
module contains a time function. It returns the current
time, in seconds since the beginning of the Epoch. We
can use this knowledge and some simple math to determine
how long some code takes to execute.

Note: Python is not fast. It's not a fast language. When
we want fast software, we can use something else. Python
is easy to use and develop and grow and it RULES the
artificial intelligence big data machine learning world
(for now, anyway!)
"""

import time


startTime = time.time()
print(startTime)

for i in range(1, 100000):
    product = product * i

endTime = time.time()
print(endTime)

print('Took %f seconds to calculate.' % (endTime - startTime))

# Consider how long it takes to perform this command!
print('The result is %s digits long.' % (len(str(product))))



