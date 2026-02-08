# iterating dictionaries
# look at the pdfs first! then look at the 'coding' section

# (1) default
d = {
    'key 1': 1,
    'key 2': 2,
    3.14: 'pi'
}
for k in d:
    print(k)

for k in d:
    print(f'd[{k}] = {d[k]}')


# (2) values()
print()
for v in d.values():
    print(v)


# (3) items()
print()
for t in d.items():
    key, value = t
    print(f'{key}: {value}')
# or
print()
for key, value in d.items():
    print(f'{key}: {value}')


# (4) iteration order
# when you create a dictionary using a literal, the insertion order is basically the order in which
# you have listed the key value pairs

# if you add new key to the dictionary, new key will be added in the end of the dict
print()
d['x'] = 100
print(d)
for k in d:
    print(k)

# updating the doesn't change the iteration order

# deleting key and add again will change the iteration order
print()
print(d)
del d['key 1']
print(d)
d['key 1'] = 100
print(d)
for k in d:
    print(k)

