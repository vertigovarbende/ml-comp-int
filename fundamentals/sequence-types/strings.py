# strings
# look at the pdfs first! then look at the 'coding' section

# (1)
a = 'hello'
# or
b = "Python"
a = "Python's best features:"
print(a)
# but if we had tried to do the same thing, putting in single quotes
# a = 'Python's best features:'
# we can see even the highlighting is not working properly because it sees this as the end of the
# string. So if we run this code, we will get an SyntaxError

# In this case we can use backslash '\'
a = 'Python\'s best features:'
print(a)

# (2) Strings are sequences
s = "Python rocks!"
print(s[0], s[1], s[len(s) - 1])

# (3) negative indexes
print(s[-13], s[-12], s[-1])

# (4) 'len' function
print(len(s))

# (5) Strings are immutable
# Which means that we cannot add, remove or replace elements, characters in a string
"""
# TypeError!
print(s[0])
s[0] = 'X'
print(s[0])
"""

# (6) creating empty strings
a = ""
b = ''
print(type(a), len(a), type(b), len(b))
# we can also use 'str()' function to create empty string
s = str()
print(type(s), len(s))


# (7) 'str()' function
# Just as with the 'tuple()' and the 'list()' functions that we say, the 'str()' function can
# also take in an arbitrary sequence type and basically convert that to a string, but it is going
# to create a string

t = 1, 2, 3
# That is just a string that Python prints out
# and that string how that tuple prints itself out is determined by the tuple type itself
# So this is just a string representation
print(t)

s = str(t)
print(s, type(s), len(s))
print(s[0], s[1], s[2])


# (8) 'str' function can take arbitrary arguments like int, float ...
# but it can also take a sequence type
# You would pass it a sequence and then it would then make a tuple with EACH element being the
# element that we specify in that sequence 's'
s = "Python"
t = tuple(s)
print(t, type(t))

# the same thing will work with 'lists'
l = list(s)
print(l, type(l))

l = ['a', 'b', 'c', 'd', 'e', 'f']
print(l)
# or we could just say
s = "abcdef"
l = list(s)
print(l)

# (9) Another thing that's interesting about 'strings' and also by the way 'tuples' and 'lists'
# is that they do support being multiplied by an integer
s = "===================="
print(len(s))
# instead what we can do is
s = '=' * 20
print(s, len(s))
# and this works with any sequence type
t = (1, 2, 3) * 3
print(t, type(t))
l = [2, 4, 6] * 3
print(l, type(l))

# 3x3 Square Matrix
"""
l = [[0, 0, 0] * 3]
for i in range(0, 3):
    for j in range(0, 3):
        print(l[i][j], end = " ")
    print()
"""

# IMPORTANT!
# When you do multiplication, it will reuse the same object whatever number of times we specify
t = ([1, 2], 30)
t2 = t * 3
print(t2)
print(t2[0] is t[0])
print(t2[2] is t[0])
print(t2[2] is t2[0])
print(t2[4] is t[0])

# So when we want to create a matrix
m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(m)
row_1 = m[0]
print(row_1)
row_1[0] = 1
print(row_1)
print(m)

# So if we try and create this zero matrix this way
m = [[0] * 3, [0] * 3, [0] * 3]
print(m)
# or
m = [[0, 0, 0]] * 3
print(m)
# When we check out the rows in that matrix
print(m[0] is m[1])
# What that means now is that if we try and modify the matrix you will notice
# we actually modified m[1][0] and m[2][0] because they are the same object
m[0][0] = 1
print(m)