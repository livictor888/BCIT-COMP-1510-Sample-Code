"""
Demonstrates how to use the if-elif-else control structure.
"""

score = int(input("Enter percent in course: "))

if (score >= 90) and (score <= 100):
    grade = 'A'
elif (score >= 80) and (score <= 89):
    grade = 'B'
elif (score >= 70) and (score <= 79):
    grade = 'C'
elif (score >= 60) and (score <= 69):
    grade = 'D'
elif (score >= 0) and (score <= 59):
    grade = 'F'
else:
    print("\n*** invalid percentage\n")

print("The letter grade is:", grade)
