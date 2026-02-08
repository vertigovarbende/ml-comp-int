# tuples
# look at the pdfs first! then look at the 'coding' section

# (1) creating a tuple
t = (1, 2, 3)
print(t, type(t))
# or
# We don't actually need to use the round parentheses all the time to define tuple
# But in some circumstances we will have to because we will need to be able to
# specifically delineate where the tuple starts and ends
t = 1, 2, 3
print(t, type(t))


# (2) tuple is a sequence type
print(t[0], t[1], t[2])


# (3) negative indexes
print(t[-3], t[-2], t[-1])


# (4) 'len' function
print(len(t))
print(t[len(t) - 1], t[-1])
print(t[-len(t)])


# (5) tuples are immutable
# We cannot add references, remove references or replace a reference
"""
# TypeError!
t[2] = 40
print(t)
"""
# But it doesn't mean that the elements inside the tuple are immutable!
t = [1, 2], [3, 4]
print(t, type(t))
print(t[0], type(t[0]))
"""
# TypeError!
t[0] = 100
print(t[0])
"""
# However
l = t[0]
print(l)
l[0] = 100
print(l)
print(t)
# So the tuple as a collection is immutable, but the elements inside the tuple may be mutable!
t[0][1] = 200
print(t)


# (6) creating empty tuples
t = ()
print(t, type(t), len(t))
# or we can use 'tuple()' function to create a empty tuple
t = tuple()
print(t, type(t), len(t))
# But since we can't mutate the tuple, this isn't very useful!


# (7) 'tuple' and 'list' functions
# We can pass in any sequence and it will take each element of that sequence and create a unique
# tuple containing the same elements
l = [1, 2, 3]
t = tuple(l)
print(t, type(t))
# We can use the 'list' function in the same way
t = 3, 4, 5
l = list(t)
print(l, type(l))

# For example
t = 10, 20, 3, 40
l = list(t)
l[2] = 30
print(l, type(l))
t = tuple(l)
print(t, type(t))


# (8)
t = [1, 2], 30, 40
print(t, type(t))
t[0][1] = 20
print(t, type(t))
l = list(t)
print(l, type(l))

# What we have to recognize and realize is that this [1, 2] object here, which is inside the 'l'
# list and the list [1, 2] object which is inside the tuple, are actually the same object!
# It is a common shared reference to the same object!

print(l[0])
l[0][0] = 10
print(l)
# Let's take a look at the original tuple
print(t)
# We can see that now also reflects the same change because these two '[1, 2]' are the same objects
# and we mutated
# We will see details in 'copying sequences' section























