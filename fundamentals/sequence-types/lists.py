# lists
# look at the pdfs first! then look at the 'coding' section

# (1) creating a list
l = [10, 20, 30, 40, 50]
print(l)

# (2) 'type' function
print(type(l))

# (3) list are sequences and their elements are therefore positionally ordered
print(l[0], l[1], l[2], l[3], l[4])

# (4) 'len' function
print(len(l))
print(l[len(l) - 1])

# (5) negative indexes
print(l[0], l[1], l[2], l[3], l[4]) # positive
print(l[-5], l[-4], l[-3], l[-2], l[-1]) # negative
# So very often when we are looking for the last element of a list will actually use
# negative

# (6) creating empty list
lEmpty = []
print(lEmpty)
print(type(lEmpty))
# or
lEmpty2 = list()
print(lEmpty2)
print(type(lEmpty2))

# (7) replacing
print(l)
l[2] = 3.14
print(l)
l[-1] = "Hello"
print(l)
