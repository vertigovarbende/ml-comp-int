# list comprehensions
# look at the pdfs first! then look at the 'coding' section

# (1)

# we are going to calculate the magnitudes of those vectors
vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]
from math import sqrt

# (1.1) standard approach
# my solution
print('standard approach')
magnitudes = []
result = 0
for vector in vectors:
    for item in vector:
        result += item ** 2
    magnitudes.append(sqrt(result))
    result = 0
print(magnitudes)

# real solution
magnitudes = []
for vector in vectors:
    magnitude = sqrt(vector[0] ** 2 + vector[1] ** 2)
    magnitudes.append(magnitude)
print(magnitudes)
# or
magnitudes = []
for x, y in vectors:
    magnitude = sqrt(x ** 2 + y ** 2)
    magnitudes.append(magnitude)
print(magnitudes)


# (1.2) comprehension approach
print('comprehension approach')
magnitudes = [sqrt(vector[0] ** 2 + vector[1] ** 2) for vector in vectors]
print(magnitudes)
# or
magnitudes = [sqrt(x ** 2 + y ** 2) for x, y in vectors]
print(magnitudes)

print()

# (2) perf_counter **
print('standard approach - perf_counter')
from time import perf_counter
start = perf_counter()
for i in range(100_000):
    magnitudes = []
    for vector in vectors:
        magnitude = sqrt(vector[0] ** 2 + vector[1] ** 2)
        magnitudes.append(magnitude)
end = perf_counter()

elapsed_time = end - start
print(elapsed_time)

print('comprehension approach - perf_counter')
start = perf_counter()
for i in range(100_000):
    magnitudes = [sqrt(vector[0] ** 2 + vector[1] ** 2) for vector in vectors]
end = perf_counter()

elapsed_time = end - start
print(elapsed_time)

print()


# (3)
# the comprehension syntax also allows for an if-clause to filter elements
# we want to include in the resulting list. And this filter works by essentially using an
# expression, applying that expression which may or may not include using the element that's
# returned in the loop. But whatever that expression is, it gets evaluated.

# If the expression is true, then it goes ahead and evaluates this expression and includes it
# in the list.

# (3.1) standard approach
strings = "Python is an awesome language".split(' ')
print(strings)
print('standard approach')
filtered = []
for item in strings:
    if len(item) >= 5:
        filtered.append(item)
print(filtered)

# (3.2) comprehension approach
print('comprehension approach')
filtered = [item for item in strings if len(item) >= 5]
print(filtered)


# (4) The iterable used in the comprehension can be any iterable

print()
sales = {
    'widget 1': 0,
    'widget 2': 5,
    'widget 3': 10,
    'widget 4': 2
}

# (4.1) standard approach
print("standard approach")
high_sales = []
for key, value in sales.items():
    if value >= 5:
        high_sales.append(key)
print(high_sales)

# (4.2) comprehension approach
print("comprehension approach")
high_sales = [key for key, value in sales.items() if value >= 5]
print(high_sales)


# (5) matrix example
print()
# (5.1) standard approach
print("standard approach")
m = [[0] * 3] * 3
print(m)
print(m[0] is m[1])
m[0][0] = 100
print(m)

# (5.2) comprehension approach
print("comprehension approach")
# Technically, this 'row' is not a variable that we use
# So we have it because we need something when we have the 'for' we need 'for' sth in sth
m = [[0, 0, 0] for row in range(3)]
# A common way in Python it's more of a convention is to use a variable name with ust a single '_' underscore.
m = [[0, 0, 0] for _ in range(3)]
# Single underscore '_' is a valid variable name because variables have to have one or more characters and
# the first character can be an '_' underscore.

print(m)
print(m[0] is m[1])
m[0][0] = 100
print(m)

# we can use this way also.
m = [[0] * 3 for _ in range(3)]
print(m)
print(m[0] is m[1])


# (6) identity matrix and nested comprehension

print()
# (6.1) standard approach
print("standard approach")
m = [[0] * 3 for _ in range(3)]
for row in range(3):
    for col in range(3):
        if row == col:
            m[row][col] = 1
print(m)

# (6.2) comprehension approach
print("comprehension approach")

# Remember that the expression in a comprehension can be anything, including another comprehension
m = [[1 if row == col else 0 for col in range(3)] for row in range(3)]
# The thing that's interesting about comprehension is that 'row' variable is actually available in other
# comprehension also.
# in the inside comprehension we use 'ternary operator'
print(m)

# more readable
m = [
    [1 if row == col else 0 for col in range(3)]
    for row in range(3)
]


