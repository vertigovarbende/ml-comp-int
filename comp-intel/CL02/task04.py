"""
Given the following matrix:
m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

Make this matrix into an identity matrix (setting the diagonal elements to 1)
Your code should mutate 'm'
"""
m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(m)
for i in range(0, len(m)):
    for j in range(0, len(m)):
        if i == j:
            m[i][j] = 1
print(m)