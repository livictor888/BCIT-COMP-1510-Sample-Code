"""
What does this show us?

Watch me use the debugger to set a breakpoint so we can see what gets created.
"""

nums = list(range(-10, 300))
for i in nums:
    print(i, id(i), id(i+1)-id(i))
