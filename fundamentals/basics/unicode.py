# unicode
# first look at the pdfs! then look at the 'coding' section

"""
s = "The letter beta is \N{Greek Small Letter Beta}"
print(s)
s = "The letter beta is \N{Greek Small Letter Omega}"
print(s)
s = "The letter beta is \N{Greek Small Letter Delta}"
print(s)
s = "The letter beta is \N{snake}"
print(s)
"""

# (1) ord() function

print(ord('A')) # 65
beta = "\N{Greek Small Letter Beta}"
print(f'{beta}: {ord(beta)}')
snake = "\N{snake}"
print(f'{snake}: {ord(snake)}')

print()

# (2) hex() function
print(f'A: {hex(ord("A"))}')
print(f'{beta}: {hex(ord(beta))}')
print(f'{snake}: {hex(ord(snake))}')


# int()
print(int(3.14))
print(int("3B1", 16))
