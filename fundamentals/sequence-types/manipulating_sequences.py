# manipulating sequences
# look at the pdfs first! then look at the 'coding' section

# (0) modifying sequences

# (1) assigning/replacing by using index and assigning/replacing by using slicing
l = [10, 20, 3, 40, 50]
l[2] = 30
print(l)

# we can also replace an entire slice inside a sequence
l = [1, 20, 30, 5, 6]
# length is not the same as the length of the slice and that's ok!
l[1: 3] = [2, 3, 4]
print(l)
# or
l = [1, 20, 30, 5, 6]
l[1: 3] = 2, 3, 4 # or (2, 3)
print(l)
# or
"""
l = [1, 20, 30, 5, 6]
l[1: 3] = "234" # but it will be a character CAREFUL!!
print(l)
"""
# CAREFUL!!
print(l[1: 3])
l[1: 3] = "Python"
print(l)

# (1.2) we can use a step in the slice definition
# but there is something though
# Number of items in the slice and the number of items that we specify in the sequence on the right
# hand side of the assignment must match

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l[1: : 2])
l[1: : 2] = 20, 40, 60, 80 # or (20, 40, 60, 80)
print(l)
# if we don't have a match, we will get an exception!
"""
l = [1, 2, 3, 4, 5, 6, 7, 8]
l[1: : 2] = 20, 40, 60 # less
print(l)
l[1: : 2] = 20, 40, 60, 80, 100 # much
"""

# (1.3) the assignment to a slice works with negative steps as well
# It doesn't use often!
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l[:-3:-1])

# the lengths must match!
# and also '100' is going to go into '8' and '200' is going to go into '7'
l[:-3:-1] = 100, 200
print(l)

# (2) we can delete an element
l = [1, 2, 3, 4, 5, 6, 7, 8]
del l[2]
print(l)
# we can also delete an entire slice
l = [1, 2, 3, 4, 5, 6, 7, 8]
del l[2: 5]
print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8]
del l[1::2]
print(l)


# (3) add elements to a list

# (3.1) append
l = [1, 2, 3, 4]
l.append(5)
print(l)

# CAREFUL!
# here the 'append' expects a single argument, not a sequence
# so it is going to treat "Python" as a single element, as a single sequence
l.append("Python")
print(l)
# same thing will happen for a tuple as well
l.append((1, 2, 3))
print(l)

# (3.2) extend
# it's basically adding multiple elements to the end of the list, but it's adding it based
# on an iterable, based on a sequence that we could provide to the method
# and there it's going to take 'EVERY ELEMENT' of that sequence and insert them as individual
# elements into that list or append them to be more specific to that list, inserting them at the
# end of the list.
l = [1, 2, 3, 4]
l.extend([5, 6, 7, 8]) # it's going to take every element of this sequence and add them to the list
print(l)
# we can also extend it by passing a 'tuple'
l = [1, 2, 3, 4]
l.extend((5, 6, 7, 8))
print(l)

l = [1, 2, 3, 4]
l.extend("Python")
print(l)


# (4) insert
# we can also insert elements in the middle of the list, but it is not as efficient!
l = [1, 2, 3, 4]
print(l[2])
# the second argument is not going to be treated as a sequence of individual items
# its going to be treated as a single object that's going to get inserted at index two
l.insert(2, 'a')
print(l)
l = [1, 2, 3, 4]
l.insert(3, [3.25, 3.5, 3.75])
print(l)

# (5) inserting an element into a list is quite slower than appending
from timeit import timeit
l = []
# 'timeit' function is going to execute this piece of code here
# when this code is getting executed, it needs to know that 'l' is
# this is how we can pass to this 'timeit' function -> globals = globals()
# and 'number' is the number of times that it's going to repeat this operation
# we do that because timing something just once is not very accurate
# we want to time it multiple times and then see overall, how long does it take for that
print(timeit('l.append(1)', globals=globals(), number = 100_000))
print(len(l)) # 100_000

l = []
print(timeit('l.insert(0, 1)', globals=globals(), number = 100_000))











