# for loop and 'enumerate()' function
# look at the pdfs first! then look at the 'coding' section

"""
data = [10, 20, 30, -10, 40, -5]
for t in enumerate(data):
    index, element = t
    if element < 0:
        data[index] = 0
print(data)
# or
data = [10, 20, 30, -10, 40, -5]
for index, element in enumerate(data):
    if element < 0:
        data[index] = 0
print(data)
"""


# (1) 'for' loop
suits = ["spades", "hearts", "diamonds", "clubs"]
for suit in suits:
    print(f'{suit[0].upper()} = {suit}')


# (2) 'for' loops are used to iterate over anything that is iterable
# for example, a list, a tuple, and of course a string

# (2.1) 'for' loop for a list
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)

# (2.2) 'for' loop for a tuple
t = 1, 2, 3, 4, 5
for i in t:
    print(i)

# (2.3) 'for' loop for a string
for c in 'python':
    print(c)

print()
# (3) the variable that we created in 'for' loop will be in memory.
# what that means is that this variable after the loop has finished running is still around.
# when we execute that and we will see that
print(c)
print(suit)


# (4) range object and 'range()' function with 'for' loop
# often when we are dealing with 'for' loops, we want to repeat things a certain number of times
# or maybe just over a sequence of integers
# in this case we can use the range object to do precisely that.
for i in range(2, 11, 2):
    print(i)

# or
l = list(range(2, 11, 2))
print(l)


# (5) nested loops
# the loop body can also contain a loop, and that's called a nested loop
print()
for i in range(3):
    for j in range(3):
        print(f'i = {i}, j = {j}')
    print('-' * 12)

# we can use nested loops to iterate through every element of a matrix

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""
for row_idx in range(3):
    for col_idx in range(3):
        print(f'[{row_idx}][{col_idx}] = {m[row_idx][col_idx]}')
    print("-" * 10)
"""
# we may not know the length of row and column
# its means that the matrix may not square matrix
for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx}][{col_idx}] = {m[row_idx][col_idx]}')
    print("-" * 10)
# it can handle that ragged array
m = [
    [0, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9],
    [10]
]
for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx}][{col_idx}] = {m[row_idx][col_idx]}')
    print("-" * 10)
# we could also use a nested loop to build an end by an identity matrix for any end.
# identity matrix
"""
n = int(input("Enter an integer number: "))
matrix = []
for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        print(matrix[row_idx][col_idx], end = " ")
    print()
"""


# (6) 'enumerate()' function
# 'enumerate()' function is a function that takes in an iterable as an argument
# and returns an iterable of tuples, where the first element of the tuple is a sequential
# integer number starting at zero.
# and then the second element is the value in the iterable itself.
data = [10, 20, 30]
# it doesn't actually create this enumeration yet, but it creates something that is iterable
# and that will hand us the data that we are looking for one by one.
print(enumerate(data))
l = list(enumerate(data))
print(l)
# the index number followed by the actual element that we want to iterate over n the data list
# so we can loop over data and get the corresponding index numbers by essentially looping
for t in enumerate(data):
    print(t)
# we can unpack the tuple
for t in enumerate(data):
    index, element = t
    print(f'{index} = {element}')
# but we can actually do the unpacking directly in the for loop itself
for index, element in enumerate(data):
    print(index, element)

# so we can look at ragged array
m = [
    [0, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9],
    [10]
]
# it is easy to write but we cannot reach the index and element directly
for row in m:
    for element in row:
        print(element)
# following example is same thing
# this example seems like hard to read but we can reach the index and element
"""
for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(m[row_idx][col_idx])
"""
print()
# in this case we can use 'enumerate()' function
for row_idx, row in enumerate(m):
    for col_idx, element, in enumerate(row):
        print(f'[{row_idx}][{col_idx}] = {element}')
    print("-" * 10)

# another example
print()
data = [10.5, 11.2, 9.8, None, 11.5, None]
# so here's the data and we want to replace these none values with the average of the
# values in the sequence 'data'
"""
total = 0.0
count = 0
for i in range(len(data)):
    if data[i] is not None:
        total += data[i]
        count += 1
avg = total / count
for i in range(len(data)):
    if data[i] is None:
        data[i] = avg
print(data)
"""
# we can do like this
"""
total = 0.0
count = 0
for value in data:
    if value is not None:
        total += value
        count += 1
avg = total / count
print(avg)
for index, value in enumerate(data):
    if value is None:
        data[index] = avg
print(data)
"""


# MORE PYTHONIC - we'll see later
# essentially we are using what is called 'comprehension'
data = [10.5, 11.2, 9.8, None, 11.5, None]
count = sum(1 for val in data if val is not None)
total = sum(val for val in data if val is not None)
avg = total / count
data = [val if val is not None else avg for val in data]
print(data)

# Python statistics module - we'll see later
from statistics import fmean
data = [10.5, 11.2, 9.8, None, 11.5, None]
avg = fmean(val for val in data if val is not None)
print(avg)
data = [val if val is not None else avg for val in data]
print(data)

# pandas library - we'll see later
# we have to add 'pandas' module in this project!
