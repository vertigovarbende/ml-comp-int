# slicing sequences
# look at the pdfs first! then look at the 'coding' section

# (1) We can slicing sequences
# [start:stop:step]
# start -> inclusive - default '0'
# stop -> exclusive - default 'last index'
# step -> default '1'
s = "Python rocks!"
print(s[0:6])

# (2) In general, slices are of the same type as the type being sliced
t = 1, 2, 3, 4, 5
print(t[1: 4], type(t[1: 4]))
l = list(t)
print(l[1: 4], type(l[1: 4]))
# What's important to realize is that a 'new object' is created that contains the same elements
# as the original sequence being sliced
# So the slice is a new object? YES
# BUT the elements are the same objects as the original ones
l1 = [1, 2, 3, 4, 5]
l2 = l1[0: 3]
print(l2)
print(l1 is l2) # new object
l2[0] = 100
print(l2) # first element changed
print(l1) # original one is still same

l = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
print(l)
sublist = l[0: 2]
print(sublist)
print(l is sublist)
sublist[1] = "Python"
print(sublist)
print(l)

# HOWEVER, if I look at the 'sublist[0]' and 'l[0]', I can see they are the same, they are the
# same object
print(sublist[0] is l[0])
sublist[0][0] = 100
print(sublist)
print(l)

# (3) sometimes we don't have to specify the 'start' and 'stop'
s = "Python rocks!"
print(s[7:])
print(s[0: 6], s[:6])

# we can omit both the 'start' and 'stop'
l = [1, 2, 3, 4, 5]
l2 = l[:]
print(l2)
# but they are not the same object
print(l is l2)
l2[0] = 100
print(l2)
print(l)

# (4) we also have a variant on slicing where we can specify the step value
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[1: 8])
print(l[1: 8: 2])

# we can omit the 'stop'
print(l[1: : 2])
print(l[0: : 2])

# we don't even have to specify the 'start' of the sequence
print(l[: : 2])

# (5) negative indexes
s = 'abcdef'
print(s[-4], s[-1])
# so we can slice from -4 to -1
print(s[-4: -1])
print(s[-1: -4: -1])
print(s[: -4: -1])


# we don't event have to specify the 'start' and the 'stop' of the sequence
s = "abcdef"
print(s[: : -1]) # fedcba

m = [1, 2, 30, 100]
mReversed = m[:: -1]
print(mReversed)
# or 'reversed' function ??
mReversed2 = list(reversed(m))
print(mReversed2)

# Palindrome
a = "racecar"
print(a[::-1])
print(a == a[:: -1])

a = "hello"
print(a[::-1])
print(a == a[::-1])



















