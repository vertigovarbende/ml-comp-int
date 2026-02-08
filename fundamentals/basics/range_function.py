# range object and 'range()' function
# look at the pdfs first! then look at the 'coding' section

# (1) 'range()' function will create range object
# range objects are objects which are basically things that contains 'integers'
# it is an iterable of integers

print(range(10))
print(type(range(10)))


# (2) we can iterate over the numbers in that range object and make a 'list' or 'tuple' out of that
# by using 'list' and 'tuple' functions

l = list(range(10))
print(l, type(l))
t = tuple(range(10))
print(t, type(t))


# (3) 'range()' function can take one, two or three arguments to create range objects

# (3.1) we can specify one argument for the range function
# first argument will be '0' (inclusive)
# the argument specifies the last argument of the range object (exclusive)
l = list(range(10))
print(l, type(l))

# (3.2) we can specify two arguments for the range function
# first argument specifies the first argument (inclusive)
# last argument specifies the last arguments of the range object (exclusive)

l = list(range(2, 8))
print(l, type(l)) # [2, 8) int

# (3.3) we can also specify three arguments for the range function
# if we don't specify the number of the step, it will be 1 by default

l = list(range(2, 8, 2))
print(l, type(l)) # 2, 4, 6

# Be careful with the arguments because as you can see one of them is inclusive and the other one is
# exclusive


# (4) 'len' function
# we can also look at the length of range objects
print(len(range(10)))
print(len(range(3, 9)))