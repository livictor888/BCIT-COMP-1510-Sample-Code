"""
What if we wat to use the iter and next functions directly?

Nothing says we can't. We may have some compelling reason to do this, though I cannot
think of any at this moment, I prefer to use abstraction.

But knowing how this works is good for a developer. We should know how a language is implemented
in order to take advantage of its quirks, strengths, and syntactic sugar.

What happens if we invoke print(next(myit)) a fourth time?
"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# What happens if we uncomment the next line?
# print(next(myit))

print(type(myit))
print(type(range(0, 1)))
