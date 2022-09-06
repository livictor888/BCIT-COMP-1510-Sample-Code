"""
What do we need to do, if anything, to ensure the
average that we calculate is a floating point
number and not an integer?

If we don't have to do anything, what is happening?
"""

# The high score variable holds the value that is
# considered a high score.
high_score = 95
 
# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')

