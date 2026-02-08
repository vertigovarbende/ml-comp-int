# random module
# for using the random module, you have to import
import random as rand

# (0) random functions
# random() -> 0.0 ile 1.0 float number
print(rand.random())

# randint(a,b) -> it will return random integer number between a and b and both are inclusive
print(rand.randint(0, 10))

# randrange(a) -> it will return random integer number BUT
# if you pass one argument like above, it returns an integer number between 0 and 'a' and 'a' is exclusive!
print(rand.randrange(10))
# if you pass two arguments like randrange(a, b), it returns an integer number between 'a' and 'b'
# and 'b' is exlcusive!
print(rand.randrange(5, 10))

# uniform(a, b) -> it will return random float number between a and b and both are inclusive
print(rand.uniform(1, 2))

# choice(seq) -> this function takes a sequence as argument and returns random element from that sequence
l = [1, 2, 3, 4, 5]
print(rand.choice(l))

# shuffle(seq) -> this function takes a sequence as argument and shuffles that sequence
l = [2, 4, 6, 8]
rand.shuffle(l)
print(l)
for value in l:
    print(value, end = " ")
print()

# sample(seq, k): it selects unique element from the specified sequence for k times
# and it returns a list as a sample!

l = list(range(100))
print(rand.sample(l, 5))

t = tuple(range(100))
print(rand.sample(t, 5))

s = 'abcdefgh'
print(rand.sample(s, 5))

# ex1:

def recursive_add(sayi):
    if sayi == -1:
        return -1
    return sayi + recursive_add(sayi + 1)

sayi = int(input("Enter an negative integer number: "))
print(recursive_add(sayi))


# ex2:

def is_even_number(number):
    if number % 2 == 0:
        return True
    return False

def add_even_number(number):
    if number == 0:
        return 0
    elif is_even_number(number):
        return number + add_even_number(number - 1)
    else:
        return add_even_number(number - 1)

number = int(input("Enter an integer number: "))
add_number = add_even_number(number)
print(add_number)



def even_number_add(number):
    if number == 0:
        return 0
    else:
        return number + even_number_add(number - 2)

number = int(input("Enter an integer number: "))
print(even_number_add(number))


# ex3:

weight = float(input("Enter your weight as 'kg': "))
height = float(input("Enter your height as 'm': "))
vki = (weight / (height ** 2))
state = ""

if vki <= 18:
    state = "zayif"
elif vki <= 25:
    state = "normal"
elif vki <= 30:
    state = "kilolu"
elif vki < 35:
    state = "obez"
else:
    state = "ciddi obez"
print(f"Your state is {state} and your vki is {vki}")


# ex4:

number = int(input("Enter an integer number: "))
tek_sayilar = 0
cift_sayilar = 0

for i in range(number):
    if i % 2 == 0:
        cift_sayilar += i
    else:
        tek_sayilar += i

print(f'cift: {cift_sayilar}, tek: {tek_sayilar}')





# 3x4
a = [
    [3, 1, 1, 4],
    [5, 3, 2, 1],
    [6, 2, 9, 5]
]
# 4x2
b = [
    [4, 9],
    [6, 8],
    [9, 7],
    [7, 6]
]
# multiplication of these matrix will be 3x2
c = [
    [0, 0],
    [0, 0],
    [0, 0]
]

for i in range(len(a)): # row
    for j in range(len(b[0])): # column
        for k in range(len(b)): # multiplication
            c[i][j] += a[i][k] * b[k][j]
# display 'c' matrix
print()
for row in c:
    for element in row:
        print(element, end = " ")
    print()


# 2x3
a = [
    [1, 2, 3],
    [4, 5, 6]
]

# 3x2
b = [
    [10, 11],
    [20, 21],
    [30, 31]
]

# 2x2
c = [
    [0, 0],
    [0, 0]
]

for i in range(len(a)): # row
    for j in range(len(b[0])): # column
        for k in range(len(b)): # multiplication
            c[i][j] += a[i][k] * b[k][j]
print()
for row in c:
    for element in row:
        print(element, end = " ")
    print()


