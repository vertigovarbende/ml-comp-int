# (1) Create a list x with values 5, 10 and 15.
x = [5, 10, 15]

# (2) Print it.
print(x)
print(type(x))
print(len(x))

# (3) Add 20 to the end of list x and print it again
x.append(20)
print(x)
print(type(x))
print(len(x))

# (4) Print now only the second and third value (10, 15) with a single command.
print(x[1], x[2])

# (5) Replace the first value (5) of x with 2.
x[0] = 2
print(x[0])
print(x)

# (6) Add 16 and 18 between the values 15 and 20 of x.
x.insert(3, 16)
x.insert(4, 18)

# (7) Print x, it should look like [2, 10, 15, 16, 18, 20].
print(x)