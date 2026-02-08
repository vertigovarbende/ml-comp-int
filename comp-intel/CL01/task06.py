# (1) Create a method calculator with parameters x1, op and x2
# x1 and x2 are numbers, op is one of the following math operations: ‘+’, ‘-‘, ‘*’, ‘/’
def calculator(x1, op, x2):
    if op == '+':
        return x1 + x2
    elif op == '-':
        return x1 - x2
    elif op == '*':
        return x1 * x2
    elif op == '/':
        return x1 / x2
    else:
        return "Invalid operator"


# (2) The method should return the result of the operation between x1 and x2, e.g.
# x1 = 12, x2 = 5, op = ‘-‘ will return 7.
result = calculator(12, '-', 5)
print(result)
