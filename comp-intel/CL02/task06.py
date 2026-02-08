"""
You are given the following tuple of lists:
data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)
Your program should:
1. Mutate the lists in `data` to add one more element indicating the distance between the two integer numbers (i.e. the absolute value fo the difference)
2. Determine on which date this newly calculate value was the largest.
3. Be able to work for a `data` set containing any number of lists.
"""

# sol1

data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)
largest = 0, abs(data[0][1] - data[0][2])
for i in range(len(data)):
    if largest[1] <= abs(data[i][1] - data[i][2]):
        largest = i, abs(data[i][1] - data[i][2])
    data[i].append(largest[1])
for row in data:
    print(row)
print(data[largest[0]][0])