
"""
# Concatenate the following tuples into a single one,
# but replacing the odd values with zeros (`0`).

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17

# You can assume that every tuple is a sequence of consecutive integers starting with an odd integer.
# Try to write your code to be as generic as possible.
"""

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17
l = list(t1)
l.extend(t2)
l.extend(t3)
zero = [0]
l[::2] = zero * 9
t = tuple(l)
print(t)