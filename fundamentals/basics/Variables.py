# integer
a = 100
print(a)
print(a + 11)
b = a + 11
print(b)

# float
a = 3.14 # now 'a' pointing float object
print(a)

# naming rules
# valid
test = 100
test_1 = 10
_test_1_ = 10
__test__ = 10
TEST = 10

print(test)
print(test_1)
print(_test_1_)
print(__test__)
print(TEST)

# not valid
# 1_test = 10
# print(1_test)

# don't use a reserved word
# if = 10

a = (float) (10)
print(a)
print(a.as_integer_ratio()) # (10, 1)

float = 100.5
print(float)

# The example below won't work because we've already defined a variable called 'flaot'
# a = (float) (12.4)
# print(a)

del float   # we deleted this variable
print(float)
a = (float)(12)
print(a)

# snake case naming
current_balance = 100.0
print(current_balance)

# Python using snake case naming by convention
# So don't use camel case naming
currentBalance = 100.5
print(currentBalance)

# When you want to define a variable, try to name this variable meaningful
# Code has to be human readable

# Compare the following two examples
x = 100
y = 0.1
z = 10

r = x * (1 + y / 12) ** (z * 12)
print(r)

principal = 100
apr = 0.1
years = 10

future_value = principal * ((1 + apr / 12) ** (years * 12))
print(future_value)






