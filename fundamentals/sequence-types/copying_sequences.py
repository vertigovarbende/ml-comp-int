# copying sequences
# look at the pdfs first! then look at the 'coding' section

# (1) shallow copy
# shallow copying will create new sequences
# but elements in new sequence reference the same elements as original

# (1.1) shallow copy by using slicing
l1 = [1, 2, 3]
l2 = l1[:]
print(l2)
print(l1 is l2)
# when we append new element
l2.append(10)
print(l1, l2) # they are not same because they are separate lists

# (1.2) 'copy' function
# we can also make a shallow copy by using the 'copy' method of lists
l3 = l1.copy()
print(l3 is l1) # False because they are separate lists
l3.append(10)
print(l1, l3)

# but what you have to be a little bit more careful is when the items in the list in the sequence
# is a mutable items is a mutable object
m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(m1)
m2 = m1.copy() # shallow copy
print(m2)
print(m1 is m2)
m2.append([10, 20, 30])
print(m2)
# but m1 will same
print(m1)
# the problem is that this list -> 'm1[0]' and this list -> 'm2[0]' are the same object!
# they both (m1, m2) references to the same object, same thing with these two -> 'm1[1]', 'm2[1]'
# it makes a new list, but it uses the same references that the original list is pointing to
print(m1[0])
print(m2[0])
print(m1[0] is m2[0])
m2[0].append(-1)
print(m2)
print(m1)

# (2) deep copy
# we may copy elements as well, so in that case, we need to make what's called a 'deep copy'
# and for that we can actually use the 'deep copy' function that Python provides in the standard
# library

from copy import deepcopy
m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m2 = deepcopy(m1)
print(m1)
print(m2)
print(m1 is m2) # False because these two are still separate lists

# but the difference from 'shallow copy' is if I look at 'm1[0]' and 'm2[0]'
# they are no longer the same object
print(m1[0])
print(m2[0])
print(m1[0] is m2[0])

# so this means that as before we could be modifying 'm1' or 'm2' by appending elements
# it won't matter just the same way with the 'shallow copy'
# But in addition, now if we try and let's say append something to 'm2[0]'
m2[0].append(10)
print(m1)
print(m2)




















