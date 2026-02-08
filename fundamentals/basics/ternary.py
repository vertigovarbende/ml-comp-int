# ternary operator
# look at the pdfs first! then look at the 'coding' section

# <exp1> if <condition> else <exp2>

# (1)
"""
price = 72
if price < 100:
    volume = 10
else:
    volume = 1

print(volume)
# we can be re-written using a conditional ternary operator

volume = 10 if price < 100 else 1
print(volume)
"""

# (2)
"""
a = 10
b = 20

variable = (a - b) if a > b else (b - a)
print(variable)
"""

# (3) Short-Circuiting
# Just like we saw with Boolean operators, the ternary operator also uses short-circuit evaluation

# <exp1> if <condition> else <exp2>
#   - first evaluates <condition>
#   - if it is True, evaluates and returns <exp1>
#       - but does not evaluate <exp2>

#    - if it is False, evaluates and returns <exp2>
#       - but does not evaluate <exp1>

# Example
"""
a = 20
b = 10
result1 = a / b if b != 0 else 'NaN'
print(result1)
b = 0
result2 = a / b if b != 0 else 'NaN'
print(result2)
"""

# (4)
"""
ask_price = 100
if ask_price > 50:
    volume = 50
else:
    volume = 80
print(volume)
"""

"""
ask_price = 100
volume = 50 if ask_price > 50 else 80
print(volume)
"""

# (5)
"""
a = 20
b = 10
# print(abs(10 - 20))
# lets say we forgot the 'abs' function

distance = a - b if a >= b else b - a
print(distance)
"""

# (6)
"""
current_value = -999
running_total = 15_000
running_count = 125

running_total = running_total + (0 if current_value == -999 else current_value)
print(running_total)
"""

















