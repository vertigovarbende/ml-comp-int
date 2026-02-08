# int + float   --> returns float
print(1 + 0.5)
print(1.0 + 0.5)

# int * float   --> returns float
print(2 * 1.125)

# int / float   --> returns float! // we'll see integer division as well!
print(18 / 4)

# Power operator (**)
print(2 ** 8)   # 2^8 --> 256
print(2 ** (-8)) # 2^-8 --> 1 / (2 ** 8) --> 1 / 256
print(1 / (2 ** 8))

# Power operator with float numbers
print(4.0 ** 0.5)
print((-4.0) ** 0.5) # Complex numbers, real numbers, they're all like floats basically under the hood.

# Complex numbers
c = (-4) ** 0.5 # So now 'c' is this number here and it is an object. It's a complex number
print(c)
# We can look at function called type to tell us what is the type of a variable
print(type(c)) # complex
print(type(10)) # int
print(type(10.0)) # float

# So 'c' is a complex number, it is an object and that object has attributes, it has state and
# functionality
# For example, we can look at the real part of that complex number or we can look at the imaginary
# part
print(c.real)
print(c.imag)

# If you do want to create your own complex number using a literal, then you just type sth like
c = 10 + 2j
print(c)

# How do they actually work?
# Well, as We mentioned in the lecture, the actual operation itself, the evaluation is actually determined
# by the type itself, so by the INT or the FLOAT.
# So If we say '10 + 5', it's actually going to use the implementation for add for the integer class, for the integer type.
# Same thing multiplication would be handled by the MUL operator, for example
print(5 * 2)
print((5).__mul__(2))

# So instead of doing '1 + 2', which is usually how we're going to write things, we could also have
# use the add method of the integer object '1'.
print(1 + 2)
a = 1
print(a.__add__(2))


# The reasoun why this method is interesting and why it's interesting to know that it's actually
# using this method is when we create our custom objects, we can actually define now addition
# We can define what addition means for our custom types.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'



v1 = Vector(1, 1)
v2 = Vector(2, 3)
print(v1)
print(v2)
# when we do that, we will get an error
# print(v1 + v2)

# So what we're going to do is we're going to define that in the object itself
# __add__ method

print(v1.__add__(v2).__repr__()) # Vector(3, 4)
print(v1.__add__(v2)) # Vector(3, 4)
print(v1 + v2) # v1.__add__(v2).__repr_() --> Vector(3, 4)

# So why is sth like this really useful?
# Well, there's all kinds of applications of this.

# So this kind of programming kind of encapsulated hides the actual implementation of
# merging to Vectors, and it makes our syntax when we actually use it very simple.

