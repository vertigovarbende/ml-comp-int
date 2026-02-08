# Operator Precedence

print(100 - 20 + 50)
print((100 - 20) + 50)
print((100 + 50) - 20)

print(10 * 4 + 5 * 5)
print((10 * 4) + (5 * 5))

# Power operator
print(10 * 2 ** 3) # (10 * (2 ** 3)) --> 10 * 8 --> 80

# Example
principal = 100
apr = 0.1
years = 10
future_value = principal * ((1 + apr / 12) ** (years * 12))
print(future_value)
# we can also write like this, because '**' operator precedence higher than '*'
future_value = principal * (1 + apr / 12) ** (years * 12)
print(future_value)

print(2 ** (-8))
print(-2 ** 8) # -256
print((-2) ** 8) # 256

print(-4 ** 0.5) # -(4 ** 0.5) --> -2
print((-4) ** 0.5) # complex number

n = 10
print(n * n - 1) # (n * n) - 1
print(n * (n - 1))


