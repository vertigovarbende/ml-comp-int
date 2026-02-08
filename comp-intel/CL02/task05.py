"""
Write some code that generates an `m` x `n` multiplication table.
For example if `m=3` and `n=4` your output should look something like:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
---------------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
---------------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
---------------
"""

m = int(input("enter m: "))
n = int(input("enter n: "))
for row in range(1, m + 1):
    for col in range(1, n + 1):
        print(f'{row} x {col} = {row * col}')
    print("-" * 10)