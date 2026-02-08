a = 10
b = 10

print(a == b) # true

c = 10.0

print(a == c) # true
print(a is c) # false

print()

# 1
d = 20
print(id(a))
print(id(d))
print(a == d) # false
print(a is d) # false
print(id(a) == id(d)) # false

print()

# id() This is that memory address that I was talking about. It will show the address of the object in memory
a = d
print(id(a))
print(id(d))
print(a is d) # true
print(a == d) # true
print(id(a) == id(b)) # true

print()

# 2 i didn't do a = b // small number
a = 10
print(id(a))
print(id(b))
print(id(a) == id(b)) # true

print()

# 3
a = 10_000
b = 10_000
print(id(a))
print(id(b))
print(id(a) == id(b))

print()

# 3.v2

a = 100_000_000
b = 100_000_000
print(id(a))
print(id(b))
print(id(a) == id(b))

print()

# == is same as '+'
print((10 != 12)) # True
print(10.5 != 10.5) # False
print(a == b) # True
print(a.__eq__(b)) # True

print()

# >=
print(10 >= 5)
print(10.5 < 100)

print()

# We can use '==' operator between complex number but we cannot use > < operator between these numbers
# bcz '<' or others not supported between instance of 'complex' and 'complex'

a = 1 + 1j
b = 1 + 1j
c = 2 + 2j

print(a == b) # True
print(a == c) # False
# print(a > b) error
# print(a > c) error

print(id(a))
print(id(b))

print()

b = c
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(c is b)

print()

# we should not use '==' operator for float numbers

print(0.1 * 3 == 0.3) # False
a = 0.1 * 3
b = 0.3
print(id(a))
print(id(b))
print(a is b) # False

print()
print()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)

print(id(v1))
print(id(v2))
print(id(v3))
print(v1 is v2)
print(v1 is v3)
print(v2 is v3)

print()

# v1 = v2
# print(id(v1))
# print(id(v2))
# print(v1 is v2) # True

# Well, by default, when you create your own custom types, Python will basically use identity comparison for
# the equality for '==' because it doesn't know how to compare two custom objects. It says
# Well, the only thing I know is the memory address. I am going to use that.
# So this is why we get a false.
print(v1 == v2) # False # if you remove __eq__ method in Vector class, you will see that this expression'll return false

print(v1.__eq__(v2))

# Of course we can override that. We can basically define what we want to mean by equality.
print(v1 == v2) # True
print(v1.__eq__(v2)) # True


# BUNLARI '<' VE '>' icinde dene!
# adamın kaynaklarında bunlar varmıs zaten!


