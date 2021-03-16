"""
A simple "stopwatch". This stopwatch uses an exception. The
keyboard interrupt is an exceptional situation. If the program
detects a keyboard interrupt, an exception object is created.

Ordinarily an exception object must be dealt with, else the
program will crash. That's what we have done here. All we did
was allow the program to exit gracefully. Sometimes that's all
we need to do.
"""

import time


# Display the program's instructions.
input('Press enter to begin. '
      'Afterwards, press ENTER to "click" the stopwatch. '
      'Press Ctrl-C to quit.')
print('Started.')

# get the first lap's start time
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input('Press ENTER to "click" the stopwatch')
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        # reset the last lap time
        lastTime = time.time()
except KeyboardInterrupt:
    print('Done.')
