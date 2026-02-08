# python sets
# look at the pdfs first! then look at the 'coding' section

# (1) creating a python set

s = {'a', 'b', 'c'}
print(type(s))
# we can also use 'set()' function
s = set(['a', 'b', 'c'])
print(s)
s = set('abc')
print(s)
s = set('python')
# The orer in sets in not guaranteed.
print(s) # the order here is not the order in which we specify the elements.


# (2) sets also like dictionary keys have unique elements

print()
s = set(['a', 'a', 'b', 'b'])
print(s)
s = set('banana')
print(s)


# (3) creating a empty python set

# don't use curly brackets to define a empty python set
# if you use it, you will define a dict not a set
s = {}
print(s, len(s), type(s))
# to define a empty set, you have to use 'set()' function
s = set()
print(s, len(s), type(s))


# (4) in terms of membership testing, iteration, clearing and copying sets,
# it works the same way as with dictionaries, so
# we have 'deep copy'
# we have 'shallow copy'
# we have 'clear()' method
# we can iterate over the elements of a set

# (4.1) membership
s = set('python')
print(s)
print('p' in s) # True
print('x' not in s) # True

# (4.2) iterating with for loop
for item in s:
    print(item, end=',') # order is not guaranteed
print()
# (4.3) copying
# shallow copy
s2 = s.copy()
print(s2)
# deep copy
from copy import deepcopy
s2 = deepcopy(s)
print(s2)