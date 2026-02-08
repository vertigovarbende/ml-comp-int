# associative arrays and dictionaries
# look at the pdfs first! then look at the 'coding' section

# (1) creating a dictionary and accessing the values
# we can create dictionaries in one line
d = {'a': 1, 'b': 2, 'c': 3}
# and also we can create dictionaries in more line
# readability matter!
person = {
    'first_name': 'Eric',
    'last_name': 'Idle',
    'year_born': 2016
}
print(person['year_born'])


# (2) replacing/updating
person['year_born'] = 1943
print(person)


# (3) creating new key:value pairs
person['month_born'] = 'March'
print(person)


# (4) keys must be hashable and unique
d = {3.14: 'pi', 2: 'even', 'prime': 7}
print(d[3.14])
print(d[2])
# we cannot use the lists as a 'key' because they are not hashable
# mutable objects are not hashable in general!
l = [1, 2, 3]
# TypeError!
# d = {l: 100}
# print(d)

# hash function
print(hash(100))
print(hash(3.14))

# tuples are an immutable collection, but they may or may not be hashable depending on whether
# all the contained elements are hashable or not
t = 1, 2, 3, 4
print(hash(t))
t = [1, 2], 3, 4
# TypeError!
# print(t, hash(t))
# so we can use tuples as keys sometimes
d = {
    (0, 0): 'origin',
    (1, 0): 'unit-x',
    (0, 1): 'unit-y'
}
print(d)
print(d[(0, 0)])


# (5) we can delete a key and its associated value
# 'del' keyword
d = {'a': 1, 'b': 2, 'c': 3}
print(id(d))
del d['a']
print(d)


# (6) exceptions

# (6.1) reading a non-existing key -> 'KeyError'
# print(d['x'])

# (6.2) deleting a non-existing key -> 'KeyError'
# del d['x']


# (7) globals()
print(globals())
print(type(globals()))
p = globals()['person']
print(p)
print(p is person)
