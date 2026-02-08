# common set operations
# look at the pdfs first! then look at the 'coding' section


# (1) isdisjoint() method -> ayrik

s1 = set('abc')
s2 = {True, False}
s3 = {'a', 100, 200}

print(s1.isdisjoint(s2)) # True
print(s2.isdisjoint(s1)) # True

print(s1.isdisjoint(s3)) # False
print(s3.isdisjoint(s1)) # False


# (2) add() method
print()

s = set()
s.add(100)
print(s)
s.add(200)
print(s)
s.add(200)
print(s)


# (3) remove() method and discard method
print()
# if we try and 'remove' sth that is not in the set
s = set('abc')
s.remove('a')
print(s)
# s.remove('d') # KeyError!

# if we try and 'discard' sth that is not in the set
print(s)
s.discard('b')
print(s)
s.discard('d') # nothing will happen!


# (4) subset, strict subset, superset, strict superset
print()

s1 = set('abc')
s2 = set('abcd')
print(s1 < s2) # True - strict subset
print(s1 <= s2) # True - subset
print(s2 >= s1) # True - superset
print(s2 > s1) # True - strict superset

print()
s3 = set('abc')

print(s1 < s3) # False - strict subset
print(s1 <= s3) # True - subset
print(s3 >= s1) # True - superset
print(s3 > s1) # False - strict superset


# (5) union, intersection
print()

s1 = set('abc')
s2 = set('bcd')

# union
print(s1 | s2) # abcd
# intersection
print(s1 & s2) # bc


# (6) difference
print()

print(s1 - s2, type(s1 - s2)) # a
print(s2 - s1, type(s2 - s1)) # d


# (7) example 1
# Suppose we have two strings and we want to find all the characters that are present
# in both strings

str_1 = 'python is an awesome language!'
str_2 = '/a python is also a snake.'

set_1 = set(str_1)
set_2 = set(str_2)

print(set_1)
print(set_2)
print(set_1 & set_2)


# (8) example 2
# we have two or more sets that contain some stock symbols.
# let's say that we have different servers that are tracking different stock symbols,
# and we want to compile a list of all the stock symbols that all the servers are tracking.
print()
s1 = {'FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG', 'MSFT'}
s2 = {'BABA', 'WMT', 'COST'}
s3 = {'TSLA', 'F', 'GM'}

consolidated = s1 | s2 | s3
print(consolidated)
consolidated = list(s1 | s2 | s3)
print(consolidated)


# (9) subtract one set from another
print()

sold = {'w1', 'w2', 'w3', 'w4'}
returned = {'w1'}

non_returned = sold - returned
print(non_returned)

alphabet = set('abcdefghijklmnopqrstuvwxyz')
# 'string' library has same thing in Python
import string
# lowercase
print(string.ascii_lowercase)
# uppercase
print(string.ascii_uppercase)
# ascii letters
print(string.ascii_letters)

# So we can do this
alphabet = set(string.ascii_letters)
print(alphabet)

text = "The quick brown fox jumps over the lazy dog"
print(set(string.ascii_letters) - set(text))
# this means is that 'text' string actually contains all the characters from A to Z.
print(set(string.ascii_letters.casefold()) - set(text))

text = 'aBcDeFgHiJkKlLmMnNoOpPqQrRsStTuUvVwW'
print(set(string.ascii_letters.casefold()) - set(text.casefold()))




