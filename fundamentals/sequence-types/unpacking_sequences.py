# unpacking sequences
# look at the pdfs first! then look at the 'coding' section

# (1) unpacking
rate = 5.0, 5.12
# sometimes we can assign them to separate symbols
apr = rate[0]
apy = rate[1]
# a much simpler way to do this is use something called unpacking
apr, apy = rate
print(apr)
print(apy)
# this works for a sequence of any size
# the only requirement is that we provide as many symbols on the left as there are elements
# in the sequence on the right
a, b, c = 10, 3.14, 'abc'
print(a, b, c)
# if the number of items don't match on either side, we will get 'value' exceptions
# a, b, c = 10, 20 ValueError!
# if we provide too many items, it will tell us this too many value to unpack
# a, b = 10, 20, 30

# (2) unpacking works with iterables in general
# tuples, lists and strings

x, y, z = 'abc'
print(x, y, z)

# (3) when we want to unpack sth, first right side will create
s = 'abcdef'
a, b, c = (1 + 1, s[::-1], 3.14)
print(a, b, c)

# (4) we can use 'unpacking' for swap variables
a = 100
b = 3.14
a, b = b, a
print(a, b)
